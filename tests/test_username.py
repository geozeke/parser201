#!/usr/bin/env python3

# --------------------------------------------------------------------------

import lzma
import pickle
from pathlib import Path

import pathprep  # noqa

from classes import LogParser  # isort: skip

TESTDATA = Path(__file__).resolve().parent/'data_parser201.bin'

# Use the pytest_generate_tests hook to create test cases from the data file.


def pytest_generate_tests(metafunc):
    with lzma.open(TESTDATA, 'rb') as f:
        testCases = pickle.load(f)
    testCases = [N for N in testCases]
    metafunc.parametrize('node', testCases)

# -------------------------------


def test_username(node):
    lp = LogParser(node['linein'],
                   timezone=node['timezone'],
                   format=node['fmt'])
    testResult = lp.username
    benchmark = node['username']
    assert testResult == benchmark
