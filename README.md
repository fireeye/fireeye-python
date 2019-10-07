[![PyPI version](https://badge.fury.io/py/fireeyepy.svg)](https://badge.fury.io/py/fireeyepy)

# FireEye Client Library for Python
This is the Python client library for all things FireEye API. Currently it only supports FireEye's Detection On Demand but will have support for other FireEye API's soon.

Installation
------------

To install the Python client library:
```
pip install fireeyepy
```

To upgrade your installed library:
```
pip install fireeyepy --upgrade
```

Alternatively, you can clone the repository via the command line:
```
git clone https://github.com/fireeye/fireeye-python.git
```

Usage
-----
Begin by importing the 'fireeye' module:
```python
import fireeyepy
```

## Detection On Demand
Construct a Detection object with your api key:
```python
detection = fireeyepy.Detection(key=api_key)
```
### Upload A File
```python
response = detection.submit_file(
  files={
    "file": ('filename', open('./path/to/filename', 'r'))
  }
)
```

### Retrieve File Report
```python
response = detection.get_report(report_id)
```
You may also provide the optional `extended=True` flag to get the full, in-depth report:
```python
response = detection.get_report(report_id, extended=True)
```

### Perform Hash Lookup
```python
response = detection.get_hash(hash)
```
