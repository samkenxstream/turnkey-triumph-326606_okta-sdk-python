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

class MDMEnrollmentPolicyRuleCondition(object):
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
        'block_non_safe_android': 'bool',
        'enrollment': 'str'
    }

    attribute_map = {
        'block_non_safe_android': 'blockNonSafeAndroid',
        'enrollment': 'enrollment'
    }

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, block_non_safe_android=None, enrollment=None):  # noqa: E501
        """MDMEnrollmentPolicyRuleCondition - a model defined in Swagger"""  # noqa: E501
        self._block_non_safe_android = None
        self._enrollment = None
        self.discriminator = None
        if block_non_safe_android is not None:
            self.block_non_safe_android = block_non_safe_android
        if enrollment is not None:
            self.enrollment = enrollment

    @property
    def block_non_safe_android(self):
        """Gets the block_non_safe_android of this MDMEnrollmentPolicyRuleCondition.  # noqa: E501


        :return: The block_non_safe_android of this MDMEnrollmentPolicyRuleCondition.  # noqa: E501
        :rtype: bool
        """
        return self._block_non_safe_android

    @block_non_safe_android.setter
    def block_non_safe_android(self, block_non_safe_android):
        """Sets the block_non_safe_android of this MDMEnrollmentPolicyRuleCondition.


        :param block_non_safe_android: The block_non_safe_android of this MDMEnrollmentPolicyRuleCondition.  # noqa: E501
        :type: bool
        """

        self._block_non_safe_android = block_non_safe_android

    @property
    def enrollment(self):
        """Gets the enrollment of this MDMEnrollmentPolicyRuleCondition.  # noqa: E501


        :return: The enrollment of this MDMEnrollmentPolicyRuleCondition.  # noqa: E501
        :rtype: str
        """
        return self._enrollment

    @enrollment.setter
    def enrollment(self, enrollment):
        """Sets the enrollment of this MDMEnrollmentPolicyRuleCondition.


        :param enrollment: The enrollment of this MDMEnrollmentPolicyRuleCondition.  # noqa: E501
        :type: str
        """
        allowed_values = ["OMM", "ANY_OR_NONE"]  # noqa: E501
        if enrollment not in allowed_values:
            raise ValueError(
                "Invalid value for `enrollment` ({0}), must be one of {1}"  # noqa: E501
                .format(enrollment, allowed_values)
            )

        self._enrollment = enrollment

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
        if issubclass(MDMEnrollmentPolicyRuleCondition, dict):
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
        if not isinstance(other, MDMEnrollmentPolicyRuleCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
