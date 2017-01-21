#!/usr/bin/env python
# encoding: utf-8

from __future__ import print_function

from allpairspy import AllPairs


"""
Provided to make it easier to compare efficiency with other tools
as per http://pairwise.org/tools.asp

Current iutput is:

3^4: produces 9 rows
3^13: produces 17 rows
4^15 * 3^17 * 2^29: produces 37 rows
4^1 * 3^39 * 2^35: produces 27 rows
3^100: produces 29 rows
10^20: produces 219 rows
10^10: produces 172 rows

"""


def get_arrays(dimensions):
    opts = []

    for d in dimensions:
        r = []
        for _i in range(d[1]):
            r.append(range(d[0]))
        opts += r

    return opts


def print_result(dimensions):
    header_list = []
    for d in dimensions:
        header_list.append("%i^%i" % d)

    pairwise = AllPairs(get_arrays(dimensions))
    n = len(list(pairwise))

    print("{:s}: produces {:d} rows".format(" * ".join(header_list), n))


print_result(((3, 4), ))
print_result(((3, 13), ))
print_result(((4, 15), (3, 17), (2, 29)))
print_result(((4, 1), (3, 39), (2, 35)))
print_result(((3, 100), ))
print_result(((10, 20), ))
print_result(((10, 10), ))
