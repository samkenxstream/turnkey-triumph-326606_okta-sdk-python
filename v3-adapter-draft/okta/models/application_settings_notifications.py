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

class ApplicationSettingsNotifications(object):
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
        'vpn': 'ApplicationSettingsNotificationsVpn'
    }

    attribute_map = {
        'vpn': 'vpn'
    }

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, vpn=None):  # noqa: E501
        """ApplicationSettingsNotifications - a model defined in Swagger"""  # noqa: E501
        self._vpn = None
        self.discriminator = None
        if vpn is not None:
            self.vpn = vpn

    @property
    def vpn(self):
        """Gets the vpn of this ApplicationSettingsNotifications.  # noqa: E501


        :return: The vpn of this ApplicationSettingsNotifications.  # noqa: E501
        :rtype: ApplicationSettingsNotificationsVpn
        """
        return self._vpn

    @vpn.setter
    def vpn(self, vpn):
        """Sets the vpn of this ApplicationSettingsNotifications.


        :param vpn: The vpn of this ApplicationSettingsNotifications.  # noqa: E501
        :type: ApplicationSettingsNotificationsVpn
        """

        self._vpn = vpn

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
        if issubclass(ApplicationSettingsNotifications, dict):
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
        if not isinstance(other, ApplicationSettingsNotifications):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
