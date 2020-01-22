# Copyright (C) 2019 FireEye, Inc. All Rights Reserved.
from platform import python_version
from .errors import *
import os
import requests
import logging

__version__ = "0.1.0"
logger = logging.getLogger("fireeye")

class Helix:
  """The Helix class allows your app to communicate with FireEye's Helix service.add()
  
  The Helix service allows you to interact with your Helix instance in a programmatic manner.add()

  This client handles constructing and sending HTTP requests to Helix as well as parsing any responses received.


  Keyword Arguments:
      key {string} -- The API key provided to you by the Helix service.
      host {string} -- The hostname of the Helix API service
      helix_id = {string} -- The ID of the Helix instance
  """
  def __init__(self,key, helix_id, host="apps.fireeye.com", ):
    self.__api_key = key
    self.__api_host = host
    self.__helix_id = helix_id
    user_agent = "fireeye-python/{version} python/{python_version}".format(
      version=__version__, python_version=python_version()
    )
    self.__headers = {"User-Agent": user_agent, "x-fireeye-api-key": key}
    self.__session = requests.Session()


  def get_alerts(self, **query):
    """Gathers a list of alerts for a single Helix instance.
    
    Arguments:
        **query -- One or more query parameters to use with this request.
    
    Returns:
        dict -- Returns a dict of the http response.
    """
    return self.__get(self.__api_host, f"/helix/id/{self.__helix_id}/api/v3/alerts", query)


  def get_alerts_fields(self, **query):
    """Lists all fields that describe alerts.

    Arguments:
        **query -- One or more query parameters to use with this request.
        
    Returns:
        dict -- Returns a dict of the http response.
    """
    return self.__get(self.__api_host, f"/helix/id/{self.__helix_id}/api/v3/alerts/fields", query)


  def get_alerts_org_metrics(self, **query):
    """Lists alert metrics by organization.

    Arguments:
        **query -- One or more query parameters to use with this request.
        
    Returns:
        dict -- Returns a dict of the http response.
    """
    return self.__get(self.__api_host, f"/helix/id/{self.__helix_id}/api/v3/alerts/org_metrics", query)


  def get_alerts_search(self, **query):
    """Search alerts

    Arguments:
        **query -- One or more query parameters to use with this request.
        
    Returns:
        dict -- Returns a dict of the http response.
    """
    return self.__get(self.__api_host, f"/helix/id/{self.__helix_id}/api/v3/alerts/search", query)

  
  def get_alerts_values(self, **query):
    """Lists the number of occurrences of each field value.

    Arguments:
        **query -- One or more query parameters to use with this request.
        
    Returns:
        dict -- Returns a dict of the http response.
    """
    return self.__get(self.__api_host, f"/helix/id/{self.__helix_id}/api/v3/alerts/values", query)


  def get_alert(self, alert_id, **query):
    """Gets the details of a single alert

    Arguments:
        alert_id {integer} -- The primary ID of the alert to get
        **query -- One or more query parameters to use with this request.
        
    Returns:
        dict -- Returns a dict of the http response.
    """
    return self.__get(self.__api_host, f"/helix/id/{self.__helix_id}/api/v3/alerts/{alert_id}", query)


  def get_alert_context(self, alert_id, **query):
    """Gets the instances and indicators for a specific alert.

    Arguments:
        alert_id {integer} -- The primary ID of the alert to get
        **query -- One or more query parameters to use with this request.
        
    Returns:
        dict -- Returns a dict of the http response.
    """
    return self.__get(self.__api_host, f"/helix/id/{self.__helix_id}/api/v3/alerts/{alert_id}/context", query)


  def get_alert_endpoints(self, alert_id, **query):
    """Retrieves a specific alert from an HX endpoint.

    Arguments:
        alert_id {integer} -- The primary ID of the alert to get
        **query -- One or more query parameters to use with this request.
        
    Returns:
        dict -- Returns a dict of the http response.
    """
    return self.__get(self.__api_host, f"/helix/id/{self.__helix_id}/api/v3/alerts/{alert_id}/endpoints", query)


  def get_alert_events(self, alert_id, **query):
    """Lists alert events for a specific alert.

    Arguments:
        alert_id {integer} -- The primary ID of the alert to get
        **query -- One or more query parameters to use with this request.
        
    Returns:
        dict -- Returns a dict of the http response.
    """
    return self.__get(self.__api_host, f"/helix/id/{self.__helix_id}/api/v3/alerts/{alert_id}/events", query)


  def get_alert_investigations(self, alert_id, **query):
    """Retrieves Managed Defense investigation results for an alert.

    Arguments:
        alert_id {integer} -- The primary ID of the alert to get
        **query -- One or more query parameters to use with this request.
        
    Returns:
        dict -- Returns a dict of the http response.
    """
    return self.__get(self.__api_host, f"/helix/id/{self.__helix_id}/api/v3/alerts/{alert_id}/investigations", query)


  def get_alert_revisions(self, alert_id, **query):
    """Returns the revision history.

    Arguments:
        alert_id {integer} -- The primary ID of the alert to get
        **query -- One or more query parameters to use with this request.
        
    Returns:
        dict -- Returns a dict of the http response.
    """
    return self.__get(self.__api_host, f"/helix/id/{self.__helix_id}/api/v3/alerts/{alert_id}/revisions", query)


  def get_alert_tips(self, alert_id, **query):
    """Lists the investigative tips for a specific alert.

    Arguments:
        alert_id {integer} -- The primary ID of the alert to get
        **query -- One or more query parameters to use with this request.
        
    Returns:
        dict -- Returns a dict of the http response.
    """
    return self.__get(self.__api_host, f"/helix/id/{self.__helix_id}/api/v3/alerts/{alert_id}/tips", query)

  
  def get_alert_cases(self, alert_id, **query):
    """Get cases for an alert

    Arguments:
        alert_id {integer} -- The primary ID of the alert to get
        **query -- One or more query parameters to use with this request.
        
    Returns:
        dict -- Returns a dict of the http response.
    """
    return self.__get(self.__api_host, f"/helix/id/{self.__helix_id}/api/v3/alerts/{alert_id}/cases", query)


  def get_alert_cases_search(self, alert_id, **query):
    """Search cases in an alert

    Arguments:
        alert_id {integer} -- The primary ID of the alert to get
        **query -- One or more query parameters to use with this request.
        
    Returns:
        dict -- Returns a dict of the http response.
    """
    return self.__get(self.__api_host, f"/helix/id/{self.__helix_id}/api/v3/alerts/{alert_id}/cases/search", query)


  def get_alert_case(self, alert_id, case_id, **query):
    """Get the details of a single case in an alert

    Arguments:
        alert_id {integer} -- The primary ID of the alert to get
        case_id {integer} -- The ID of the case to be deleted
        **query -- One or more query parameters to use with this request.
        
    Returns:
        dict -- Returns a dict of the http response.
    """
    return self.__get(self.__api_host, f"/helix/id/{self.__helix_id}/api/v3/alerts/{alert_id}/cases/{case_id}", query)


  def get_alert_plays(self, alert_id, **query):
    """Get the plays for an alert

    Arguments:
        alert_id {integer} -- The primary ID of the alert to get
        **query -- One or more query parameters to use with this request.
        
    Returns:
        dict -- Returns a dict of the http response.
    """
    return self.__get(self.__api_host, f"/helix/id/{self.__helix_id}/api/v3/alerts/{alert_id}/plays", query)


  def get_alert_plays_search(self, alert_id, **query):
    """Search the plays of an alert

    Arguments:
        alert_id {integer} -- The primary ID of the alert to get
        **query -- One or more query parameters to use with this request.
        
    Returns:
        dict -- Returns a dict of the http response.
    """
    return self.__get(self.__api_host, f"/helix/id/{self.__helix_id}/api/v3/alerts/{alert_id}/plays/search", query)


  def get_alert_play(self, alert_id, play_id, **query):
    """Get a single play for an alert

    Arguments:
        alert_id {integer} -- The primary ID of the alert to get
        play_id {integer} -- The primary ID of the play to get
        **query -- One or more query parameters to use with this request.
        
    Returns:
        dict -- Returns a dict of the http response.
    """
    return self.__get(self.__api_host, f"/helix/id/{self.__helix_id}/api/v3/alerts/{alert_id}/plays/{play_id}", query)


  def get_alert_notes(self, alert_id, **query):
    """Get the notes for an alert

    Arguments:
        alert_id {integer} -- The primary ID of the alert to get
        **query -- One or more query parameters to use with this request.
        
    Returns:
        dict -- Returns a dict of the http response.
    """
    return self.__get(self.__api_host, f"/helix/id/{self.__helix_id}/api/v3/alerts/{alert_id}/notes", query)


  def get_alert_note(self, alert_id, note_id, **query):
    """Get a single note for an alert

    Arguments:
        alert_id {integer} -- The primary ID of the alert to get
        note_id {integer} -- The primary ID of the note to get
        **query -- One or more query parameters to use with this request.
        
    Returns:
        dict -- Returns a dict of the http response.
    """
    return self.__get(self.__api_host, f"/helix/id/{self.__helix_id}/api/v3/alerts/{alert_id}/notes/{note_id}", query)


  def get_alert_types(self, **query):
    """Get alert types

    Arguments:
        **query -- One or more query parameters to use with this request.
        
    Returns:
        dict -- Returns a dict of the http response.
    """
    return self.__get(self.__api_host, f"/helix/id/{self.__helix_id}/api/v3/alerts/types", query)


  def get_alert_types_search(self, **query):
    """Search alert types

    Arguments:
        **query -- One or more query parameters to use with this request.
        
    Returns:
        dict -- Returns a dict of the http response.
    """
    return self.__get(self.__api_host, f"/helix/id/{self.__helix_id}/api/v3/alerts/types/search", query)


  def get_alert_type(self, type_id, **query):
    """Get the details of a single alert type

    Arguments:
        type_id {integer} -- The primary ID of an alert type
        **query -- One or more query parameters to use with this request.
        
    Returns:
        dict -- Returns a dict of the http response.
    """
    return self.__get(self.__api_host, f"/helix/id/{self.__helix_id}/api/v3/alerts/types/{type_id}", query)

  
  def create_alert(self, body):
    """Creates a new alert.
    
    Keyword Arguments:
        body {dict} -- The body of your http request.
    
    Returns:
        dict -- Returns a dict of the http response.
    """
    return self.__post(self.__api_host, f"/helix/id/{self.__helix_id}/api/v3/alerts/values", body)


  def create_alert_case(self, alert_id, body):
    """Creates a new alert case.
    
    Keyword Arguments:
        alert_id {integer} -- The ID of the alert to create a case for
        body {dict} -- The body of your http request.
    
    Returns:
        dict -- Returns a dict of the http response.
    """
    return self.__post(self.__api_host, f"/helix/id/{self.__helix_id}/api/v3/alerts/{alert_id}/cases", body)


  def create_alert_note(self, alert_id, body):
    """Creates a new alert note.
    
    Keyword Arguments:
        alert_id {integer} -- The ID of the alert to create a note for
        body {dict} -- The body of your http request.
    
    Returns:
        dict -- Returns a dict of the http response.
    """
    return self.__post(self.__api_host, f"/helix/id/{self.__helix_id}/api/v3/alerts/{alert_id}/notes", body)


  def create_alert_type(self, body):
    """Creates a new alert type.
    
    Keyword Arguments:
        body {dict} -- The body of your http request.
    
    Returns:
        dict -- Returns a dict of the http response.
    """
    return self.__post(self.__api_host, f"/helix/id/{self.__helix_id}/api/v3/alerts/types", body)


  def update_alert_case(self, alert_id, case_id, body):
    """Full or partial update of an alert case

    Arguments:
        alert_id {integer} -- The primary ID of the alert to get
        case_id {integer} -- The ID of the case to be updated
        body {dict} -- A dictionary of fields:values to update
        
    Returns:
        dict -- Returns a dict of the http response.
    """
    return self.__put(self.__api_host, f"/helix/id/{self.__helix_id}/api/v3/alerts/{alert_id}/cases/{case_id}", body)


  def update_alert_note(self, alert_id, note_id, body):
    """Full or partial update of an alert note

    Arguments:
        alert_id {integer} -- The primary ID of the alert to get
        note_id {integer} -- The ID of the note to be updated
        body {dict} -- A dictionary of fields:values to update
        
    Returns:
        dict -- Returns a dict of the http response.
    """
    return self.__put(self.__api_host, f"/helix/id/{self.__helix_id}/api/v3/alerts/{alert_id}/notes/{note_id}", body)


  def update_alert_type(self, type_id, body):
    """Full or partial update of an alert type

    Arguments:
        type_id {integer} -- The primary ID of the type to update
        body {dict} -- A dictionary of fields:values to update
        
    Returns:
        dict -- Returns a dict of the http response.
    """
    return self.__put(self.__api_host, f"/helix/id/{self.__helix_id}/api/v3/alerts/types/{type_id}", body)


  def delete_alert_case(self, alert_id, case_id):
    """Deletes a single alert case.
    
    Keyword Arguments:
        alert_id {integer} -- The ID of the alert that contains the case to be deleted
        case_id {integer} -- The ID of the case to be deleted
    
    Returns:
        dict -- Returns a dict of the http response.
    """
    return self.__post(self.__api_host, f"/helix/id/{self.__helix_id}/api/v3/alerts/{alert_id}/cases/{case_id}")


  def delete_alert_cases(self, alert_id):
    """Deletes all cases in an alert
    
    Keyword Arguments:
        alert_id {integer} -- The ID of the alert that contains the cases to be deleted
    
    Returns:
        dict -- Returns a dict of the http response.
    """
    return self.__post(self.__api_host, f"/helix/id/{self.__helix_id}/api/v3/alerts/{alert_id}/cases")


  def delete_alert_note(self, alert_id, note_id):
    """Deletes a single alert note.
    
    Keyword Arguments:
        alert_id {integer} -- The ID of the alert that contains the note to be deleted
        note_id {integer} -- The ID of the note to be deleted
    
    Returns:
        dict -- Returns a dict of the http response.
    """
    return self.__post(self.__api_host, f"/helix/id/{self.__helix_id}/api/v3/alerts/{alert_id}/notes/{note_id}")


  def delete_alert_type(self, type_id):
    """Deletes a single alert type.
    
    Keyword Arguments:
        type_id {integer} -- The ID of the type to be deleted
    
    Returns:
        dict -- Returns a dict of the http response.
    """
    return self.__post(self.__api_host, f"/helix/id/{self.__helix_id}/api/v3/alerts/types/{type_id}")


  def __get(self, host, request_uri, params=None):
    uri = "https://{host}{request_uri}".format(host=host, request_uri=request_uri)
    headers = self.__headers

    logger.debug("GET to %r with params %r, headers %r", uri, params, headers)
    return self.__parse(host, self.__session.get(uri, params=params, headers=headers))


  def __post(self, host, request_uri, data=None):
    uri = "https://{host}{request_uri}".format(host=host, request_uri=request_uri)
    headers = self.__headers

    logger.debug("POST to %r with data %r, headers %r", uri, data, headers)
    return self.__parse(host, self.__session.post(uri, data=data, headers=headers))


  def __put(self, host, request_uri, data=None):
    uri = "https://{host}{request_uri}".format(host=host, request_uri=request_uri)
    headers = self.__headers

    logger.debug("PUT to %r with data %r, headers %r", uri, data, headers)
    return self.__parse(host, self.__session.put(uri, data=data, headers=headers))


  def __delete(self, host, request_uri):
    uri = "https://{host}{request_uri}".format(host=host, request_uri=request_uri)
    headers = self.__headers

    logger.debug("DELETE to %r with headers %r", uri, headers)
    return self.__parse(host, self.__session.delete(uri, headers=headers))


  def __parse(self, host, response):
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