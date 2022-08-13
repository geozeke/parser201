#!/usr/bin/env python3
"""Test LogParser edge cases."""

from parser201.classes import LogParser


def test_non_str():
    """Test inputs that are non-strings."""
    lp = LogParser(42)
    test_result = lp.ipaddress
    benchmark = None
    assert test_result == benchmark


def test_mangled_field():
    """Test malformed input."""
    lp = LogParser(42)
    test_result = lp.ipaddress
    benchmark = None
    assert test_result == benchmark


def test_assign_ip():
    """Test assignment of an ipaddress."""
    lp = LogParser(42)
    lp.ipaddress = '192.168.1.1'
    assert lp.ipaddress == '192.168.1.1'


def test_assign_uid():
    """Test assignment of a userid."""
    lp = LogParser(42)
    lp.userid = 'user@test.com'
    assert lp.userid == 'user@test.com'


def test_assign_uname():
    """Test assignment of a username."""
    lp = LogParser(42)
    lp.username = 'StarLord'
    assert lp.username == 'StarLord'


def test_assign_tstamp():
    """Test assignment of a timestamp."""
    lp = LogParser(42)
    lp.timestamp = '24/Mar/2009:18:07:16 +0100'
    assert lp.timestamp == '24/Mar/2009:18:07:16 +0100'


def test_assign_req_line():
    """Test assignment of a request line."""
    lp = LogParser(42)
    lp.requestline = 'GET /images/puce.gif HTTP/1.1'
    assert lp.requestline == 'GET /images/puce.gif HTTP/1.1'


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
    lp.referrer = '-'
    assert lp.referrer == '-'


def test_assign_uagent():
    """Test assignment of a useragent."""
    lp = LogParser(42)
    lp.useragent = 'Mozilla/4.0'
    assert lp.useragent == 'Mozilla/4.0'
