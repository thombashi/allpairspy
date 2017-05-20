#!/usr/bin/env python
# encoding: utf-8

"""
Demo of the basic functionality - just getting pairwise/n-wise combinations
"""

from __future__ import print_function

from allpairspy import AllPairs


parameters = [
    ["Brand X", "Brand Y"],
    ["98", "NT", "2000", "XP"],
    ["Internal", "Modem"],
    ["Salaried", "Hourly", "Part-Time", "Contr."],
    [6, 10, 15, 30, 60],
]
# sample parameters are is taken from
# http://www.stsc.hill.af.mil/consulting/sw_testing/improvement/cst.html

print("TRIPLEWISE:")
for i, pairs in enumerate(AllPairs(parameters, n=3)):
    print("{:2d}: {}".format(i, pairs))
