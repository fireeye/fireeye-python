# coding: utf-8

"""
    Helix API Documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from fireeye.helix.configuration import Configuration


class InlineObject74(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'count': 'int',
        'start_date': 'str',
        'error_message': 'str',
        'end_date': 'str',
        'parent_id': 'str',
        'results': 'str',
        'updated_date': 'str',
        'took': 'int',
        'state': 'str',
        'created_date': 'str',
        'customer_id': 'str'
    }

    attribute_map = {
        'count': 'count',
        'start_date': 'startDate',
        'error_message': 'errorMessage',
        'end_date': 'endDate',
        'parent_id': 'parentId',
        'results': 'results',
        'updated_date': 'updatedDate',
        'took': 'took',
        'state': 'state',
        'created_date': 'createdDate',
        'customer_id': 'customer_id'
    }

    def __init__(self, count=None, start_date=None, error_message=None, end_date=None, parent_id=None, results=None, updated_date=None, took=None, state=None, created_date=None, customer_id=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject74 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._count = None
        self._start_date = None
        self._error_message = None
        self._end_date = None
        self._parent_id = None
        self._results = None
        self._updated_date = None
        self._took = None
        self._state = None
        self._created_date = None
        self._customer_id = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if start_date is not None:
            self.start_date = start_date
        if error_message is not None:
            self.error_message = error_message
        if end_date is not None:
            self.end_date = end_date
        self.parent_id = parent_id
        if results is not None:
            self.results = results
        if updated_date is not None:
            self.updated_date = updated_date
        if took is not None:
            self.took = took
        if state is not None:
            self.state = state
        if created_date is not None:
            self.created_date = created_date
        if customer_id is not None:
            self.customer_id = customer_id

    @property
    def count(self):
        """Gets the count of this InlineObject74.  # noqa: E501

          # noqa: E501

        :return: The count of this InlineObject74.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this InlineObject74.

          # noqa: E501

        :param count: The count of this InlineObject74.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def start_date(self):
        """Gets the start_date of this InlineObject74.  # noqa: E501

          # noqa: E501

        :return: The start_date of this InlineObject74.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this InlineObject74.

          # noqa: E501

        :param start_date: The start_date of this InlineObject74.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def error_message(self):
        """Gets the error_message of this InlineObject74.  # noqa: E501

          # noqa: E501

        :return: The error_message of this InlineObject74.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this InlineObject74.

          # noqa: E501

        :param error_message: The error_message of this InlineObject74.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def end_date(self):
        """Gets the end_date of this InlineObject74.  # noqa: E501

          # noqa: E501

        :return: The end_date of this InlineObject74.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this InlineObject74.

          # noqa: E501

        :param end_date: The end_date of this InlineObject74.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def parent_id(self):
        """Gets the parent_id of this InlineObject74.  # noqa: E501

          # noqa: E501

        :return: The parent_id of this InlineObject74.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this InlineObject74.

          # noqa: E501

        :param parent_id: The parent_id of this InlineObject74.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and parent_id is None:  # noqa: E501
            raise ValueError("Invalid value for `parent_id`, must not be `None`")  # noqa: E501

        self._parent_id = parent_id

    @property
    def results(self):
        """Gets the results of this InlineObject74.  # noqa: E501

          # noqa: E501

        :return: The results of this InlineObject74.  # noqa: E501
        :rtype: str
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this InlineObject74.

          # noqa: E501

        :param results: The results of this InlineObject74.  # noqa: E501
        :type: str
        """

        self._results = results

    @property
    def updated_date(self):
        """Gets the updated_date of this InlineObject74.  # noqa: E501

          # noqa: E501

        :return: The updated_date of this InlineObject74.  # noqa: E501
        :rtype: str
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """Sets the updated_date of this InlineObject74.

          # noqa: E501

        :param updated_date: The updated_date of this InlineObject74.  # noqa: E501
        :type: str
        """

        self._updated_date = updated_date

    @property
    def took(self):
        """Gets the took of this InlineObject74.  # noqa: E501

          # noqa: E501

        :return: The took of this InlineObject74.  # noqa: E501
        :rtype: int
        """
        return self._took

    @took.setter
    def took(self, took):
        """Sets the took of this InlineObject74.

          # noqa: E501

        :param took: The took of this InlineObject74.  # noqa: E501
        :type: int
        """

        self._took = took

    @property
    def state(self):
        """Gets the state of this InlineObject74.  # noqa: E501

          # noqa: E501

        :return: The state of this InlineObject74.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this InlineObject74.

          # noqa: E501

        :param state: The state of this InlineObject74.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def created_date(self):
        """Gets the created_date of this InlineObject74.  # noqa: E501

          # noqa: E501

        :return: The created_date of this InlineObject74.  # noqa: E501
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this InlineObject74.

          # noqa: E501

        :param created_date: The created_date of this InlineObject74.  # noqa: E501
        :type: str
        """

        self._created_date = created_date

    @property
    def customer_id(self):
        """Gets the customer_id of this InlineObject74.  # noqa: E501

          # noqa: E501

        :return: The customer_id of this InlineObject74.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this InlineObject74.

          # noqa: E501

        :param customer_id: The customer_id of this InlineObject74.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineObject74):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject74):
            return True

        return self.to_dict() != other.to_dict()
