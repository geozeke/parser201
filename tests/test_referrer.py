#!/usr/bin/env python3
"""Test the referrer attribute."""

import lzma
import pickle
from pathlib import Path

from parser201.classes import LogParser

p = Path(__file__).resolve().parent
TESTDATA = p / "data_parser201.bin"


def pytest_generate_tests(metafunc):
    """Use the pytest_generate_tests hook to create test cases.

    Parameters
    ----------
    metafunc : obj
        The python object that facilitates parametrization.
    """
    with lzma.open(TESTDATA, "rb") as f:
        test_cases = pickle.load(f)
    metafunc.parametrize("node", test_cases)


def test_referrer(node):
    """Test referrer.

    Parameters
    ----------
    node : dict
        A dictionary object containing a test string and expected
        results for various tests.
    """
    lp = LogParser(
        node["linein"], timezone=node["timezone"], dts_format=node["dts_format"]
    )
    test_result = lp.referrer
    benchmark = node["referrer"]
    assert test_result == benchmark
