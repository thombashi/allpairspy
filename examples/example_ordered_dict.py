#!/usr/bin/env python
# encoding: utf-8

from __future__ import print_function

from collections import OrderedDict

from allpairspy import AllPairs


parameters = OrderedDict({
    "brand": ["Brand X", "Brand Y"],
    "os": ["98", "NT", "2000", "XP"],
    "minute": [15, 30, 60],
})

print("PAIRWISE:")
for i, pairs in enumerate(AllPairs(parameters)):
    print("{:2d}: {}".format(i, pairs))
