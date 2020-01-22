[![PyPI version](https://badge.fury.io/py/fireeyepy.svg)](https://badge.fury.io/py/fireeyepy)
[![Python versions supported](https://img.shields.io/pypi/pyversions/fireeyepy.svg)](https://pypi.python.org/pypi/fireeyepy)

# FireEye Client Library for Python
This is the Python client library for all things FireEye API.  The current list of supported APIs and endpoints is limited but growing every day.

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
Begin by importing one or more modules from the fireeyepy package:
```python
from fireeyepy import *
```

## Detection On Demand
Construct a Detection object with your api key:
```python
detection = detection_on_demand.Detection(key=api_key)
```
### Upload A File
```python
response = detection.submit_file(
  files={
    "file": ('filename', open('./path/to/filename', 'rb'))
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

## Helix
Construct a Helix object with your api key and helix instance id, and optionally your Helix instance hostname:
```python
h = helix.Helix('api key', 'hexaaa999', host='apps.fireeye.com')
```

### Get a list of alerts
Get a list of alerts in your Helix instance.  The function arguments will accept named parameters for any query parameters supported by the endpoint.
```python
alerts = h.get_alerts(limit=3)
```
