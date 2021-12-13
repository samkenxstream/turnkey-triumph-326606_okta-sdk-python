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

class LogSecurityContext(object):
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
        'as_number': 'int',
        'as_org': 'str',
        'domain': 'str',
        'is_proxy': 'bool',
        'isp': 'str'
    }

    attribute_map = {
        'as_number': 'asNumber',
        'as_org': 'asOrg',
        'domain': 'domain',
        'is_proxy': 'isProxy',
        'isp': 'isp'
    }

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, as_number=None, as_org=None, domain=None, is_proxy=None, isp=None):  # noqa: E501
        """LogSecurityContext - a model defined in Swagger"""  # noqa: E501
        self._as_number = None
        self._as_org = None
        self._domain = None
        self._is_proxy = None
        self._isp = None
        self.discriminator = None
        if as_number is not None:
            self.as_number = as_number
        if as_org is not None:
            self.as_org = as_org
        if domain is not None:
            self.domain = domain
        if is_proxy is not None:
            self.is_proxy = is_proxy
        if isp is not None:
            self.isp = isp

    @property
    def as_number(self):
        """Gets the as_number of this LogSecurityContext.  # noqa: E501


        :return: The as_number of this LogSecurityContext.  # noqa: E501
        :rtype: int
        """
        return self._as_number

    @as_number.setter
    def as_number(self, as_number):
        """Sets the as_number of this LogSecurityContext.


        :param as_number: The as_number of this LogSecurityContext.  # noqa: E501
        :type: int
        """

        self._as_number = as_number

    @property
    def as_org(self):
        """Gets the as_org of this LogSecurityContext.  # noqa: E501


        :return: The as_org of this LogSecurityContext.  # noqa: E501
        :rtype: str
        """
        return self._as_org

    @as_org.setter
    def as_org(self, as_org):
        """Sets the as_org of this LogSecurityContext.


        :param as_org: The as_org of this LogSecurityContext.  # noqa: E501
        :type: str
        """

        self._as_org = as_org

    @property
    def domain(self):
        """Gets the domain of this LogSecurityContext.  # noqa: E501


        :return: The domain of this LogSecurityContext.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this LogSecurityContext.


        :param domain: The domain of this LogSecurityContext.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def is_proxy(self):
        """Gets the is_proxy of this LogSecurityContext.  # noqa: E501


        :return: The is_proxy of this LogSecurityContext.  # noqa: E501
        :rtype: bool
        """
        return self._is_proxy

    @is_proxy.setter
    def is_proxy(self, is_proxy):
        """Sets the is_proxy of this LogSecurityContext.


        :param is_proxy: The is_proxy of this LogSecurityContext.  # noqa: E501
        :type: bool
        """

        self._is_proxy = is_proxy

    @property
    def isp(self):
        """Gets the isp of this LogSecurityContext.  # noqa: E501


        :return: The isp of this LogSecurityContext.  # noqa: E501
        :rtype: str
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        """Sets the isp of this LogSecurityContext.


        :param isp: The isp of this LogSecurityContext.  # noqa: E501
        :type: str
        """

        self._isp = isp

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
        if issubclass(LogSecurityContext, dict):
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
        if not isinstance(other, LogSecurityContext):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
