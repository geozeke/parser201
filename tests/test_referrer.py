#!/usr/bin/env python3
"""Test the referrer attribute."""

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
    testCases = [N for N in testCases]
    metafunc.parametrize('node', testCases)


def test_referrer(node):
    """Test ipaddress.

    Parameters
    ----------
    node : dict
        A dictionary object containing a test string and expected
        results for various tests.
    """
    lp = LogParser(node['linein'],
                   timezone=node['timezone'],
                   dtsformat=node['dtsformat'])
    testResult = lp.referrer
    benchmark = node['referrer']
    assert testResult == benchmark
