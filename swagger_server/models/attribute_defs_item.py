# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class AttributeDefsItem(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, name=None, type_name=None, is_optional=None, cardinality=None, values_min_count=None, values_max_count=None, is_unique=None, is_indexable=None):  # noqa: E501
        """AttributeDefsItem - a model defined in Swagger

        :param name: The name of this AttributeDefsItem.  # noqa: E501
        :type name: str
        :param type_name: The type_name of this AttributeDefsItem.  # noqa: E501
        :type type_name: str
        :param is_optional: The is_optional of this AttributeDefsItem.  # noqa: E501
        :type is_optional: bool
        :param cardinality: The cardinality of this AttributeDefsItem.  # noqa: E501
        :type cardinality: str
        :param values_min_count: The values_min_count of this AttributeDefsItem.  # noqa: E501
        :type values_min_count: int
        :param values_max_count: The values_max_count of this AttributeDefsItem.  # noqa: E501
        :type values_max_count: int
        :param is_unique: The is_unique of this AttributeDefsItem.  # noqa: E501
        :type is_unique: bool
        :param is_indexable: The is_indexable of this AttributeDefsItem.  # noqa: E501
        :type is_indexable: bool
        """
        self.swagger_types = {
            'name': str,
            'type_name': str,
            'is_optional': bool,
            'cardinality': str,
            'values_min_count': int,
            'values_max_count': int,
            'is_unique': bool,
            'is_indexable': bool
        }

        self.attribute_map = {
            'name': 'name',
            'type_name': 'typeName',
            'is_optional': 'isOptional',
            'cardinality': 'cardinality',
            'values_min_count': 'valuesMinCount',
            'values_max_count': 'valuesMaxCount',
            'is_unique': 'isUnique',
            'is_indexable': 'isIndexable'
        }

        self._name = name
        self._type_name = type_name
        self._is_optional = is_optional
        self._cardinality = cardinality
        self._values_min_count = values_min_count
        self._values_max_count = values_max_count
        self._is_unique = is_unique
        self._is_indexable = is_indexable

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AttributeDefsItem of this AttributeDefsItem.  # noqa: E501
        :rtype: AttributeDefsItem
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this AttributeDefsItem.


        :return: The name of this AttributeDefsItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AttributeDefsItem.


        :param name: The name of this AttributeDefsItem.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type_name(self):
        """Gets the type_name of this AttributeDefsItem.


        :return: The type_name of this AttributeDefsItem.
        :rtype: str
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name):
        """Sets the type_name of this AttributeDefsItem.


        :param type_name: The type_name of this AttributeDefsItem.
        :type type_name: str
        """
        if type_name is None:
            raise ValueError("Invalid value for `type_name`, must not be `None`")  # noqa: E501

        self._type_name = type_name

    @property
    def is_optional(self):
        """Gets the is_optional of this AttributeDefsItem.


        :return: The is_optional of this AttributeDefsItem.
        :rtype: bool
        """
        return self._is_optional

    @is_optional.setter
    def is_optional(self, is_optional):
        """Sets the is_optional of this AttributeDefsItem.


        :param is_optional: The is_optional of this AttributeDefsItem.
        :type is_optional: bool
        """

        self._is_optional = is_optional

    @property
    def cardinality(self):
        """Gets the cardinality of this AttributeDefsItem.


        :return: The cardinality of this AttributeDefsItem.
        :rtype: str
        """
        return self._cardinality

    @cardinality.setter
    def cardinality(self, cardinality):
        """Sets the cardinality of this AttributeDefsItem.


        :param cardinality: The cardinality of this AttributeDefsItem.
        :type cardinality: str
        """

        self._cardinality = cardinality

    @property
    def values_min_count(self):
        """Gets the values_min_count of this AttributeDefsItem.


        :return: The values_min_count of this AttributeDefsItem.
        :rtype: int
        """
        return self._values_min_count

    @values_min_count.setter
    def values_min_count(self, values_min_count):
        """Sets the values_min_count of this AttributeDefsItem.


        :param values_min_count: The values_min_count of this AttributeDefsItem.
        :type values_min_count: int
        """

        self._values_min_count = values_min_count

    @property
    def values_max_count(self):
        """Gets the values_max_count of this AttributeDefsItem.


        :return: The values_max_count of this AttributeDefsItem.
        :rtype: int
        """
        return self._values_max_count

    @values_max_count.setter
    def values_max_count(self, values_max_count):
        """Sets the values_max_count of this AttributeDefsItem.


        :param values_max_count: The values_max_count of this AttributeDefsItem.
        :type values_max_count: int
        """

        self._values_max_count = values_max_count

    @property
    def is_unique(self):
        """Gets the is_unique of this AttributeDefsItem.


        :return: The is_unique of this AttributeDefsItem.
        :rtype: bool
        """
        return self._is_unique

    @is_unique.setter
    def is_unique(self, is_unique):
        """Sets the is_unique of this AttributeDefsItem.


        :param is_unique: The is_unique of this AttributeDefsItem.
        :type is_unique: bool
        """

        self._is_unique = is_unique

    @property
    def is_indexable(self):
        """Gets the is_indexable of this AttributeDefsItem.


        :return: The is_indexable of this AttributeDefsItem.
        :rtype: bool
        """
        return self._is_indexable

    @is_indexable.setter
    def is_indexable(self, is_indexable):
        """Sets the is_indexable of this AttributeDefsItem.


        :param is_indexable: The is_indexable of this AttributeDefsItem.
        :type is_indexable: bool
        """

        self._is_indexable = is_indexable
