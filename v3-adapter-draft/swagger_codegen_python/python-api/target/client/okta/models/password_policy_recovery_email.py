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

from okta.helpers import to_snake_case

class PasswordPolicyRecoveryEmail(object):
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
        'properties': 'PasswordPolicyRecoveryEmailProperties',
        'status': 'str'
    }

    attribute_map = {
        'properties': 'properties',
        'status': 'status'
    }

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, properties=None, status=None):  # noqa: E501
        """PasswordPolicyRecoveryEmail - a model defined in Swagger"""  # noqa: E501
        self._properties = None
        self._status = None
        self.discriminator = None
        if properties is not None:
            self.properties = properties
        if status is not None:
            self.status = status

    @property
    def properties(self):
        """Gets the properties of this PasswordPolicyRecoveryEmail.  # noqa: E501


        :return: The properties of this PasswordPolicyRecoveryEmail.  # noqa: E501
        :rtype: PasswordPolicyRecoveryEmailProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this PasswordPolicyRecoveryEmail.


        :param properties: The properties of this PasswordPolicyRecoveryEmail.  # noqa: E501
        :type: PasswordPolicyRecoveryEmailProperties
        """

        self._properties = properties

    @property
    def status(self):
        """Gets the status of this PasswordPolicyRecoveryEmail.  # noqa: E501


        :return: The status of this PasswordPolicyRecoveryEmail.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PasswordPolicyRecoveryEmail.


        :param status: The status of this PasswordPolicyRecoveryEmail.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if issubclass(PasswordPolicyRecoveryEmail, dict):
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
        if not isinstance(other, PasswordPolicyRecoveryEmail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
