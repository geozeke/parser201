#!/usr/bin/env python3
"""Test the timestamp."""

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


# -------------------------------


def test_timestamp(node):
    """Test the timestamp attribute.

    Parameters
    ----------
    node : dict
        A dictionary object containing a test string and expected
        results for various tests.
    """
    lp = LogParser(
        node["linein"], timezone=node["timezone"], dts_format=node["dts_format"]
    )
    test_result = lp.timestamp
    benchmark = node["timestamp"]
    print(f" timezone: {node['timezone']}")
    print(f"dts_format: {node['dts_format']}")
    assert test_result == benchmark
