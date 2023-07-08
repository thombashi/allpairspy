#!/usr/bin/env python3

from collections import OrderedDict

from allpairspy import AllPairs


parameters = OrderedDict(
    {"brand": ["Brand X", "Brand Y"], "os": ["98", "NT", "2000", "XP"], "minute": [15, 30, 60]}
)

print("PAIRWISE:")
for i, pairs in enumerate(AllPairs(parameters)):
    print(f"{i:2d}: {pairs}")
