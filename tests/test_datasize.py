#!/usr/bin/env python3
"""Test the dataSize attribute."""

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


def test_datasize(node):
    """Test datasize.

    Parameters
    ----------
    node : dict
        A dictionary object containing a test string and expected
        results for various tests.
    """
    lp = LogParser(node['linein'],
                   timezone=node['timezone'],
                   dtsformat=node['dtsformat'])
    testResult = lp.datasize
    try:
        benchmark = int(node['datasize'])
    except TypeError:
        benchmark = node['datasize']
    assert testResult == benchmark
