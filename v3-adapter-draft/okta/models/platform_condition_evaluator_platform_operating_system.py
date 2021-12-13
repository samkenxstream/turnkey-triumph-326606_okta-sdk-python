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

class PlatformConditionEvaluatorPlatformOperatingSystem(object):
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
        'expression': 'str',
        'type': 'str',
        'version': 'PlatformConditionEvaluatorPlatformOperatingSystemVersion'
    }

    attribute_map = {
        'expression': 'expression',
        'type': 'type',
        'version': 'version'
    }

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, expression=None, type=None, version=None):  # noqa: E501
        """PlatformConditionEvaluatorPlatformOperatingSystem - a model defined in Swagger"""  # noqa: E501
        self._expression = None
        self._type = None
        self._version = None
        self.discriminator = None
        if expression is not None:
            self.expression = expression
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version

    @property
    def expression(self):
        """Gets the expression of this PlatformConditionEvaluatorPlatformOperatingSystem.  # noqa: E501


        :return: The expression of this PlatformConditionEvaluatorPlatformOperatingSystem.  # noqa: E501
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this PlatformConditionEvaluatorPlatformOperatingSystem.


        :param expression: The expression of this PlatformConditionEvaluatorPlatformOperatingSystem.  # noqa: E501
        :type: str
        """

        self._expression = expression

    @property
    def type(self):
        """Gets the type of this PlatformConditionEvaluatorPlatformOperatingSystem.  # noqa: E501


        :return: The type of this PlatformConditionEvaluatorPlatformOperatingSystem.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PlatformConditionEvaluatorPlatformOperatingSystem.


        :param type: The type of this PlatformConditionEvaluatorPlatformOperatingSystem.  # noqa: E501
        :type: str
        """
        allowed_values = ["ANDROID", "IOS", "WINDOWS", "OSX", "OTHER", "ANY"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def version(self):
        """Gets the version of this PlatformConditionEvaluatorPlatformOperatingSystem.  # noqa: E501


        :return: The version of this PlatformConditionEvaluatorPlatformOperatingSystem.  # noqa: E501
        :rtype: PlatformConditionEvaluatorPlatformOperatingSystemVersion
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PlatformConditionEvaluatorPlatformOperatingSystem.


        :param version: The version of this PlatformConditionEvaluatorPlatformOperatingSystem.  # noqa: E501
        :type: PlatformConditionEvaluatorPlatformOperatingSystemVersion
        """

        self._version = version

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
        if issubclass(PlatformConditionEvaluatorPlatformOperatingSystem, dict):
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
        if not isinstance(other, PlatformConditionEvaluatorPlatformOperatingSystem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
