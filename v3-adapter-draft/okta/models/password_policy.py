# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API  # noqa: E501

    OpenAPI spec version: 2.7.0
    Contact: devex-public@okta.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from okta.models.policy import Policy  # noqa: F401,E501

from okta.helpers import to_snake_case

class PasswordPolicy(Policy):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'conditions': 'PasswordPolicyConditions',
        'settings': 'PasswordPolicySettings'
    }
    if hasattr(Policy, "swagger_types"):
        swagger_types.update(Policy.swagger_types)

    attribute_map = {
        'conditions': 'conditions',
        'settings': 'settings'
    }
    if hasattr(Policy, "attribute_map"):
        attribute_map.update(Policy.attribute_map)

    def __init__(self, config=None):
        super().__init__(config)
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, conditions=None, settings=None, *args, **kwargs):  # noqa: E501
        """PasswordPolicy - a model defined in Swagger"""  # noqa: E501
        self._conditions = None
        self._settings = None
        self.discriminator = None
        if conditions is not None:
            self.conditions = conditions
        if settings is not None:
            self.settings = settings

    @property
    def conditions(self):
        """Gets the conditions of this PasswordPolicy.  # noqa: E501


        :return: The conditions of this PasswordPolicy.  # noqa: E501
        :rtype: PasswordPolicyConditions
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this PasswordPolicy.


        :param conditions: The conditions of this PasswordPolicy.  # noqa: E501
        :type: PasswordPolicyConditions
        """

        self._conditions = conditions

    @property
    def settings(self):
        """Gets the settings of this PasswordPolicy.  # noqa: E501


        :return: The settings of this PasswordPolicy.  # noqa: E501
        :rtype: PasswordPolicySettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this PasswordPolicy.


        :param settings: The settings of this PasswordPolicy.  # noqa: E501
        :type: PasswordPolicySettings
        """

        self._settings = settings

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(PasswordPolicy, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PasswordPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
