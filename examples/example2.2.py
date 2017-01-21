#!/usr/bin/env python
# encoding: utf-8

from __future__ import print_function
import functools

from allpairspy import AllPairs

"""
Another demo of filtering capabilities.
Demonstrates how to use named parameters
"""


def is_valid_combination(values, names):

    dictionary = dict(zip(names, values))

    """
    Should return True if combination is valid and False otherwise.
    
    Dictionary that is passed here can be incomplete.
    To prevent search for unnecessary items filtering function
    is executed with found subset of data to validate it.
    """

    rules = [
        # Brand Y does not support Windows 98
        # Brand X does not work with XP
        # Contractors are billed in 30 min increments
        lambda d: "98" == d["os"] and "Brand Y" == d["brand"],
        lambda d: "XP" == d["os"] and "Brand X" == d["brand"],
        lambda d: "Contr." == d["employee"] and d["increment"] < 30
    ]

    for rule in rules:
        try:
            if rule(dictionary):
                return False
        except KeyError:
            pass

    return True

# sample parameters are is taken from
# http://www.stsc.hill.af.mil/consulting/sw_testing/improvement/cst.html
parameters = [
    ("brand", ["Brand X", "Brand Y"]),
    ("os", ["98", "NT", "2000", "XP"]),
    ("network", ["Internal", "Modem"]),
    ("employee", ["Salaried", "Hourly", "Part-Time", "Contr."]),
    ("increment", [6, 10, 15, 30, 60])
]

pairwise = AllPairs(
    [x[1] for x in parameters],
    filter_func=lambda values: is_valid_combination(
        values, [x[0] for x in parameters])
)

for i, parameter in enumerate(pairwise):
    print("{:2d}: {}".format(i, parameter))
