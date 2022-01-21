#!/usr/bin/env python3

"""Generate data for testing."""
# Author: Peter Nardi
# Date: 01/16/22
# License: (see MIT License at the end of this file)

# Title: Test data generator for parser201

# Imports

import lzma
import pickle
import random
import sys
from pathlib import Path

import pathprep

from classes import FMT  # isort: skip
from classes import TZ  # isort: skip
from classes import LogParser  # isort: skip

# Globals

ZONES = list(TZ)
FORMATS = list(FMT)

# --------------------------------------------------------------------------
# Helper function to create data dictionaries


def makeDict(dataIn, options):
    """Make a dictionary from test data.

    This function takes some generated test data, and stores it in a
    dictionary for later pickling into a file. This pickled file will be
    used for testing.

    Parameters
    ----------
    dataIn : str
        A line from an Apache log file. This will come from one of the
        files in `datasources`.
    options : (TZ, FMT)
        Various combinations of timezone formats and datetime formats
        are used when generating test data.

    Returns
    -------
    dict
        A dictionary with all the key/value pairs set to various
        elements needed for testing.
    """
    D = {}

    lp = LogParser(dataIn, timezone=options[0], format=options[1])

    D['linein'] = dataIn
    D['ipaddress'] = lp.ipaddress
    D['userid'] = lp.userid
    D['username'] = lp.username
    D['timestamp'] = lp.timestamp
    D['requestline'] = lp.requestline
    D['statuscode'] = lp.statuscode
    D['datasize'] = lp.datasize
    D['referrer'] = lp.referrer
    D['useragent'] = lp.useragent
    D['str'] = str(lp)
    D['timezone'] = options[0]
    D['fmt'] = options[1]

    return D

# --------------------------------------------------------------------------

# Build the test cases and save the result to the output file


def build(testData):
    """Build a file of data for testing.

    Parameters
    ----------
    testData : str
        The name of the file where test data will be stored.
    """
    # List to hold test cases
    L = []

    p = Path(__file__).resolve().parent/'datasources'
    with open(p/'samplelog.txt', 'r') as f:

        for line in f:
            zone = random.choice(ZONES)
            fmt = random.choice(FORMATS)
            L.append(makeDict(line, (zone, fmt)))

    # Edge cases ------------------------------------------------------------

    # Inject a malformed line. This should cause all object properties to be
    # set to None
    line = 'This is a malformed line'
    L.append(makeDict(line, (TZ.original, FMT.string)))

    # -----------------------------------------------------------------------

    # Empty line
    L.append(makeDict('', (TZ.original, FMT.string)))

    # -----------------------------------------------------------------------

    # Input that fails somewhere in the middle. In this case, intentionally
    # remove the spaces between ipaddress, userid and username.
    line = '175.156.126.209-- [31/Jan/2017:21:09:47 +0800] '
    line += '"GET / HTTP/1.1" 403 4897 "-" "Mozilla/5.0 (Windows NT 10.0; '
    line += 'WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"'
    L.append(makeDict(line, (TZ.original, FMT.string)))

    # -----------------------------------------------------------------------

    # Bad date/time field (33rd of January).
    line = '175.156.126.209 - - [33/Jan/2017:21:09:47 +0800] '
    line += '"GET / HTTP/1.1" 403 4897 "-" "Mozilla/5.0 (Windows NT 10.0; '
    line += 'WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"'
    L.append(makeDict(line, (TZ.utc, FMT.dateobj)))

    # -----------------------------------------------------------------------

    # Mix things up :-)
    random.shuffle(L)

    # Pickle the List
    fName = Path(__file__).resolve().parent/testData
    with lzma.open(fName, 'wb') as f:
        pickle.dump(L, f)

    # Restore the system path
    del sys.path[-1]

    return

# --------------------------------------------------------------------------


def main():
    """Initiate test data file creation."""
    build('data_parser201.bin')

    return

# --------------------------------------------------------------------------


if __name__ == '__main__':
    main()

# ========================================================================

# MIT License

# Copyright 2020-2022 Peter Nardi

# Terms of use for source code:

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
