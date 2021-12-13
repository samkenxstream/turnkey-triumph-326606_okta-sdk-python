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
from okta.models.application import Application  # noqa: F401,E501

from okta.helpers import to_snake_case

class OpenIdConnectApplication(Application):
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
        'credentials': 'OAuthApplicationCredentials',
        'name': 'str',
        'settings': 'OpenIdConnectApplicationSettings'
    }
    if hasattr(Application, "swagger_types"):
        swagger_types.update(Application.swagger_types)

    attribute_map = {
        'credentials': 'credentials',
        'name': 'name',
        'settings': 'settings'
    }
    if hasattr(Application, "attribute_map"):
        attribute_map.update(Application.attribute_map)

    def __init__(self, config=None):
        super().__init__(config)
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, credentials=None, name='oidc_client', settings=None, *args, **kwargs):  # noqa: E501
        """OpenIdConnectApplication - a model defined in Swagger"""  # noqa: E501
        self._credentials = None
        self._name = None
        self._settings = None
        self.discriminator = None
        if credentials is not None:
            self.credentials = credentials
        if name is not None:
            self.name = name
        if settings is not None:
            self.settings = settings

    @property
    def credentials(self):
        """Gets the credentials of this OpenIdConnectApplication.  # noqa: E501


        :return: The credentials of this OpenIdConnectApplication.  # noqa: E501
        :rtype: OAuthApplicationCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this OpenIdConnectApplication.


        :param credentials: The credentials of this OpenIdConnectApplication.  # noqa: E501
        :type: OAuthApplicationCredentials
        """

        self._credentials = credentials

    @property
    def name(self):
        """Gets the name of this OpenIdConnectApplication.  # noqa: E501


        :return: The name of this OpenIdConnectApplication.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OpenIdConnectApplication.


        :param name: The name of this OpenIdConnectApplication.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def settings(self):
        """Gets the settings of this OpenIdConnectApplication.  # noqa: E501


        :return: The settings of this OpenIdConnectApplication.  # noqa: E501
        :rtype: OpenIdConnectApplicationSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this OpenIdConnectApplication.


        :param settings: The settings of this OpenIdConnectApplication.  # noqa: E501
        :type: OpenIdConnectApplicationSettings
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
        if issubclass(OpenIdConnectApplication, dict):
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
        if not isinstance(other, OpenIdConnectApplication):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
