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

class VerifyUserFactorResponse(object):
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
        'embedded': 'dict(str, object)',
        'links': 'dict(str, object)',
        'expires_at': 'datetime',
        'factor_result': 'str',
        'factor_result_message': 'str'
    }

    attribute_map = {
        'embedded': '_embedded',
        'links': '_links',
        'expires_at': 'expiresAt',
        'factor_result': 'factorResult',
        'factor_result_message': 'factorResultMessage'
    }

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, embedded=None, links=None, expires_at=None, factor_result=None, factor_result_message=None):  # noqa: E501
        """VerifyUserFactorResponse - a model defined in Swagger"""  # noqa: E501
        self._embedded = None
        self._links = None
        self._expires_at = None
        self._factor_result = None
        self._factor_result_message = None
        self.discriminator = None
        if embedded is not None:
            self.embedded = embedded
        if links is not None:
            self.links = links
        if expires_at is not None:
            self.expires_at = expires_at
        if factor_result is not None:
            self.factor_result = factor_result
        if factor_result_message is not None:
            self.factor_result_message = factor_result_message

    @property
    def embedded(self):
        """Gets the embedded of this VerifyUserFactorResponse.  # noqa: E501


        :return: The embedded of this VerifyUserFactorResponse.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._embedded

    @embedded.setter
    def embedded(self, embedded):
        """Sets the embedded of this VerifyUserFactorResponse.


        :param embedded: The embedded of this VerifyUserFactorResponse.  # noqa: E501
        :type: dict(str, object)
        """

        self._embedded = embedded

    @property
    def links(self):
        """Gets the links of this VerifyUserFactorResponse.  # noqa: E501


        :return: The links of this VerifyUserFactorResponse.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this VerifyUserFactorResponse.


        :param links: The links of this VerifyUserFactorResponse.  # noqa: E501
        :type: dict(str, object)
        """

        self._links = links

    @property
    def expires_at(self):
        """Gets the expires_at of this VerifyUserFactorResponse.  # noqa: E501


        :return: The expires_at of this VerifyUserFactorResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this VerifyUserFactorResponse.


        :param expires_at: The expires_at of this VerifyUserFactorResponse.  # noqa: E501
        :type: datetime
        """

        self._expires_at = expires_at

    @property
    def factor_result(self):
        """Gets the factor_result of this VerifyUserFactorResponse.  # noqa: E501


        :return: The factor_result of this VerifyUserFactorResponse.  # noqa: E501
        :rtype: str
        """
        return self._factor_result

    @factor_result.setter
    def factor_result(self, factor_result):
        """Sets the factor_result of this VerifyUserFactorResponse.


        :param factor_result: The factor_result of this VerifyUserFactorResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["SUCCESS", "EXPIRED", "CHALLENGE", "WAITING", "FAILED", "REJECTED", "TIMEOUT", "TIME_WINDOW_EXCEEDED", "PASSCODE_REPLAYED", "ERROR"]  # noqa: E501
        if factor_result not in allowed_values:
            raise ValueError(
                "Invalid value for `factor_result` ({0}), must be one of {1}"  # noqa: E501
                .format(factor_result, allowed_values)
            )

        self._factor_result = factor_result

    @property
    def factor_result_message(self):
        """Gets the factor_result_message of this VerifyUserFactorResponse.  # noqa: E501


        :return: The factor_result_message of this VerifyUserFactorResponse.  # noqa: E501
        :rtype: str
        """
        return self._factor_result_message

    @factor_result_message.setter
    def factor_result_message(self, factor_result_message):
        """Sets the factor_result_message of this VerifyUserFactorResponse.


        :param factor_result_message: The factor_result_message of this VerifyUserFactorResponse.  # noqa: E501
        :type: str
        """

        self._factor_result_message = factor_result_message

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
        if issubclass(VerifyUserFactorResponse, dict):
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
        if not isinstance(other, VerifyUserFactorResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
