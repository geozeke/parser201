![GitHub](https://img.shields.io/github/license/geozeke/parser201)
![PyPI](https://img.shields.io/pypi/v/parser201)
![PyPI - Status](https://img.shields.io/pypi/status/parser201)
![GitHub last commit](https://img.shields.io/github/last-commit/geozeke/parser201)
![GitHub issues](https://img.shields.io/github/issues/geozeke/parser201)
![PyPI - Downloads](https://img.shields.io/pypi/dm/parser201)
![GitHub repo size](https://img.shields.io/github/repo-size/geozeke/parser201)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/parser201)

<br>

<img
src="https://lh3.googleusercontent.com/d/1H04KVAA3ohH_dLXIrC0bXuJXDn3VutKc"
alt="Dinobox Logo" width="120"/>

## Features

The centerpiece of the parser201 module is the LogParser class. The
class initializer takes a single line from an Apache access log file and
extracts the individual fields into attributes within an object.

## Installation

```text
pip3 install parser201
```

## Usage

The most common use-case for parser201 is importing individual lines
from an Apache access log file and creating LogParser objects, like
this:

```python
from parser201 import LogParser

with open('access.log', 'r') as f:
    for line in f:
        lp = LogParser(line)
        # Use lp as desired: add to List, Dictionary, etc.
```

## Documentation

See: [parser201 Documentation][def].

## Version History

* 1.5.2 (2024-09-23)
  * Migrated packaging and build system to [uv][def2], and code
    formatting and linting to [ruff][def3].
  * Improved exception handling for invalid date-time objects.
  * Migrated documentation generation to [pdoc][def7].
  * Code and documentation linting.<br><br>
* 1.5.0 (2024-01-27)
  * Cleaned up packaging for better [PEP561][def4] compliance.
  * Cleaned up type hints.
  * Dropped support for converting timestamps to local machine time.
    Processing local timezones across multiple architectures and
    operating systems is a bit of a hot mess in Python right now.
    There's just too much variability with regard to OS Settings,
    location, daylight savings time, etc. The performance of this
    feature was spotty at best. There is still support for the
    *original* timezone and converstion to [*UTC*][def5].<br><br>
* 1.4.1 (2023-06-22)
  * Migrated code formatter to *black*.<br><br>
* 1.4.0 (2023-04-30)
  * Strengthened regular expression parsing to handle log lines that
    contain a wider array of malicious attacks.
  * Added support for access logs that contain both IPv4 and IPv6
    addresses.
  * Minimum supported Python version is now 3.8 (^3.8).
  * Miscellaneous optimizations.<br><br>
* 1.3.1 (2022-10-22)
  * Migrated dependency/build management to [poetry][def6].<br><br>
* 1.3.0 (2022-08-13)
  * Implemented `__eq__` magic method for the `LogParser` class. You can
    now perform equality checks on two `LogParser` objects.
  * Added test cases for `__eq__`
  * Migrated task runner to `make`
  * Documentation cleanup
  * Code linting and cleanup<br><br>
* 1.2.0 (2022-07-17)
  * Implemented `__eq__` magic methods in the `FMT` and `TZ` classes.
  * Documentation cleanup.
  * Testing improvements and pyproject.toml adjustments for better
    pytest compatability.
  * Code linting and cleanup.<br><br>
* 1.1.5 (2022-01-17)
  * Code linting and cleanup.<br><br>
* 1.1.4 (2021-12-23)
  * Documentation cleanup.<br><br>
* 1.1.3 (2021-12-19)
  * Make file tuning.
  * Documentation cleanup.
  * Added site logo to README.md.<br><br>
* 1.1.0 (2021-11-13)
  * Implemented selectable timestamp conversion options {*original*,
    *local*,
    [*UTC*][def5]}.
  * Implemented selectable formatting options for timestamp attribute
    {*string*, *date_obj*}.
  * Migrated API reference to GitHub pages.
  * Code cleanup.<br><br>
* 1.0.2 (2021-11-05)
  * Documentation cleanup.<br><br>
* 1.0.0 (2021-11-04)
  * Stable production release.
  * Migrated to a new development framework.
  * Implemented more robust and compartmentalized test cases.
  * Code tuning.<br><br>
* 0.2.0 (2021-10-31)
  * Changed behavior to gracefully fail for any malformed input line. If
    an input line cannot be successfully parsed, all attributes of the
    returned object are set to `None` and no messages are printed.
  * Added additional pytest cases to verify failure behavior.<br><br>
* 0.1.9 (2021-09-15)
  * Code cleanup for pep8 compliance.
  * Cleaned up Makefiles and scripts to remove references to python
    (meaning python2) and replace it with python3.<br><br>
* 0.1.7 (2021-06-05)
  * Re-tooled testing scripts to use parameterized test data, and
    conduct more robust testing.<br><br>
* 0.1.6 (2020-12-19)
  * Addressed exception handling for initializer input not being a valid
    string data type.
  * Documentation cleanup.<br><br>
* 0.1.5 (2020-10-26)
  * Enabled automatic deployment of tagged releases to pypi from travis
    using encrypted token.
  * Converted references to the master branch in the git repository to
    main across the documentation set.
  * Documentation cleanup.<br><br>
* 0.1.4 (2020-10-24)
  * Initial pypi release.
  * Fixed test file filtering issue in .gitignore.
  * Dependency fix for travis tests.<br><br>
* 0.1.1 (2020-10-22)
  * Follow-on testing on test.pypi.org.<br><br>
* 0.1.0 (2020-10-18)
  * Initial testing on test.pypi.org.

[def]: https://geozeke.github.io/parser201
[def2]: https://docs.astral.sh/uv/
[def3]: https://docs.astral.sh/ruff/
[def4]: https://peps.python.org/pep-0561/
[def5]: https://en.wikipedia.org/wiki/Coordinated_Universal_Time
[def6]: https://python-poetry.org/
[def7]: https://github.com/mitmproxy/pdoc
