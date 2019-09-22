from platform import python_version
from .errors import *
import os
import requests
import logging

__version__ = "0.0.1"
logger = logging.getLogger("fireeye")

class Detection:
  def __init__(self,key=None):
    self.api_key = key or os.environ.get("FIREEYE_API_KEY", None)
    self.api_host = "feapi.marketplace.apps.fireeye.com"
    user_agent = "fireeye-python/{version} python/{python_version}".format(
      version=__version__, python_version=python_version()
    )
    self.headers = {"User-Agent": user_agent, "feye-auth-key": key}
    self.session = requests.Session()
  
  def submit_file(self, body=None, files=None):
    return self.post(self.api_host, "/file-submit", body, files)

  def get_file_result(self, submission_id):
    return self.get(self.api_host, "/file-result", {"submission_id": submission_id})

  def get_hash_lookup(self, hash):
    return self.get(self.api_host, "/hash-lookup", {"hash": hash})

  def get_submissions(self):
    return self.get(self.api_host, "/get-submissions")

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