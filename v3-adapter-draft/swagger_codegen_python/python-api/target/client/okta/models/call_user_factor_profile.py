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

class CallUserFactorProfile(object):
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
        'phone_extension': 'str',
        'phone_number': 'str'
    }

    attribute_map = {
        'phone_extension': 'phoneExtension',
        'phone_number': 'phoneNumber'
    }

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, phone_extension=None, phone_number=None):  # noqa: E501
        """CallUserFactorProfile - a model defined in Swagger"""  # noqa: E501
        self._phone_extension = None
        self._phone_number = None
        self.discriminator = None
        if phone_extension is not None:
            self.phone_extension = phone_extension
        if phone_number is not None:
            self.phone_number = phone_number

    @property
    def phone_extension(self):
        """Gets the phone_extension of this CallUserFactorProfile.  # noqa: E501


        :return: The phone_extension of this CallUserFactorProfile.  # noqa: E501
        :rtype: str
        """
        return self._phone_extension

    @phone_extension.setter
    def phone_extension(self, phone_extension):
        """Sets the phone_extension of this CallUserFactorProfile.


        :param phone_extension: The phone_extension of this CallUserFactorProfile.  # noqa: E501
        :type: str
        """

        self._phone_extension = phone_extension

    @property
    def phone_number(self):
        """Gets the phone_number of this CallUserFactorProfile.  # noqa: E501


        :return: The phone_number of this CallUserFactorProfile.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this CallUserFactorProfile.


        :param phone_number: The phone_number of this CallUserFactorProfile.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

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
        if issubclass(CallUserFactorProfile, dict):
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
        if not isinstance(other, CallUserFactorProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
