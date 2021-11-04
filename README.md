![GitHub](https://img.shields.io/github/license/geozeke/parser201)
![PyPI](https://img.shields.io/pypi/v/parser201)
![PyPI - Status](https://img.shields.io/pypi/status/parser201)
![GitHub last commit](https://img.shields.io/github/last-commit/geozeke/parser201)
![GitHub issues](https://img.shields.io/github/issues/geozeke/parser201)
[![Downloads](https://pepy.tech/badge/parser201)](https://pepy.tech/project/parser201)
![PyPI - Downloads](https://img.shields.io/pypi/dm/parser201)
![GitHub repo size](https://img.shields.io/github/repo-size/geozeke/parser201)
![Lines of code](https://img.shields.io/tokei/lines/github/geozeke/parser201)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/parser201)

## Features

The centerpiece of the parser201 module is the LogParser class. The class initializer takes a single line from an Apache log file and extracts the individual fields into properties within an object.

## Installation

```
pip3 install parser201
```

## Usage

The most common use-case for parser201 is importing individual lines from an Apache log file and creating LogParser objects, like this:

```python
from parser201 import LogParser

with open('access.log', 'r') as f:
    for line in f:
        lp = LogParser(line)
        # Use lp as desired: add to List, Dictionary, etc.
```


## Class Attributes

### Properties

Here's an example showing the properties of a LogParser class object:

```
  ipaddress: 81.48.51.130
     userid: -
   username: -
  timestamp: 24/Mar/2009:18:07:16 +0100
requestline: GET /images/puce.gif HTTP/1.1
 statuscode: 304
   datasize: 2454
    referer: -
  useragent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1;
```


* **datasize**

	The size of the response to the client (in bytes).

	*type: int*

* **ipaddress**

	The remote host (the client IP).

	*type: str*

* **referrer**

	The referrer header of the HTTP request (containing the URL of the page from which this request was initiated) if any is present, and `"-"` otherwise.

	*type: str*

* **requestline**

	The request line from the client. (e.g. `"GET / HTTP/1.0"`).

	*type: str*

* **statuscode**

	The status code sent from the server to the client (`200`, `404`, etc.).

	*type: int*

* **timestamp**

	The time of the request in the following format:

	`dd/MMM/YYYY:HH:MM:SS –hhmm`

	NOTE: `-hhmm` is the time offset from Greenwich Mean Time (GMT). Usually (but not always) `mm == 00`. Negative offsets (`-hhmm`) are west of Greenwich; positive offsets (`+hhmm`) are east of Greenwich. The date/time component has a guaranteed length of 28 characters (which includes the leading and training brackets). Every other component of a log entry is variable length.

	*type: str*

* **useragent**

	The browser identification string if any is present, and `"-"` otherwise.

	*type: str*

* **userid**

	The identity of the user determined by `identd` (not usually used since not reliable). If `identd` is not present, `userid == "-"`.

	*type: str*

* **username**

	The user name determined by HTTP authentication. If no username is present, `username == "-"`.

	*type: str*

---

### Methods

* **`__init__(line)`**

	LogParser class initializer. Returns an object with the properties set as described above.

	Parameters:

	* **line** (type *str*) – A single line from an Apache log file.


* **`__str()__`**

	Returns a string representation of a LogParser object. An example looks like this:

	
	```
	  ipaddress: 81.48.51.130
	     userid: -
	   username: -
	  timestamp: 24/Mar/2009:18:07:16 +0100
	requestline: GET /images/puce.gif HTTP/1.1
	 statuscode: 304
	   datasize: 2454
	    referer: -
	  useragent: Mozilla/4.0 (compatible; MSIE 7.0;
	             Windows NT 5.1;
	```

---

### Exception Handling

If a line from an Apache log file cannot be parsed by the class initializer (is corrupted for some reason) the initializer returns an object with all the properties set to `None`.

```
  ipaddress: None
     userid: None
   username: None
  timestamp: None
requestline: None
 statuscode: None
   datasize: None
    referer: None
  useragent: None
```

---

## Version History

* 1.0.0 (2021-11-04)
	* Stable production release.
	* Migrated to a new development framework.
	* Implemented more robust and compartmentalized test cases.
	* Code tuning.<br><br>
* 0.2.0 (2021-10-31)
	* Changed behavior to gracefully fail for any malformed input line. If an input line cannot be successfully parsed, all properties of the returned object are set to `None` and no messages are printed.
	* Added additional pytest cases to verify failure behavior.<br><br>
* 0.1.9 (2021-09-15)
	* Code cleanup for pep8 compliance.
	* Cleaned up Makefiles and scripts to remove references to python (meaning python2) and replace it with python3.<br><br>
* 0.1.8 (2021-09-15)
	* Internal build.<br><br>
* 0.1.7 (2021-06-05)
	* Re-tooled testing scripts to use parameterized test data, and conduct more robust testing.<br><br>
* 0.1.6 (2020-12-19)
	* Addressed exception handling for initializer input not being a valid string data type.
	* Documentation cleanup.<br><br>
* 0.1.5 (2020-10-26)
	* Enabled automatic deployment of tagged releases to pypi from travis using encrypted token.
	* Converted references to the master branch in the git repository to main across the documentation set.
	* Documentation cleanup.<br><br>
* 0.1.4 (2020-10-24)
	* Initial pypi release.
	* Fixed test file filtering issue in .gitignore.
	* Dependency fix for travis tests.<br><br>
* 0.1.1 (2020-10-22)
	* Follow-on testing on test.pypi.org.<br><br>
* 0.1.0 (2020-10-18)
	* Initial testing on test.pypi.org.