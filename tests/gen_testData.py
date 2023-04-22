#!/usr/bin/env python3
"""Generate data for testing."""

import lzma
import pickle
import random
import sys
from pathlib import Path
from time import timezone

p = Path(__file__).resolve().parents
sys.path.append(f'{p[1]}/src/parser201')
TESTDATA = p[0]/'data_parser201.bin'

from classes import FMT  # type: ignore # noqa
from classes import TZ  # type: ignore # noqa
from classes import LogParser  # type: ignore # noqa

ZONES = tuple(TZ)
FORMATS = tuple(FMT)


def make_dict(data_in, options):
    """Make a dictionary from test data.

    This function takes some generated test data, and stores it in a
    dictionary for later pickling into a file. This pickled file will be
    used for testing.

    Parameters
    ----------
    data_in : str
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

    # lp = LogParser(data_in)
    lp = LogParser(data_in, timezone=options[0], dts_format=options[1])

    D['linein'] = data_in
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
    D['dts_format'] = options[1]

    return D


def build():
    """Build a file of data for testing.

    Parameters
    ----------
    testData : str
        The name of the file where test data will be stored. Note: the
        sample log file includes several lines with various injection
        attacks. This stresses the class initializer to handle a more
        roboust set of use cases.
    """
    # List to hold test cases
    L = []

    p = Path(__file__).resolve().parent/'datasources'
    with open(p/'samplelog.txt', 'r') as f:

        for line in f:
            zone = random.choice(ZONES)
            dts_format = random.choice(FORMATS)
            L.append(make_dict(line, (zone, dts_format)))

    # Edge cases ------------------------------------------------------------

    # Inject a malformed line. This should cause all object properties to be
    # set to None
    line = 'This is a malformed line'
    L.append(make_dict(line, (TZ.original, FMT.string)))

    # -----------------------------------------------------------------------

    # Empty line
    L.append(make_dict('', (TZ.original, FMT.string)))

    # -----------------------------------------------------------------------

    # Input that fails somewhere in the middle. In this case, intentionally
    # remove the spaces between ipaddress, userid and username.
    line = '175.156.126.209-- [31/Jan/2017:21:09:47 +0800] '
    line += '"GET / HTTP/1.1" 403 4897 "-" "Mozilla/5.0 (Windows NT 10.0; '
    line += 'WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"'
    L.append(make_dict(line, (TZ.original, FMT.string)))

    # -----------------------------------------------------------------------

    # Bad date/time field (33rd of January).
    line = '175.156.126.209 - - [33/Jan/2017:21:09:47 +0800] '
    line += '"GET / HTTP/1.1" 403 4897 "-" "Mozilla/5.0 (Windows NT 10.0; '
    line += 'WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"'
    L.append(make_dict(line, (TZ.utc, FMT.date_obj)))

    # -----------------------------------------------------------------------

    # Mix things up :-)
    random.shuffle(L)

    # Pickle the List
    with lzma.open(TESTDATA, 'wb') as f:
        pickle.dump(L, f)

    # Restore the system path
    del sys.path[-1]

    return


def main():  # noqa
    build()
    return


if __name__ == '__main__':
    main()
