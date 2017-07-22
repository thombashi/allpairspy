#!/usr/bin/env python
# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

from __future__ import print_function
from __future__ import unicode_literals

import pytest

from allpairspy import AllPairs


def function_to_be_tested(brand, operating_system, minute):
    # do something

    return True


class Test__parameterized(object):

    @pytest.mark.parametrize(
        ["brand", "operating_system", "minute"],
        [
            value_list for value_list in AllPairs([
                ["Brand X", "Brand Y"],
                ["98", "NT", "2000", "XP"],
                [10, 15, 30, 60]
            ])
        ])
    def test(self, brand, operating_system, minute):
        assert function_to_be_tested(brand, operating_system, minute)
