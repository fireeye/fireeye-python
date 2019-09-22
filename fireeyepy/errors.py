class Error(Exception):
  pass

class AuthenticationError(Error):
  pass

class ServerError(Error):
  pass

class ClientError(Error):
  pass