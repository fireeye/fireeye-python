# FireEye Client Library for Python
This is the Python client library for all things FireEye API. Currently it only supports FireEye's Detection On Demand but will have support for other FireEye API's soon.

Installation
------------

To install the Python client library:
```
git clone https://github.com/fireeye/fireeye-python.git
cd fireeye-python
pip install -r requirements.txt
python setup.py bdist_wheel
pip install -e .
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
    "file": ('maliciousfile.txt', open('./maliciousfile.txt', 'rb'))
  }
)
```

### Retrieve File Results
```python
response = detection.get_file_result(submission_id)
```

### Perform Hash Lookup
```python
response = detection.get_hash_lookup(hash)
```
