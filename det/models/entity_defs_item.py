# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from det.models.base_model_ import Model
from det.models.attribute_defs_item import AttributeDefsItem  # noqa: F401,E501
from det import util


class EntityDefsItem(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, category: str=None, name: str=None, description: str=None, type_version: str=None, attribute_defs: List[AttributeDefsItem]=None, super_types: List[str]=None):  # noqa: E501
        """EntityDefsItem - a model defined in Swagger

        :param category: The category of this EntityDefsItem.  # noqa: E501
        :type category: str
        :param name: The name of this EntityDefsItem.  # noqa: E501
        :type name: str
        :param description: The description of this EntityDefsItem.  # noqa: E501
        :type description: str
        :param type_version: The type_version of this EntityDefsItem.  # noqa: E501
        :type type_version: str
        :param attribute_defs: The attribute_defs of this EntityDefsItem.  # noqa: E501
        :type attribute_defs: List[AttributeDefsItem]
        :param super_types: The super_types of this EntityDefsItem.  # noqa: E501
        :type super_types: List[str]
        """
        self.swagger_types = {
            'category': str,
            'name': str,
            'description': str,
            'type_version': str,
            'attribute_defs': List[AttributeDefsItem],
            'super_types': List[str]
        }

        self.attribute_map = {
            'category': 'category',
            'name': 'name',
            'description': 'description',
            'type_version': 'typeVersion',
            'attribute_defs': 'attributeDefs',
            'super_types': 'superTypes'
        }

        self._category = category
        self._name = name
        self._description = description
        self._type_version = type_version
        self._attribute_defs = attribute_defs
        self._super_types = super_types

    @classmethod
    def from_dict(cls, dikt) -> 'EntityDefsItem':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EntityDefsItem of this EntityDefsItem.  # noqa: E501
        :rtype: EntityDefsItem
        """
        return util.deserialize_model(dikt, cls)

    @property
    def category(self) -> str:
        """Gets the category of this EntityDefsItem.


        :return: The category of this EntityDefsItem.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category: str):
        """Sets the category of this EntityDefsItem.


        :param category: The category of this EntityDefsItem.
        :type category: str
        """
        allowed_values = ["ENTITY"]  # noqa: E501
        if category not in allowed_values:
            raise ValueError(
                "Invalid value for `category` ({0}), must be one of {1}"
                .format(category, allowed_values)
            )

        self._category = category

    @property
    def name(self) -> str:
        """Gets the name of this EntityDefsItem.


        :return: The name of this EntityDefsItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this EntityDefsItem.


        :param name: The name of this EntityDefsItem.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self) -> str:
        """Gets the description of this EntityDefsItem.


        :return: The description of this EntityDefsItem.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this EntityDefsItem.


        :param description: The description of this EntityDefsItem.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def type_version(self) -> str:
        """Gets the type_version of this EntityDefsItem.


        :return: The type_version of this EntityDefsItem.
        :rtype: str
        """
        return self._type_version

    @type_version.setter
    def type_version(self, type_version: str):
        """Sets the type_version of this EntityDefsItem.


        :param type_version: The type_version of this EntityDefsItem.
        :type type_version: str
        """

        self._type_version = type_version

    @property
    def attribute_defs(self) -> List[AttributeDefsItem]:
        """Gets the attribute_defs of this EntityDefsItem.


        :return: The attribute_defs of this EntityDefsItem.
        :rtype: List[AttributeDefsItem]
        """
        return self._attribute_defs

    @attribute_defs.setter
    def attribute_defs(self, attribute_defs: List[AttributeDefsItem]):
        """Sets the attribute_defs of this EntityDefsItem.


        :param attribute_defs: The attribute_defs of this EntityDefsItem.
        :type attribute_defs: List[AttributeDefsItem]
        """

        self._attribute_defs = attribute_defs

    @property
    def super_types(self) -> List[str]:
        """Gets the super_types of this EntityDefsItem.


        :return: The super_types of this EntityDefsItem.
        :rtype: List[str]
        """
        return self._super_types

    @super_types.setter
    def super_types(self, super_types: List[str]):
        """Sets the super_types of this EntityDefsItem.


        :param super_types: The super_types of this EntityDefsItem.
        :type super_types: List[str]
        """

        self._super_types = super_types
