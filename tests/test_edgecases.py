#!/usr/bin/env python3
"""Test LogParser edge cases."""

from parser201.classes import LogParser


def test_nonStrInput():
    """Test inputs that are non-strings."""
    lp = LogParser(42)
    testResult = lp.ipaddress
    benchmark = None
    assert testResult == benchmark


def test_mangledField():
    """Test malformed input."""
    lp = LogParser(42)
    testResult = lp.ipaddress
    benchmark = None
    assert testResult == benchmark


def test_assignIPaddress():
    """Test assignment of an ipaddress."""
    lp = LogParser(42)
    lp.ipaddress = '192.168.1.1'
    assert lp.ipaddress == '192.168.1.1'


def test_assignUserid():
    """Test assignment of a userid."""
    lp = LogParser(42)
    lp.userid = 'user@test.com'
    assert lp.userid == 'user@test.com'


def test_assignUsername():
    """Test assignment of a username."""
    lp = LogParser(42)
    lp.username = 'StarLord'
    assert lp.username == 'StarLord'


def test_assignTimestamp():
    """Test assignment of a timestamp."""
    lp = LogParser(42)
    lp.timestamp = '24/Mar/2009:18:07:16 +0100'
    assert lp.timestamp == '24/Mar/2009:18:07:16 +0100'


def test_assignRequestline():
    """Test assignment of a request line."""
    lp = LogParser(42)
    lp.requestline = 'GET /images/puce.gif HTTP/1.1'
    assert lp.requestline == 'GET /images/puce.gif HTTP/1.1'


def test_assignStatuscode():
    """Test assignment of a status code."""
    lp = LogParser(42)
    lp.statuscode = 42
    assert lp.statuscode == 42


def test_assignDatasize():
    """Test assignment of a datasize field."""
    lp = LogParser(42)
    lp.datasize = 42
    assert lp.datasize == 42


def test_assignReferrer():
    """Test assignment of a referrer."""
    lp = LogParser(42)
    lp.referrer = '-'
    assert lp.referrer == '-'


def test_assignUseragent():
    """Test assignment of a useragent."""
    lp = LogParser(42)
    lp.useragent = 'Mozilla/4.0'
    assert lp.useragent == 'Mozilla/4.0'
