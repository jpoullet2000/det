# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from det.models.base_model_ import Model
from det import util


class ElementDefsItem(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, value: str=None, ordinal: int=None):  # noqa: E501
        """ElementDefsItem - a model defined in Swagger

        :param value: The value of this ElementDefsItem.  # noqa: E501
        :type value: str
        :param ordinal: The ordinal of this ElementDefsItem.  # noqa: E501
        :type ordinal: int
        """
        self.swagger_types = {
            'value': str,
            'ordinal': int
        }

        self.attribute_map = {
            'value': 'value',
            'ordinal': 'ordinal'
        }

        self._value = value
        self._ordinal = ordinal

    @classmethod
    def from_dict(cls, dikt) -> 'ElementDefsItem':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ElementDefsItem of this ElementDefsItem.  # noqa: E501
        :rtype: ElementDefsItem
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value(self) -> str:
        """Gets the value of this ElementDefsItem.


        :return: The value of this ElementDefsItem.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """Sets the value of this ElementDefsItem.


        :param value: The value of this ElementDefsItem.
        :type value: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def ordinal(self) -> int:
        """Gets the ordinal of this ElementDefsItem.


        :return: The ordinal of this ElementDefsItem.
        :rtype: int
        """
        return self._ordinal

    @ordinal.setter
    def ordinal(self, ordinal: int):
        """Sets the ordinal of this ElementDefsItem.


        :param ordinal: The ordinal of this ElementDefsItem.
        :type ordinal: int
        """
        if ordinal is None:
            raise ValueError("Invalid value for `ordinal`, must not be `None`")  # noqa: E501

        self._ordinal = ordinal
