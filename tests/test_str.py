#!/usr/bin/env python3

# --------------------------------------------------------------------------

import pytest
import pickle
import lzma
from pathlib import Path
from classes import LogParser

TESTDATA = str(Path(__file__).resolve().parent) + '/' + 'data_parser201.bin'

# Use the pytest_generate_tests hook to create test cases from the data file.


def pytest_generate_tests(metafunc):
    with lzma.open(TESTDATA, 'rb') as f:
        testCases = pickle.load(f)
    testCases = [N for N in testCases]
    metafunc.parametrize('node', testCases)

# -------------------------------


def test_str(node):
    noneStr = str(LogParser('bad line'))
    lp = LogParser(node['linein'])
    testResult = str(lp)
    if lp.ipaddress is None:
        benchmark = noneStr
    else:
        benchmark = node['str']
    assert testResult == benchmark
