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


class InlineObject107(object):
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
        'status': 'str',
        'severity': 'int',
        'tags': 'list[str]',
        'name': 'str',
        'priority': 'str',
        'state': 'str',
        'info_links': 'list[str]',
        'assigned_to': 'object',
        'total_days_unresolved': 'str',
        'description': 'str'
    }

    attribute_map = {
        'status': 'status',
        'severity': 'severity',
        'tags': 'tags',
        'name': 'name',
        'priority': 'priority',
        'state': 'state',
        'info_links': 'info_links',
        'assigned_to': 'assigned_to',
        'total_days_unresolved': 'total_days_unresolved',
        'description': 'description'
    }

    def __init__(self, status=None, severity=None, tags=None, name=None, priority=None, state=None, info_links=None, assigned_to=None, total_days_unresolved=None, description=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject107 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._status = None
        self._severity = None
        self._tags = None
        self._name = None
        self._priority = None
        self._state = None
        self._info_links = None
        self._assigned_to = None
        self._total_days_unresolved = None
        self._description = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if severity is not None:
            self.severity = severity
        if tags is not None:
            self.tags = tags
        self.name = name
        if priority is not None:
            self.priority = priority
        if state is not None:
            self.state = state
        if info_links is not None:
            self.info_links = info_links
        if assigned_to is not None:
            self.assigned_to = assigned_to
        if total_days_unresolved is not None:
            self.total_days_unresolved = total_days_unresolved
        if description is not None:
            self.description = description

    @property
    def status(self):
        """Gets the status of this InlineObject107.  # noqa: E501

          # noqa: E501

        :return: The status of this InlineObject107.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineObject107.

          # noqa: E501

        :param status: The status of this InlineObject107.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def severity(self):
        """Gets the severity of this InlineObject107.  # noqa: E501

          # noqa: E501

        :return: The severity of this InlineObject107.  # noqa: E501
        :rtype: int
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this InlineObject107.

          # noqa: E501

        :param severity: The severity of this InlineObject107.  # noqa: E501
        :type: int
        """

        self._severity = severity

    @property
    def tags(self):
        """Gets the tags of this InlineObject107.  # noqa: E501

          # noqa: E501

        :return: The tags of this InlineObject107.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this InlineObject107.

          # noqa: E501

        :param tags: The tags of this InlineObject107.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def name(self):
        """Gets the name of this InlineObject107.  # noqa: E501

          # noqa: E501

        :return: The name of this InlineObject107.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineObject107.

          # noqa: E501

        :param name: The name of this InlineObject107.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def priority(self):
        """Gets the priority of this InlineObject107.  # noqa: E501

          # noqa: E501

        :return: The priority of this InlineObject107.  # noqa: E501
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this InlineObject107.

          # noqa: E501

        :param priority: The priority of this InlineObject107.  # noqa: E501
        :type: str
        """

        self._priority = priority

    @property
    def state(self):
        """Gets the state of this InlineObject107.  # noqa: E501

          # noqa: E501

        :return: The state of this InlineObject107.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this InlineObject107.

          # noqa: E501

        :param state: The state of this InlineObject107.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def info_links(self):
        """Gets the info_links of this InlineObject107.  # noqa: E501

          # noqa: E501

        :return: The info_links of this InlineObject107.  # noqa: E501
        :rtype: list[str]
        """
        return self._info_links

    @info_links.setter
    def info_links(self, info_links):
        """Sets the info_links of this InlineObject107.

          # noqa: E501

        :param info_links: The info_links of this InlineObject107.  # noqa: E501
        :type: list[str]
        """

        self._info_links = info_links

    @property
    def assigned_to(self):
        """Gets the assigned_to of this InlineObject107.  # noqa: E501

          # noqa: E501

        :return: The assigned_to of this InlineObject107.  # noqa: E501
        :rtype: object
        """
        return self._assigned_to

    @assigned_to.setter
    def assigned_to(self, assigned_to):
        """Sets the assigned_to of this InlineObject107.

          # noqa: E501

        :param assigned_to: The assigned_to of this InlineObject107.  # noqa: E501
        :type: object
        """

        self._assigned_to = assigned_to

    @property
    def total_days_unresolved(self):
        """Gets the total_days_unresolved of this InlineObject107.  # noqa: E501

          # noqa: E501

        :return: The total_days_unresolved of this InlineObject107.  # noqa: E501
        :rtype: str
        """
        return self._total_days_unresolved

    @total_days_unresolved.setter
    def total_days_unresolved(self, total_days_unresolved):
        """Sets the total_days_unresolved of this InlineObject107.

          # noqa: E501

        :param total_days_unresolved: The total_days_unresolved of this InlineObject107.  # noqa: E501
        :type: str
        """

        self._total_days_unresolved = total_days_unresolved

    @property
    def description(self):
        """Gets the description of this InlineObject107.  # noqa: E501

          # noqa: E501

        :return: The description of this InlineObject107.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineObject107.

          # noqa: E501

        :param description: The description of this InlineObject107.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if not isinstance(other, InlineObject107):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject107):
            return True

        return self.to_dict() != other.to_dict()
