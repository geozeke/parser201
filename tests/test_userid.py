#!/usr/bin/env python3

# --------------------------------------------------------------------------

import lzma
import pickle
from pathlib import Path

import pathprep

from classes import LogParser  # isort: skip

TESTDATA = Path(__file__).resolve().parent/'data_parser201.bin'

# Use the pytest_generate_tests hook to create test cases from the data file.


def pytest_generate_tests(metafunc):
    with lzma.open(TESTDATA, 'rb') as f:
        testCases = pickle.load(f)
    metafunc.parametrize('node', testCases)

# -------------------------------


def test_userid(node):
    lp = LogParser(node['linein'],
                   timezone=node['timezone'],
                   dtsformat=node['dtsformat'])
    testResult = lp.userid
    benchmark = node['userid']
    assert testResult == benchmark
