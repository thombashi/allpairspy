# encoding: utf-8

from six.moves import range

from .combinatorics import xuniqueCombinations


class Node(object):

    @property
    def id(self):
        return self.__node_id

    @property
    def counter(self):
        return self.__counter

    def __init__(self, node_id):
        self.__node_id = node_id
        self.__counter = 0
        self.in_ = set()
        self.out = set()

    def __str__(self):
        return str(self.__dict__)

    def inc_counter(self):
        self.__counter += 1


def key(items):
    return "->".join([x.id for x in items])


class pairs_storage(object):

    def __init__(self, n):
        self.__n = n
        self.__nodes = {}
        self.__combs_arr = [
            set() for _i in range(n)
        ]

    def add(self, comb):
        n = len(comb)
        assert(n > 0)

        self.__combs_arr[n - 1].add(key(comb))
        if n == 1 and comb[0].id not in self.__nodes:
            self.__nodes[comb[0].id] = Node(comb[0].id)
            return

        ids = [x.id for x in comb]
        for i, id in enumerate(ids):
            curr = self.__nodes[id]
            curr.inc_counter()
            curr.in_.update(ids[:i])
            curr.out.update(ids[i + 1:])

    def add_sequence(self, seq):
        for i in range(1, self.__n + 1):
            for comb in xuniqueCombinations(seq, i):
                self.add(comb)

    def get_node_info(self, item):
        return self.__nodes.get(item.id, Node(item.id))

    def get_combs(self):
        return self.__combs_arr

    def __len__(self):
        return len(self.__combs_arr[-1])
