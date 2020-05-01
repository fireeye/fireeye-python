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


class InlineObject65(object):
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
        'description': 'str',
        'deleted': 'bool',
        'is_hidden': 'bool',
        'id': 'str',
        'is_default': 'bool',
        'name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'deleted': 'deleted',
        'is_hidden': 'is_hidden',
        'id': 'id',
        'is_default': 'isDefault',
        'name': 'name'
    }

    def __init__(self, description=None, deleted=None, is_hidden=None, id=None, is_default=None, name=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject65 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._deleted = None
        self._is_hidden = None
        self._id = None
        self._is_default = None
        self._name = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if deleted is not None:
            self.deleted = deleted
        if is_hidden is not None:
            self.is_hidden = is_hidden
        if id is not None:
            self.id = id
        if is_default is not None:
            self.is_default = is_default
        self.name = name

    @property
    def description(self):
        """Gets the description of this InlineObject65.  # noqa: E501

          # noqa: E501

        :return: The description of this InlineObject65.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineObject65.

          # noqa: E501

        :param description: The description of this InlineObject65.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def deleted(self):
        """Gets the deleted of this InlineObject65.  # noqa: E501

          # noqa: E501

        :return: The deleted of this InlineObject65.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this InlineObject65.

          # noqa: E501

        :param deleted: The deleted of this InlineObject65.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def is_hidden(self):
        """Gets the is_hidden of this InlineObject65.  # noqa: E501

          # noqa: E501

        :return: The is_hidden of this InlineObject65.  # noqa: E501
        :rtype: bool
        """
        return self._is_hidden

    @is_hidden.setter
    def is_hidden(self, is_hidden):
        """Sets the is_hidden of this InlineObject65.

          # noqa: E501

        :param is_hidden: The is_hidden of this InlineObject65.  # noqa: E501
        :type: bool
        """

        self._is_hidden = is_hidden

    @property
    def id(self):
        """Gets the id of this InlineObject65.  # noqa: E501

          # noqa: E501

        :return: The id of this InlineObject65.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineObject65.

          # noqa: E501

        :param id: The id of this InlineObject65.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_default(self):
        """Gets the is_default of this InlineObject65.  # noqa: E501

          # noqa: E501

        :return: The is_default of this InlineObject65.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this InlineObject65.

          # noqa: E501

        :param is_default: The is_default of this InlineObject65.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

    @property
    def name(self):
        """Gets the name of this InlineObject65.  # noqa: E501

          # noqa: E501

        :return: The name of this InlineObject65.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineObject65.

          # noqa: E501

        :param name: The name of this InlineObject65.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if not isinstance(other, InlineObject65):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject65):
            return True

        return self.to_dict() != other.to_dict()
