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
        testCases = pickle.load(f)
    metafunc.parametrize('node', testCases)


def test_str(node):
    """Test the str attribute.

    Parameters
    ----------
    node : dict
        A dictionary object containing a test string and expected
        results for various tests.
    """
    noneStr = str(LogParser('bad line'))
    lp = LogParser(node['linein'],
                   timezone=node['timezone'],
                   dtsformat=node['dtsformat'])
    testResult = str(lp)
    if lp.ipaddress is None:
        benchmark = noneStr
    else:
        benchmark = node['str']
    print(f"timezone: {node['timezone']}")
    print(f"  dtsformat: {node['dtsformat']}\n")
    print(f"received:\n{testResult}\n")
    print(f"expected:\n{node['str']}")
    assert testResult == benchmark
