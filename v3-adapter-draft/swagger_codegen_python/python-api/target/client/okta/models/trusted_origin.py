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

class TrustedOrigin(object):
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
        'links': 'dict(str, object)',
        'created': 'datetime',
        'created_by': 'str',
        'id': 'str',
        'last_updated': 'datetime',
        'last_updated_by': 'str',
        'name': 'str',
        'origin': 'str',
        'scopes': 'list[Scope]',
        'status': 'str'
    }

    attribute_map = {
        'links': '_links',
        'created': 'created',
        'created_by': 'createdBy',
        'id': 'id',
        'last_updated': 'lastUpdated',
        'last_updated_by': 'lastUpdatedBy',
        'name': 'name',
        'origin': 'origin',
        'scopes': 'scopes',
        'status': 'status'
    }

    def __init__(self, config=None):
        if config is not None:
            config = {to_snake_case(key): value for key, value in config.items()}
            self.set_attributes(**config)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return cls(config=kwargs)

    def set_attributes(self, links=None, created=None, created_by=None, id=None, last_updated=None, last_updated_by=None, name=None, origin=None, scopes=None, status=None):  # noqa: E501
        """TrustedOrigin - a model defined in Swagger"""  # noqa: E501
        self._links = None
        self._created = None
        self._created_by = None
        self._id = None
        self._last_updated = None
        self._last_updated_by = None
        self._name = None
        self._origin = None
        self._scopes = None
        self._status = None
        self.discriminator = None
        if links is not None:
            self.links = links
        if created is not None:
            self.created = created
        if created_by is not None:
            self.created_by = created_by
        if id is not None:
            self.id = id
        if last_updated is not None:
            self.last_updated = last_updated
        if last_updated_by is not None:
            self.last_updated_by = last_updated_by
        if name is not None:
            self.name = name
        if origin is not None:
            self.origin = origin
        if scopes is not None:
            self.scopes = scopes
        if status is not None:
            self.status = status

    @property
    def links(self):
        """Gets the links of this TrustedOrigin.  # noqa: E501


        :return: The links of this TrustedOrigin.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this TrustedOrigin.


        :param links: The links of this TrustedOrigin.  # noqa: E501
        :type: dict(str, object)
        """

        self._links = links

    @property
    def created(self):
        """Gets the created of this TrustedOrigin.  # noqa: E501


        :return: The created of this TrustedOrigin.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this TrustedOrigin.


        :param created: The created of this TrustedOrigin.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def created_by(self):
        """Gets the created_by of this TrustedOrigin.  # noqa: E501


        :return: The created_by of this TrustedOrigin.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this TrustedOrigin.


        :param created_by: The created_by of this TrustedOrigin.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def id(self):
        """Gets the id of this TrustedOrigin.  # noqa: E501


        :return: The id of this TrustedOrigin.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TrustedOrigin.


        :param id: The id of this TrustedOrigin.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def last_updated(self):
        """Gets the last_updated of this TrustedOrigin.  # noqa: E501


        :return: The last_updated of this TrustedOrigin.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this TrustedOrigin.


        :param last_updated: The last_updated of this TrustedOrigin.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def last_updated_by(self):
        """Gets the last_updated_by of this TrustedOrigin.  # noqa: E501


        :return: The last_updated_by of this TrustedOrigin.  # noqa: E501
        :rtype: str
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, last_updated_by):
        """Sets the last_updated_by of this TrustedOrigin.


        :param last_updated_by: The last_updated_by of this TrustedOrigin.  # noqa: E501
        :type: str
        """

        self._last_updated_by = last_updated_by

    @property
    def name(self):
        """Gets the name of this TrustedOrigin.  # noqa: E501


        :return: The name of this TrustedOrigin.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TrustedOrigin.


        :param name: The name of this TrustedOrigin.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def origin(self):
        """Gets the origin of this TrustedOrigin.  # noqa: E501


        :return: The origin of this TrustedOrigin.  # noqa: E501
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this TrustedOrigin.


        :param origin: The origin of this TrustedOrigin.  # noqa: E501
        :type: str
        """

        self._origin = origin

    @property
    def scopes(self):
        """Gets the scopes of this TrustedOrigin.  # noqa: E501


        :return: The scopes of this TrustedOrigin.  # noqa: E501
        :rtype: list[Scope]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """Sets the scopes of this TrustedOrigin.


        :param scopes: The scopes of this TrustedOrigin.  # noqa: E501
        :type: list[Scope]
        """

        self._scopes = scopes

    @property
    def status(self):
        """Gets the status of this TrustedOrigin.  # noqa: E501


        :return: The status of this TrustedOrigin.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TrustedOrigin.


        :param status: The status of this TrustedOrigin.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(TrustedOrigin, dict):
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
        if not isinstance(other, TrustedOrigin):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
