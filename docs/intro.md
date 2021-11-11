## Documentation

### Installation

parser201 is lightweight, with no third party dependencies. 

```
pip3 install parser201
```

### Usage Example

```python
from parser201 import LogParser, FMT, TZ

with open('access.log', 'r') as f:
    for line in f:
        lp = LogParser(line)
        # Use lp as desired: add to List, Dictionary, etc.
```

### LogParser Attributes
Detailed attribute information is available by clicking on the `parser201.classes` link. Here's an example showing the attributes of a LogParser class object:

```
  ipaddress: 81.48.51.130
     userid: -
   username: -
  timestamp: 24/Mar/2009:18:07:16 +0100
requestline: GET /images/puce.gif HTTP/1.1
 statuscode: 304
   datasize: 2454
    referer: -
  useragent: Mozilla/4.0 compatible; MSIE 7.0; Windows NT 5.1;
```

### Exception Handling

If a line from an Apache access log file cannot be parsed by the class initializer (is corrupted for some reason) the initializer returns an object with all the properties set to `None`.

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


