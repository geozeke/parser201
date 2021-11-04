#!/usr/bin/env python3

# Author: Peter Nardi
# Date: 11/03/21
# License: (see MIT License at the end of this file)

# Title: Test data generator for parser201

# Imports

import lzma
import pickle
import random
import string
import sys
from pathlib import Path

# Adjust path before importing local modules
sources = '/src/parser201/'
P = str(Path(__file__).resolve().parent.parent) + sources
sys.path.append(P)

try:
    from classes import LogParser
except Exception as e:
    print(e)
    sys.exit(1)

# --------------------------------------------------------------------------
# Helper function to create data dictionaries


def makeDict(dataIn):

    D = {}

    D['linein'] = dataIn[0]
    D['ipaddress'] = dataIn[1]
    D['userid'] = dataIn[2]
    D['username'] = dataIn[3]
    D['timestamp'] = dataIn[4]
    D['requestline'] = dataIn[5]
    D['statuscode'] = dataIn[6]
    D['datasize'] = dataIn[7]
    D['referrer'] = dataIn[8]
    D['useragent'] = dataIn[9]
    D['str'] = dataIn[10]

    return D

# --------------------------------------------------------------------------

# Build the test cases and save the result to the output file


def build(testData):

    # List to hold test cases
    L = []

    P = str(Path(__file__).resolve().parent) + '/datasources/'
    with open(P + 'benchmarkdata.txt', 'r') as f:

        for line in f:

            # Add a str representation of the object to the end of the list.
            if line.split() != '':
                parts = line.strip().split('FIELDBREAK')
                parts.append(str(LogParser(parts[0])))
                L.append(makeDict(parts))

    # Edge cases ------------------------------------------------------------

    # Inject a malformed line. This should cause all object properties to be
    # set to None
    parts = ['This is a malformed line']
    parts += [None] * 10
    L.append(makeDict(parts))

    # -----------------------------------------------------------------------

    # Empty line
    parts = ['']
    parts += [None] * 10
    L.append(makeDict(parts))

    # -----------------------------------------------------------------------

    # Input that fails somewhere in the middle. In this case, intentionally
    # remove the spaces between ipaddress, userid and username.
    line = '175.156.126.209-- [31/Jan/2017:21:09:47 +0800] '
    line += '"GET / HTTP/1.1" 403 4897 "-" "Mozilla/5.0 (Windows NT 10.0; '
    line += 'WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"'
    parts = [line]
    parts += [None] * 10
    L.append(makeDict(parts))

    # -----------------------------------------------------------------------

    # Mix things up :-)
    random.shuffle(L)

    # Pickle the List
    fName = str(Path(__file__).resolve().parent) + '/' + testData
    with lzma.open(fName, 'wb') as f:
        pickle.dump(L, f)

    # Restore the system path
    del sys.path[-1]

    return

# --------------------------------------------------------------------------


def main():

    build('data_parser201.bin')

    return

# --------------------------------------------------------------------------


if __name__ == '__main__':
    main()

# ========================================================================

# MIT License

# Copyright 2020-2021 Peter Nardi

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
