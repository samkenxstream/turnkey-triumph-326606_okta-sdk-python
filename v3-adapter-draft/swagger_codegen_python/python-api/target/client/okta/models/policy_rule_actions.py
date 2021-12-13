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

class PolicyRuleActions(object):
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
        'enroll': 'PolicyRuleActionsEnroll',
        'signon': 'OktaSignOnPolicyRuleSignonActions',
        'password_change': 'PasswordPolicyRuleAction',
        'self_service_password_reset': 'PasswordPolicyRuleAction',
        'self_service_unlock': 'PasswordPolicyRuleAction'
    }

    attribute_map = {
        'enroll': 'enroll',
        'signon': 'signon',
        'password_change': 'passwordChange',
        'self_service_password_reset': 'selfServicePasswordReset',
        'self_service_unlock': 'selfServiceUnlock'
    }

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, enroll=None, signon=None, password_change=None, self_service_password_reset=None, self_service_unlock=None):  # noqa: E501
        """PolicyRuleActions - a model defined in Swagger"""  # noqa: E501
        self._enroll = None
        self._signon = None
        self._password_change = None
        self._self_service_password_reset = None
        self._self_service_unlock = None
        self.discriminator = None
        if enroll is not None:
            self.enroll = enroll
        if signon is not None:
            self.signon = signon
        if password_change is not None:
            self.password_change = password_change
        if self_service_password_reset is not None:
            self.self_service_password_reset = self_service_password_reset
        if self_service_unlock is not None:
            self.self_service_unlock = self_service_unlock

    @property
    def enroll(self):
        """Gets the enroll of this PolicyRuleActions.  # noqa: E501


        :return: The enroll of this PolicyRuleActions.  # noqa: E501
        :rtype: PolicyRuleActionsEnroll
        """
        return self._enroll

    @enroll.setter
    def enroll(self, enroll):
        """Sets the enroll of this PolicyRuleActions.


        :param enroll: The enroll of this PolicyRuleActions.  # noqa: E501
        :type: PolicyRuleActionsEnroll
        """

        self._enroll = enroll

    @property
    def signon(self):
        """Gets the signon of this PolicyRuleActions.  # noqa: E501


        :return: The signon of this PolicyRuleActions.  # noqa: E501
        :rtype: OktaSignOnPolicyRuleSignonActions
        """
        return self._signon

    @signon.setter
    def signon(self, signon):
        """Sets the signon of this PolicyRuleActions.


        :param signon: The signon of this PolicyRuleActions.  # noqa: E501
        :type: OktaSignOnPolicyRuleSignonActions
        """

        self._signon = signon

    @property
    def password_change(self):
        """Gets the password_change of this PolicyRuleActions.  # noqa: E501


        :return: The password_change of this PolicyRuleActions.  # noqa: E501
        :rtype: PasswordPolicyRuleAction
        """
        return self._password_change

    @password_change.setter
    def password_change(self, password_change):
        """Sets the password_change of this PolicyRuleActions.


        :param password_change: The password_change of this PolicyRuleActions.  # noqa: E501
        :type: PasswordPolicyRuleAction
        """

        self._password_change = password_change

    @property
    def self_service_password_reset(self):
        """Gets the self_service_password_reset of this PolicyRuleActions.  # noqa: E501


        :return: The self_service_password_reset of this PolicyRuleActions.  # noqa: E501
        :rtype: PasswordPolicyRuleAction
        """
        return self._self_service_password_reset

    @self_service_password_reset.setter
    def self_service_password_reset(self, self_service_password_reset):
        """Sets the self_service_password_reset of this PolicyRuleActions.


        :param self_service_password_reset: The self_service_password_reset of this PolicyRuleActions.  # noqa: E501
        :type: PasswordPolicyRuleAction
        """

        self._self_service_password_reset = self_service_password_reset

    @property
    def self_service_unlock(self):
        """Gets the self_service_unlock of this PolicyRuleActions.  # noqa: E501


        :return: The self_service_unlock of this PolicyRuleActions.  # noqa: E501
        :rtype: PasswordPolicyRuleAction
        """
        return self._self_service_unlock

    @self_service_unlock.setter
    def self_service_unlock(self, self_service_unlock):
        """Sets the self_service_unlock of this PolicyRuleActions.


        :param self_service_unlock: The self_service_unlock of this PolicyRuleActions.  # noqa: E501
        :type: PasswordPolicyRuleAction
        """

        self._self_service_unlock = self_service_unlock

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
        if issubclass(PolicyRuleActions, dict):
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
        if not isinstance(other, PolicyRuleActions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
