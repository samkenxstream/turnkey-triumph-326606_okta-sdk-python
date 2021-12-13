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

class AuthorizationServerPolicyRuleConditions(object):
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
        'people': 'PolicyPeopleCondition',
        'clients': 'ClientPolicyCondition',
        'grant_types': 'GrantTypePolicyRuleCondition',
        'scopes': 'OAuth2ScopesMediationPolicyRuleCondition'
    }

    attribute_map = {
        'people': 'people',
        'clients': 'clients',
        'grant_types': 'grantTypes',
        'scopes': 'scopes'
    }

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, people=None, clients=None, grant_types=None, scopes=None):  # noqa: E501
        """AuthorizationServerPolicyRuleConditions - a model defined in Swagger"""  # noqa: E501
        self._people = None
        self._clients = None
        self._grant_types = None
        self._scopes = None
        self.discriminator = None
        if people is not None:
            self.people = people
        if clients is not None:
            self.clients = clients
        if grant_types is not None:
            self.grant_types = grant_types
        if scopes is not None:
            self.scopes = scopes

    @property
    def people(self):
        """Gets the people of this AuthorizationServerPolicyRuleConditions.  # noqa: E501


        :return: The people of this AuthorizationServerPolicyRuleConditions.  # noqa: E501
        :rtype: PolicyPeopleCondition
        """
        return self._people

    @people.setter
    def people(self, people):
        """Sets the people of this AuthorizationServerPolicyRuleConditions.


        :param people: The people of this AuthorizationServerPolicyRuleConditions.  # noqa: E501
        :type: PolicyPeopleCondition
        """

        self._people = people

    @property
    def clients(self):
        """Gets the clients of this AuthorizationServerPolicyRuleConditions.  # noqa: E501


        :return: The clients of this AuthorizationServerPolicyRuleConditions.  # noqa: E501
        :rtype: ClientPolicyCondition
        """
        return self._clients

    @clients.setter
    def clients(self, clients):
        """Sets the clients of this AuthorizationServerPolicyRuleConditions.


        :param clients: The clients of this AuthorizationServerPolicyRuleConditions.  # noqa: E501
        :type: ClientPolicyCondition
        """

        self._clients = clients

    @property
    def grant_types(self):
        """Gets the grant_types of this AuthorizationServerPolicyRuleConditions.  # noqa: E501


        :return: The grant_types of this AuthorizationServerPolicyRuleConditions.  # noqa: E501
        :rtype: GrantTypePolicyRuleCondition
        """
        return self._grant_types

    @grant_types.setter
    def grant_types(self, grant_types):
        """Sets the grant_types of this AuthorizationServerPolicyRuleConditions.


        :param grant_types: The grant_types of this AuthorizationServerPolicyRuleConditions.  # noqa: E501
        :type: GrantTypePolicyRuleCondition
        """

        self._grant_types = grant_types

    @property
    def scopes(self):
        """Gets the scopes of this AuthorizationServerPolicyRuleConditions.  # noqa: E501


        :return: The scopes of this AuthorizationServerPolicyRuleConditions.  # noqa: E501
        :rtype: OAuth2ScopesMediationPolicyRuleCondition
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """Sets the scopes of this AuthorizationServerPolicyRuleConditions.


        :param scopes: The scopes of this AuthorizationServerPolicyRuleConditions.  # noqa: E501
        :type: OAuth2ScopesMediationPolicyRuleCondition
        """

        self._scopes = scopes

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
        if issubclass(AuthorizationServerPolicyRuleConditions, dict):
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
        if not isinstance(other, AuthorizationServerPolicyRuleConditions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
