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

class IonForm(object):
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
        'accepts': 'str',
        'href': 'str',
        'method': 'str',
        'name': 'str',
        'produces': 'str',
        'refresh': 'int',
        'rel': 'list[str]',
        'relates_to': 'list[str]',
        'value': 'list[IonField]'
    }

    attribute_map = {
        'accepts': 'accepts',
        'href': 'href',
        'method': 'method',
        'name': 'name',
        'produces': 'produces',
        'refresh': 'refresh',
        'rel': 'rel',
        'relates_to': 'relatesTo',
        'value': 'value'
    }

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, accepts=None, href=None, method=None, name=None, produces=None, refresh=None, rel=None, relates_to=None, value=None):  # noqa: E501
        """IonForm - a model defined in Swagger"""  # noqa: E501
        self._accepts = None
        self._href = None
        self._method = None
        self._name = None
        self._produces = None
        self._refresh = None
        self._rel = None
        self._relates_to = None
        self._value = None
        self.discriminator = None
        if accepts is not None:
            self.accepts = accepts
        if href is not None:
            self.href = href
        if method is not None:
            self.method = method
        if name is not None:
            self.name = name
        if produces is not None:
            self.produces = produces
        if refresh is not None:
            self.refresh = refresh
        if rel is not None:
            self.rel = rel
        if relates_to is not None:
            self.relates_to = relates_to
        if value is not None:
            self.value = value

    @property
    def accepts(self):
        """Gets the accepts of this IonForm.  # noqa: E501


        :return: The accepts of this IonForm.  # noqa: E501
        :rtype: str
        """
        return self._accepts

    @accepts.setter
    def accepts(self, accepts):
        """Sets the accepts of this IonForm.


        :param accepts: The accepts of this IonForm.  # noqa: E501
        :type: str
        """

        self._accepts = accepts

    @property
    def href(self):
        """Gets the href of this IonForm.  # noqa: E501


        :return: The href of this IonForm.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this IonForm.


        :param href: The href of this IonForm.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def method(self):
        """Gets the method of this IonForm.  # noqa: E501


        :return: The method of this IonForm.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this IonForm.


        :param method: The method of this IonForm.  # noqa: E501
        :type: str
        """

        self._method = method

    @property
    def name(self):
        """Gets the name of this IonForm.  # noqa: E501


        :return: The name of this IonForm.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IonForm.


        :param name: The name of this IonForm.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def produces(self):
        """Gets the produces of this IonForm.  # noqa: E501


        :return: The produces of this IonForm.  # noqa: E501
        :rtype: str
        """
        return self._produces

    @produces.setter
    def produces(self, produces):
        """Sets the produces of this IonForm.


        :param produces: The produces of this IonForm.  # noqa: E501
        :type: str
        """

        self._produces = produces

    @property
    def refresh(self):
        """Gets the refresh of this IonForm.  # noqa: E501


        :return: The refresh of this IonForm.  # noqa: E501
        :rtype: int
        """
        return self._refresh

    @refresh.setter
    def refresh(self, refresh):
        """Sets the refresh of this IonForm.


        :param refresh: The refresh of this IonForm.  # noqa: E501
        :type: int
        """

        self._refresh = refresh

    @property
    def rel(self):
        """Gets the rel of this IonForm.  # noqa: E501


        :return: The rel of this IonForm.  # noqa: E501
        :rtype: list[str]
        """
        return self._rel

    @rel.setter
    def rel(self, rel):
        """Sets the rel of this IonForm.


        :param rel: The rel of this IonForm.  # noqa: E501
        :type: list[str]
        """

        self._rel = rel

    @property
    def relates_to(self):
        """Gets the relates_to of this IonForm.  # noqa: E501


        :return: The relates_to of this IonForm.  # noqa: E501
        :rtype: list[str]
        """
        return self._relates_to

    @relates_to.setter
    def relates_to(self, relates_to):
        """Sets the relates_to of this IonForm.


        :param relates_to: The relates_to of this IonForm.  # noqa: E501
        :type: list[str]
        """

        self._relates_to = relates_to

    @property
    def value(self):
        """Gets the value of this IonForm.  # noqa: E501


        :return: The value of this IonForm.  # noqa: E501
        :rtype: list[IonField]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this IonForm.


        :param value: The value of this IonForm.  # noqa: E501
        :type: list[IonField]
        """

        self._value = value

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
        if issubclass(IonForm, dict):
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
        if not isinstance(other, IonForm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
