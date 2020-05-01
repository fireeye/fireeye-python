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


class InlineObject177(object):
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
        'is_enabled': 'bool',
        'repeat': 'str',
        'run_at': 'str',
        'state': 'str',
        'repeat_on': 'list[str]',
        'saved_search': 'str',
        'history': 'bool'
    }

    attribute_map = {
        'is_enabled': 'is_enabled',
        'repeat': 'repeat',
        'run_at': 'run_at',
        'state': 'state',
        'repeat_on': 'repeat_on',
        'saved_search': 'saved_search',
        'history': 'history'
    }

    def __init__(self, is_enabled=None, repeat=None, run_at=None, state=None, repeat_on=None, saved_search=None, history=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject177 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._is_enabled = None
        self._repeat = None
        self._run_at = None
        self._state = None
        self._repeat_on = None
        self._saved_search = None
        self._history = None
        self.discriminator = None

        if is_enabled is not None:
            self.is_enabled = is_enabled
        if repeat is not None:
            self.repeat = repeat
        self.run_at = run_at
        if state is not None:
            self.state = state
        if repeat_on is not None:
            self.repeat_on = repeat_on
        self.saved_search = saved_search
        if history is not None:
            self.history = history

    @property
    def is_enabled(self):
        """Gets the is_enabled of this InlineObject177.  # noqa: E501

          # noqa: E501

        :return: The is_enabled of this InlineObject177.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this InlineObject177.

          # noqa: E501

        :param is_enabled: The is_enabled of this InlineObject177.  # noqa: E501
        :type: bool
        """

        self._is_enabled = is_enabled

    @property
    def repeat(self):
        """Gets the repeat of this InlineObject177.  # noqa: E501

          # noqa: E501

        :return: The repeat of this InlineObject177.  # noqa: E501
        :rtype: str
        """
        return self._repeat

    @repeat.setter
    def repeat(self, repeat):
        """Sets the repeat of this InlineObject177.

          # noqa: E501

        :param repeat: The repeat of this InlineObject177.  # noqa: E501
        :type: str
        """

        self._repeat = repeat

    @property
    def run_at(self):
        """Gets the run_at of this InlineObject177.  # noqa: E501

          # noqa: E501

        :return: The run_at of this InlineObject177.  # noqa: E501
        :rtype: str
        """
        return self._run_at

    @run_at.setter
    def run_at(self, run_at):
        """Sets the run_at of this InlineObject177.

          # noqa: E501

        :param run_at: The run_at of this InlineObject177.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and run_at is None:  # noqa: E501
            raise ValueError("Invalid value for `run_at`, must not be `None`")  # noqa: E501

        self._run_at = run_at

    @property
    def state(self):
        """Gets the state of this InlineObject177.  # noqa: E501

          # noqa: E501

        :return: The state of this InlineObject177.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this InlineObject177.

          # noqa: E501

        :param state: The state of this InlineObject177.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def repeat_on(self):
        """Gets the repeat_on of this InlineObject177.  # noqa: E501

          # noqa: E501

        :return: The repeat_on of this InlineObject177.  # noqa: E501
        :rtype: list[str]
        """
        return self._repeat_on

    @repeat_on.setter
    def repeat_on(self, repeat_on):
        """Sets the repeat_on of this InlineObject177.

          # noqa: E501

        :param repeat_on: The repeat_on of this InlineObject177.  # noqa: E501
        :type: list[str]
        """

        self._repeat_on = repeat_on

    @property
    def saved_search(self):
        """Gets the saved_search of this InlineObject177.  # noqa: E501

          # noqa: E501

        :return: The saved_search of this InlineObject177.  # noqa: E501
        :rtype: str
        """
        return self._saved_search

    @saved_search.setter
    def saved_search(self, saved_search):
        """Sets the saved_search of this InlineObject177.

          # noqa: E501

        :param saved_search: The saved_search of this InlineObject177.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and saved_search is None:  # noqa: E501
            raise ValueError("Invalid value for `saved_search`, must not be `None`")  # noqa: E501

        self._saved_search = saved_search

    @property
    def history(self):
        """Gets the history of this InlineObject177.  # noqa: E501

          # noqa: E501

        :return: The history of this InlineObject177.  # noqa: E501
        :rtype: bool
        """
        return self._history

    @history.setter
    def history(self, history):
        """Sets the history of this InlineObject177.

          # noqa: E501

        :param history: The history of this InlineObject177.  # noqa: E501
        :type: bool
        """

        self._history = history

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
        if not isinstance(other, InlineObject177):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject177):
            return True

        return self.to_dict() != other.to_dict()
