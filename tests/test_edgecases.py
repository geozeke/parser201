#!/usr/bin/env python3
"""Test LogParser edge cases."""

from parser201.classes import LogParser


def test_non_str():
    """Test inputs that are non-strings."""
    lp = LogParser(42)
    test_result = lp.ipaddress
    benchmark = None
    assert test_result == benchmark


def test_mangled_field1():
    """Test malformed input.

    Checks to see if a line containing mangled input can be recognized.
    In this case, I removed the space between userid and user name, so
    it becomes '--' instead of '- -'
    """
    logline = '198.0.200.105 -- [14/Jan/2014:09:36:50 -0800] "GET /svds.com/ '
    logline += 'rockandroll HTTP/1.1" 301 241 "-" "Mozilla/5.0 (Macintosh; '
    logline += "Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) "
    logline += 'Chrome/ 31.0.1650.63 Safari/537.36"'
    lp = LogParser(logline)
    test_result = lp.ipaddress
    benchmark = None
    assert test_result == benchmark


def test_mangled_field2():
    """Test malformed input.

    Checks to see if a line containing mangled input can be recognized.
    In this case, I removed a quote mark from the beginning of the
    request line.
    """
    logline = "198.0.200.105 -- [14/Jan/2014:09:36:50 -0800] GET /svds.com/ "
    logline += 'rockandroll HTTP/1.1" 301 241 "-" "Mozilla/5.0 (Macintosh; '
    logline += "Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) "
    logline += 'Chrome/ 31.0.1650.63 Safari/537.36"'
    lp = LogParser(logline)
    test_result = lp.ipaddress
    benchmark = None
    assert test_result == benchmark


def test_assign_ip():
    """Test assignment of an ipaddress."""
    lp = LogParser(42)
    lp.ipaddress = "192.168.1.1"
    assert lp.ipaddress == "192.168.1.1"


def test_assign_uid():
    """Test assignment of a userid."""
    lp = LogParser(42)
    lp.userid = "user@test.com"
    assert lp.userid == "user@test.com"


def test_assign_uname():
    """Test assignment of a username."""
    lp = LogParser(42)
    lp.username = "StarLord"
    assert lp.username == "StarLord"


def test_assign_tstamp():
    """Test assignment of a timestamp."""
    lp = LogParser(42)
    lp.timestamp = "24/Mar/2009:18:07:16 +0100"
    assert lp.timestamp == "24/Mar/2009:18:07:16 +0100"


def test_assign_req_line():
    """Test assignment of a request line."""
    lp = LogParser(42)
    lp.requestline = "GET /images/puce.gif HTTP/1.1"
    assert lp.requestline == "GET /images/puce.gif HTTP/1.1"


def test_assign_stat_code():
    """Test assignment of a status code."""
    lp = LogParser(42)
    lp.statuscode = 42
    assert lp.statuscode == 42


def test_assign_data_size():
    """Test assignment of a datasize field."""
    lp = LogParser(42)
    lp.datasize = 42
    assert lp.datasize == 42


def test_assign_referrer():
    """Test assignment of a referrer."""
    lp = LogParser(42)
    lp.referrer = "-"
    assert lp.referrer == "-"


def test_assign_uagent():
    """Test assignment of a useragent."""
    lp = LogParser(42)
    lp.useragent = "Mozilla/4.0"
    assert lp.useragent == "Mozilla/4.0"


def test_property_quantity():
    """Check the number of properties.

    This test ensures that the length of the list of labels matches the
    number of properties in a LogParser object. This is just a sanity
    check if I start adding or deleting properties in the class.
    """
    lp = LogParser("dummy")
    assert len(vars(lp)) == len(LogParser._labels)
