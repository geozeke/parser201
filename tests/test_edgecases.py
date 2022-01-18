#!/usr/bin/env python3

# --------------------------------------------------------------------------

import pathprep  # noqa

from classes import LogParser  # isort: skip


def test_nonStrInput():
    lp = LogParser(42)
    testResult = lp.ipaddress
    benchmark = None
    assert testResult == benchmark


def test_mangledField():
    lp = LogParser(42)
    testResult = lp.ipaddress
    benchmark = None
    assert testResult == benchmark


def test_assignIPaddress():
    lp = LogParser(42)
    lp.ipaddress = '192.168.1.1'
    assert lp.ipaddress == '192.168.1.1'


def test_assignUserid():
    lp = LogParser(42)
    lp.userid = 'user@test.com'
    assert lp.userid == 'user@test.com'


def test_assignUsername():
    lp = LogParser(42)
    lp.username = 'StarLord'
    assert lp.username == 'StarLord'


def test_assignTimestamp():
    lp = LogParser(42)
    lp.timestamp = '24/Mar/2009:18:07:16 +0100'
    assert lp.timestamp == '24/Mar/2009:18:07:16 +0100'


def test_assignRequestline():
    lp = LogParser(42)
    lp.requestline = 'GET /images/puce.gif HTTP/1.1'
    assert lp.requestline == 'GET /images/puce.gif HTTP/1.1'


def test_assignStatuscode():
    lp = LogParser(42)
    lp.statuscode = 42
    assert lp.statuscode == 42


def test_assignDatasize():
    lp = LogParser(42)
    lp.datasize = 42
    assert lp.datasize == 42


def test_assignReferrer():
    lp = LogParser(42)
    lp.referrer = '-'
    assert lp.referrer == '-'


def test_assignUseragent():
    lp = LogParser(42)
    lp.useragent = 'Mozilla/4.0'
    assert lp.useragent == 'Mozilla/4.0'
