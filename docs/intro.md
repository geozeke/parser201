The parser201 module takes a single line from an Apache access log file and
extracts the individual fields into attributes within an object. parser201 is
robust, and is able to handle Apache Access Log lines containing malicious
code attacks like: Mambo, PHPBB, SQL Injection, etc.

## Installation

parser201 is lightweight, with no third party dependencies.

```text
pip3 install parser201
```

## Usage Example

```python
from parser201 import LogParser

with open('access.log', 'r') as f:
    for line in f:
        lp = LogParser(line)
        # Use lp as desired: add to List, Dictionary, etc.
```

## API Documentation

Detailed API information is available by clicking on the `parser201.classes` link.

**TL/DR**: Here's an example showing the attributes of a LogParser class object:

```text
  ipaddress: 81.48.51.130
     userid: -
   username: -
  timestamp: 24/Mar/2009:18:07:16 +0100
requestline: GET /images/puce.gif HTTP/1.1
 statuscode: 304
   datasize: 2454
   referrer: -
  useragent: Mozilla/4.0 compatible; MSIE 7.0; Windows NT 5.1;
```

## Exception Handling

If a line from an Apache access log file cannot be parsed by the class initializer (is corrupted for some reason) the initializer returns an object with all the attributes set to `None`.

```text
  ipaddress: None
     userid: None
   username: None
  timestamp: None
requestline: None
 statuscode: None
   datasize: None
   referrer: None
  useragent: None
```
