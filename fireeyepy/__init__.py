# Copyright (C) 2019 FireEye, Inc. All Rights Reserved.
from platform import python_version
from .errors import *
import os
import requests
import logging

__version__ = "1.0.2"
logger = logging.getLogger("fireeye")

class Detection:
  """The Detection class allows your app to communicate with FireEye's Detection On Demand service.add()
  
  The Detection On Demand service provides the ability for you to submit files and md5sum hashes for malware analysis.add()

  This client handles constructing and sending HTTP requests to Detection On Demand as well as parsing any responses received.


  Keyword Arguments:
      key {string} -- The API key provided to you by the Detection On Demand service.


  Example of sending a file in for malware analysis.
  ```python
  import fireeyepy

  detection = fireeyepy.Detection(key="yourapikeyhere")

  result = detection.submit_file(file_name="myfile.txt", contents=open("path/to/myfile.txt", "rb"))
  ```

  By default, submit_file() will only send the first 32 MB (32,000,000 bytes) of a file, which is the API limit, but this can be configured by setting the "file_size_limit" option to any positive integer, where the unit is bytes.  While you can send more than 32 MB, the API will only use the first 32 MB itself, so this option will save network bandwidth.
  ```
  # Send the first 10 MB of the file
  result = detection.submit_file(file_name="myfile.txt", contents=open("path/to/myfile.txt", "rb"), file_size_limit=10000000)
  ```
  ------------------------------

  Example of getting a file result from a previous analysis
  ```python
  import fireeyepy

  detection = fireeyepy.Detection(key="yourapikeyhere")

  result = detection.get_report("report_id")
  ```
  ------------------------------

  Example of getting a presigned URL for a browser viewable report
  ```python
  import fireeyepy

  detection = fireeyepy.Detection(key="yourapikeyhere")

  result = detection.get_presigned_url("report_id")
  ```
  ------------------------------

  Example of getting the results of a hash that was previously analyzed.
  ```python
  import fireeyepy

  detection = fireeyepy.Detection(key="yourapikeyhere")

  result = detection.get_hash_lookup(hash="md5sumhashhere")
  ```
  """
  def __init__(self,key=None):
    self.api_key = key or os.environ.get("FIREEYE_API_KEY", None)
    self.api_host = "feapi.marketplace.apps.fireeye.com"
    user_agent = "fireeye-python/{version} python/{python_version}".format(
      version=__version__, python_version=python_version()
    )
    self.headers = {"User-Agent": user_agent, "feye-auth-key": key}
    self.session = requests.Session()
  
  def submit_file(self, file_name, contents, file_size_limit=32000000):
    """Allows you to submit a binary file object for malware analysis.
    
    Keyword Arguments:
        file_name {string} -- The name of the file
        contents {io.BufferedIOBase} -- The contents of the file in binary
        file_size_limit {integer} -- The number of bytes to send to the detection service from the beginning of the file.  Files that are smaller than the limit will be sent in their entirety.  Files that are larger than this limit will only have the first 'n' bytes sent.  Default is 32 MB (32,000,000 bytes).
    
    Returns:
        dict -- Returns a dict of the http response.
    """
    contents.seek(0) # Make sure the file handler is at byte 0 so we can read the next 'n' bytes
    files = {
      "file": (file_name, contents.read(file_size_limit))
    }

    return self.post(self.api_host, "/files", None, files)

  def get_report(self, report_id, extended=False):
    """Allows you to get the report details for a file or hash submission.
    
    Returns:
        dict -- Returns the report details
    """
    return self.get(self.api_host, "/reports/{}".format(report_id), {"extended": extended})

  def get_presigned_url(self, report_id, expiry=72):
    """Allows you to get a presigned URL for a browser viewable version of the analysis report
    
    Returns:
        dict -- Returns the presigned URL details
    """
    return self.get(self.api_host, "/presigned-url/{}".format(report_id), {"expiry": expiry})

  def get_hash(self, hash):
    """Allows you to get the malware analysis results for a given hash.
    
    Arguments:
        hash {string} -- The md5sum of the file you would like to check.
    
    Returns:
        dict -- Returns a dict of the http response.
    """
    return self.get(self.api_host, "/hashes/{}".format(hash))

  def get(self, host, request_uri, params=None):
    uri = "https://{host}{request_uri}".format(host=host, request_uri=request_uri)
    headers = self.headers

    logger.debug("GET to %r with params %r, headers %r", uri, params, headers)
    return self.parse(host, self.session.get(uri, params=params, headers=headers))

  def post(self, host, request_uri, data=None, files=None):
    uri = "https://{host}{request_uri}".format(host=host, request_uri=request_uri)
    headers = self.headers

    logger.debug("POST to %r with data %r, files %r, headers %r", uri, data, files, headers)
    return self.parse(host, self.session.post(uri, data=data, files=files, headers=headers))

  def parse(self, host, response):
    logger.debug("Response headers %r", response.headers)
    if response.status_code == 401:
      raise AuthenticationError
    elif response.status_code == 204:
      return None
    elif 200 <= response.status_code < 300:
      content_mime = response.headers.get("content-type").split(";", 1)[0]
      if content_mime == "application/json":
          return response.json()
      else:
          return response.content
    elif 400 <= response.status_code < 500:
      logger.warning(
          "Client error: %s %r", response.status_code, response.content
      )
      message = "{code} response from {host}".format(
          code=response.status_code, host=host
      )
      raise ClientError(message)
    elif 500 <= response.status_code < 600:
      logger.warning(
          "Server error: %s %r", response.status_code, response.content
      )
      message = "{code} response from {host}".format(
          code=response.status_code, host=host
      )
      raise ServerError(message)