[![PyPI version](https://badge.fury.io/py/fireeyepy.svg)](https://badge.fury.io/py/fireeyepy)
[![Python versions supported](https://img.shields.io/pypi/pyversions/fireeyepy.svg)](https://pypi.python.org/pypi/fireeyepy)

# FireEye Client Library for Python
This is the Python client library for all things FireEye API. Currently it only supports FireEye's Detection On Demand but will have support for other FireEye API's soon.

For more API information, visit the [FireEye Developer Hub](https://fireeye.dev)

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
To obtain a free trial API key, subscribe on the [AWS Marketplace](https://aws.amazon.com/marketplace/pp/B07XSMKK41)

### Upload A File
```python
response = detection.submit_file(file_name="myfile.txt", contents=open("path/to/myfile.txt", "rb"))
```
 By default, submit_file() will only send the first 32 MB (32,000,000 bytes) of a file, which is the API limit, but this can be configured by setting the "file_size_limit" option to any positive integer, where the unit is bytes.  While you can send more than 32 MB, the API will only use the first 32 MB itself, so this option will save network bandwidth.
```
# Send the first 10 MB of the file
result = detection.submit_file(file_name="myfile.txt", contents=open("path/to/myfile.txt", "rb"), file_size_limit=10000000)
```

### Retrieve File Report
```python
response = detection.get_report(report_id)
```
You may also provide the optional `extended=True` flag to get the full, in-depth report:
```python
response = detection.get_report(report_id, extended=True)
```

### Retrieve Presigned URL for Dashboard Report
```python
result = detection.get_presigned_url(report_id)
```

### Perform Hash Lookup
```python
response = detection.get_hash(hash)
```
