#!/usr/bin/env python3

"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

import pytest

from allpairspy import AllPairs


def function_to_be_tested(brand: str, operating_system: str, minute: int) -> bool:
    # do something

    return True


class TestParameterized:
    @pytest.mark.parametrize(
        ["brand", "operating_system", "minute"],
        [
            values
            for values in AllPairs(
                [["Brand X", "Brand Y"], ["98", "NT", "2000", "XP"], [10, 15, 30, 60]]
            )
        ],
    )
    def test(self, brand, operating_system, minute):
        assert function_to_be_tested(brand, operating_system, minute)
