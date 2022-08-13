#!/usr/bin/env python3
"""Test LogParser __eq__ method."""

from parser201.classes import LogParser


def test_eq_true():
    """Test that two LogParser objects are equal."""
    line = '175.156.126.209 - - [31/Jan/2017:22:36:45 +0800] "GET /assets/css/'
    line += 'new/prettyPhoto.css?cache_breaker=1.0.27012017 HTTP/1.1" 200 '
    line += '27463 "http://gobudgetair.com/index.php" "Mozilla/5.0 (iPhone; '
    line += 'CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, '
    line += 'like Gecko) Version/10.0 Mobile/14D27 Safari/602.1"'
    lp1 = LogParser(line)
    lp2 = LogParser(line)
    assert lp1 == lp2


def test_eq_false():
    """Test that two LogParser objects are not equal."""
    line1 = '175.156.126.209 - - [31/Jan/2017:22:36:45 +0800] "GET '
    line1 += '/assets/css/new/prettyPhoto.css?cache_breaker=1.0.27012017 HTTP/'
    line1 += '1.1" 200 27463 "http://gobudgetair.com/index.php" "Mozilla/5.0 '
    line1 += '(iPhone; CPU iPhone OS 10_2_1 like Mac OS X) '
    line1 += 'AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 Mobile/'
    line1 += '14D27 Safari/602.1"'

    # Tweak the timestamp (22:36:45 to 22:36:46) to get a difference.
    line2 = '175.156.126.209 - - [31/Jan/2017:22:36:46 +0800] "GET '
    line2 += '/assets/css/new/prettyPhoto.css?cache_breaker=1.0.27012017 HTTP/'
    line2 += '1.1" 200 27463 "http://gobudgetair.com/index.php" "Mozilla/5.0 '
    line2 += '(iPhone; CPU iPhone OS 10_2_1 like Mac OS X) '
    line2 += 'AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 Mobile/'
    line2 += '14D27 Safari/602.1"'

    lp1 = LogParser(line1)
    lp2 = LogParser(line2)
    assert lp1 != lp2


def test_diff_type_false():
    """Compare a LogParser object to an objet of a different type."""
    line1 = '175.156.126.209 - - [31/Jan/2017:22:36:45 +0800] "GET '
    line1 += '/assets/css/new/prettyPhoto.css?cache_breaker=1.0.27012017 HTTP/'
    line1 += '1.1" 200 27463 "http://gobudgetair.com/index.php" "Mozilla/5.0 '
    line1 += '(iPhone; CPU iPhone OS 10_2_1 like Mac OS X) '
    line1 += 'AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 Mobile/'
    line1 += '14D27 Safari/602.1"'

    lp1 = LogParser(line1)
    assert lp1 != "hello world"
