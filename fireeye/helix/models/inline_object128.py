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


class InlineObject128(object):
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
        'note': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'note': 'note',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, note=None, created_at=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject128 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._note = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.note = note
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def note(self):
        """Gets the note of this InlineObject128.  # noqa: E501

          # noqa: E501

        :return: The note of this InlineObject128.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this InlineObject128.

          # noqa: E501

        :param note: The note of this InlineObject128.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and note is None:  # noqa: E501
            raise ValueError("Invalid value for `note`, must not be `None`")  # noqa: E501

        self._note = note

    @property
    def created_at(self):
        """Gets the created_at of this InlineObject128.  # noqa: E501

          # noqa: E501

        :return: The created_at of this InlineObject128.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InlineObject128.

          # noqa: E501

        :param created_at: The created_at of this InlineObject128.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this InlineObject128.  # noqa: E501

          # noqa: E501

        :return: The updated_at of this InlineObject128.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this InlineObject128.

          # noqa: E501

        :param updated_at: The updated_at of this InlineObject128.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

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
        if not isinstance(other, InlineObject128):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject128):
            return True

        return self.to_dict() != other.to_dict()
