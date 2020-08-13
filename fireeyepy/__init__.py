# Copyright (C) 2019 FireEye, Inc. All Rights Reserved.
from platform import python_version
from .errors import *
import os
import requests
import logging

__version__ = "1.2.4"
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

  result = detection.submit_file(
    files={
      "file": ('filename', open('./path/to/filename', 'rb'))
    }
  )
  ```

  Optionally, you can send body parameters:
  ```python
  result = detection.submit_file(
    body={
      "file_name": "different_name.txt",
      "screenshot": true
    },
    files={
      "file": ('filename', open('./path/to/filename', 'rb'))
    }
  )
  ```

  ------------------------------

  Example of sending one or more URLs for malware analysis.
  ```python
  import fireeyepy

  detection = fireeyepy.Detection(key="yourapikeyhere")

  result = detection.submit_urls(["url1","url2",...])
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
  ------------------------------

  Example of getting an artifact from a report.

  ```python
  import fireeyepy

  detection = fireeyepy.Detection(key="yourapikeyhere")

  result = detection.get_artifact(report_id="8d0aa90b-8bf3-4483-ae3b-0ded00d157ab", artifact_type="screenshot")
  ```

  ------------------------------

  Example of getting the health of the service.

  ```python
  import fireeyepy

  detection = fireeyepy.Detection(key="yourapikeyhere")

  health = detection.get_health()
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
  
  def submit_file(self, body=None, files=None):
    """Allows you to submit a file object for malware analysis.
    
    Keyword Arguments:
        body {dict} -- The body of your http request. This is optional. (default: {None})
        files {io.TextIOWrapper} -- The file you will be submitting for analysis. (default: {None})
    
    Returns:
        dict -- Returns a dict of the http response.
    """
    return self.post(self.api_host, "/files", body, files)

  def submit_urls(self, urls=[], body=None):
    """Allows you to submit one or more URLs for malware analysis.
    
    Keyword Arguments:
        body {dict} -- The body of your http request. This is optional. (default: {None})
        urls {string} -- The URLs you will be submitting. (default: {None})
    
    Returns:
        dict -- Returns a dict of the http response.
    """
    formatted_urls = "[" + ",".join(list(map(lambda url: url.replace(url, f'"{url}"'), urls))) + "]"
    url_submission = { "urls": formatted_urls}

    return self.post(self.api_host, "/urls", body, url_submission)

  def get_health(self):
    """Allows you to get the status of the DoD service, as well as quota information for the API key.
    
    Returns:
        dict -- Returns the health details
    """
    return self.get(self.api_host, "/health")

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

  def get_artifact(self, report_id, artifact_type):
    """This endpoint fetches the screenshot gif file for the given report_id
    
    Arguments:
        report_id {string} -- The ID of the report to get artifacts for
        artifact_type {string} -- The type of artifact to get. ex. 'screenshot'
    
    Returns:
        dict -- Returns a dict of the http response.
    """
    return self.get(self.api_host, "/artifacts/{}?type={}".format(report_id,artifact_type))

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