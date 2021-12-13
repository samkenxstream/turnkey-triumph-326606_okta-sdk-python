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

class OpenIdConnectApplicationSettingsRefreshToken(object):
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
        'leeway': 'int',
        'rotation_type': 'OpenIdConnectRefreshTokenRotationType'
    }

    attribute_map = {
        'leeway': 'leeway',
        'rotation_type': 'rotation_type'
    }

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, leeway=None, rotation_type=None):  # noqa: E501
        """OpenIdConnectApplicationSettingsRefreshToken - a model defined in Swagger"""  # noqa: E501
        self._leeway = None
        self._rotation_type = None
        self.discriminator = None
        if leeway is not None:
            self.leeway = leeway
        if rotation_type is not None:
            self.rotation_type = rotation_type

    @property
    def leeway(self):
        """Gets the leeway of this OpenIdConnectApplicationSettingsRefreshToken.  # noqa: E501


        :return: The leeway of this OpenIdConnectApplicationSettingsRefreshToken.  # noqa: E501
        :rtype: int
        """
        return self._leeway

    @leeway.setter
    def leeway(self, leeway):
        """Sets the leeway of this OpenIdConnectApplicationSettingsRefreshToken.


        :param leeway: The leeway of this OpenIdConnectApplicationSettingsRefreshToken.  # noqa: E501
        :type: int
        """

        self._leeway = leeway

    @property
    def rotation_type(self):
        """Gets the rotation_type of this OpenIdConnectApplicationSettingsRefreshToken.  # noqa: E501


        :return: The rotation_type of this OpenIdConnectApplicationSettingsRefreshToken.  # noqa: E501
        :rtype: OpenIdConnectRefreshTokenRotationType
        """
        return self._rotation_type

    @rotation_type.setter
    def rotation_type(self, rotation_type):
        """Sets the rotation_type of this OpenIdConnectApplicationSettingsRefreshToken.


        :param rotation_type: The rotation_type of this OpenIdConnectApplicationSettingsRefreshToken.  # noqa: E501
        :type: OpenIdConnectRefreshTokenRotationType
        """

        self._rotation_type = rotation_type

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
        if issubclass(OpenIdConnectApplicationSettingsRefreshToken, dict):
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
        if not isinstance(other, OpenIdConnectApplicationSettingsRefreshToken):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
