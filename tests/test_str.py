#!/usr/bin/env python3
"""Test the str attribute."""

import lzma
import pickle
from pathlib import Path

from parser201.classes import LogParser

p = Path(__file__).resolve().parent
TESTDATA = p/'data_parser201.bin'


def pytest_generate_tests(metafunc):
    """Use the pytest_generate_tests hook to create test cases.

    Parameters
    ----------
    metafunc : obj
        The python object that facilitates parametrization.
    """
    with lzma.open(TESTDATA, 'rb') as f:
        test_cases = pickle.load(f)
    metafunc.parametrize('node', test_cases)


def test_str(node):
    """Test the str attribute.

    Parameters
    ----------
    node : dict
        A dictionary object containing a test string and expected
        results for various tests.
    """
    none_str = str(LogParser('bad line'))
    lp = LogParser(node['linein'],
                   timezone=node['timezone'],
                   dts_format=node['dts_format'])
    test_result = str(lp)
    if lp.ipaddress is None:
        benchmark = none_str
    else:
        benchmark = node['str']
    print(f"timezone: {node['timezone']}")
    print(f"  dts_format: {node['dts_format']}\n")
    print(f"received:\n{test_result}\n")
    print(f"expected:\n{node['str']}")
    assert test_result == benchmark
