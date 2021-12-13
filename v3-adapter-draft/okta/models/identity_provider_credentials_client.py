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

class IdentityProviderCredentialsClient(object):
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
        'client_id': 'str',
        'client_secret': 'str'
    }

    attribute_map = {
        'client_id': 'client_id',
        'client_secret': 'client_secret'
    }

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, client_id=None, client_secret=None):  # noqa: E501
        """IdentityProviderCredentialsClient - a model defined in Swagger"""  # noqa: E501
        self._client_id = None
        self._client_secret = None
        self.discriminator = None
        if client_id is not None:
            self.client_id = client_id
        if client_secret is not None:
            self.client_secret = client_secret

    @property
    def client_id(self):
        """Gets the client_id of this IdentityProviderCredentialsClient.  # noqa: E501


        :return: The client_id of this IdentityProviderCredentialsClient.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this IdentityProviderCredentialsClient.


        :param client_id: The client_id of this IdentityProviderCredentialsClient.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def client_secret(self):
        """Gets the client_secret of this IdentityProviderCredentialsClient.  # noqa: E501


        :return: The client_secret of this IdentityProviderCredentialsClient.  # noqa: E501
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """Sets the client_secret of this IdentityProviderCredentialsClient.


        :param client_secret: The client_secret of this IdentityProviderCredentialsClient.  # noqa: E501
        :type: str
        """

        self._client_secret = client_secret

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
        if issubclass(IdentityProviderCredentialsClient, dict):
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
        if not isinstance(other, IdentityProviderCredentialsClient):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
