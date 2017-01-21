# encoding: utf-8

from functools import cmp_to_key

from six.moves import (
    range,
    reduce,
)

from .pairs_storage import (
    pairs_storage,
    key,
)
from .combinatorics import xuniqueCombinations


class Item(object):

    @property
    def id(self):
        return self.__item_id

    @property
    def value(self):
        return self.__value

    def __init__(self, item_id, value):
        self.__item_id = item_id
        self.__value = value
        self.weights = []

    def __str__(self):
        return str(self.__dict__)


def get_max_comb_number(arr, n):
    items = [len(x) for x in arr]
    f = lambda x, y: x * y
    total = sum([reduce(f, z) for z in xuniqueCombinations(items, n)])
    return total


def cmp(lhs, rhs):
    if lhs.weights == rhs.weights:
        return 0

    return -1 if lhs.weights < rhs.weights else 1


class AllPairs(object):

    def __init__(
            self, options, filter_func=lambda x: True, previously_tested=[[]],
            n=2):
        """
        TODO: check that input arrays are:
            - (optional) has no duplicated values inside single array / or compress such values
        """

        if len(options) < 2:
            raise Exception("must provide more than one option")

        for arr in options:
            if not len(arr):
                raise Exception("option arrays must have at least one item")

        self.__filter_func = filter_func
        self.__n = n
        self.__pairs = pairs_storage(n)
        self.__max_unique_pairs_expected = get_max_comb_number(options, n)
        self.__working_arr = []

        for i in range(len(options)):
            self.__working_arr.append([
                Item("a%iv%i" % (i, j), value)
                for j, value in enumerate(options[i])
            ])

        for arr in previously_tested:
            if len(arr) == 0:
                continue
            elif len(arr) != len(self.__working_arr):
                raise Exception(
                    "previously tested combination is not complete")

            if not self.__filter_func(arr):
                raise Exception("invalid tested combination is provided")

            tested = []
            for i, val in enumerate(arr):
                idxs = [
                    Item(node.id, 0)
                    for node in self.__working_arr[i] if node.value == val
                ]

                if len(idxs) != 1:
                    raise Exception(
                        "value from previously tested combination is not found in the options or found more than once")
                tested.append(idxs[0])
            self.__pairs.add_sequence(tested)

    def __iter__(self):
        return self

    def next(self):
        return self.__next__()

    def __next__(self):
        assert(len(self.__pairs) <= self.__max_unique_pairs_expected)

        if len(self.__pairs) == self.__max_unique_pairs_expected:
            # no reasons to search further - all pairs are found
            raise StopIteration

        previous_unique_pairs_count = len(self.__pairs)
        chosen_values_arr = [None] * len(self.__working_arr)
        indexes = [None] * len(self.__working_arr)

        direction = 1
        i = 0

        while -1 < i < len(self.__working_arr):
            if direction == 1:  # move forward
                self.resort_working_array(chosen_values_arr[:i], i)
                indexes[i] = 0

            # scan current array or go back
            elif direction == 0 or direction == -1:
                indexes[i] += 1
                if indexes[i] >= len(self.__working_arr[i]):
                    direction = -1
                    if i == 0:
                        raise StopIteration
                    i += direction
                    continue
                direction = 0
            else:
                raise Exception("next(): unknown 'direction' code.")

            chosen_values_arr[i] = self.__working_arr[i][indexes[i]]

            if self.__filter_func(
                    self.__get_values_array(chosen_values_arr[:i + 1])):
                assert(direction > -1)
                direction = 1
            else:
                direction = 0
            i += direction

        if len(self.__working_arr) != len(chosen_values_arr):
            raise StopIteration

        self.__pairs.add_sequence(chosen_values_arr)

        if len(self.__pairs) == previous_unique_pairs_count:
            # could not find new unique pairs - stop
            raise StopIteration

        # replace returned array elements with real values and return it
        return self.__get_values_array(chosen_values_arr)

    def resort_working_array(self, chosen_values_arr, num):
        for item in self.__working_arr[num]:
            data_node = self.__pairs.get_node_info(item)

            new_combs = []
            for i in range(0, self.__n):
                # numbers of new combinations to be created if this item is
                # appended to array
                new_combs.append(
                    set([
                        key(z) for z in xuniqueCombinations(
                            chosen_values_arr + [item], i + 1)
                    ]) - self.__pairs.get_combs()[i])

            # weighting the node
            # node that creates most of new pairs is the best
            item.weights = [-len(new_combs[-1])]

            # less used outbound connections most likely to produce more new
            # pairs while search continues
            item.weights += [len(data_node.out)]
            item.weights += [len(x) for x in reversed(new_combs[:-1])]
            item.weights += [-data_node.counter]  # less used node is better

            # otherwise we will prefer node with most of free inbound
            # connections; somehow it works out better ;)
            item.weights += [-len(data_node.in_)]

        self.__working_arr[num].sort(key=cmp_to_key(cmp))

    def __get_values_array(self, item_list):
        return [item.value for item in item_list]
