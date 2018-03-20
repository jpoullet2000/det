# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.security_governance_item import SecurityGovernanceItem  # noqa: F401,E501
from swagger_server import util


class HdfsPathItemClassification(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, sg=None):  # noqa: E501
        """HdfsPathItemClassification - a model defined in Swagger

        :param sg: The sg of this HdfsPathItemClassification.  # noqa: E501
        :type sg: SecurityGovernanceItem
        """
        self.swagger_types = {
            'sg': SecurityGovernanceItem
        }

        self.attribute_map = {
            'sg': 'sg'
        }

        self._sg = sg

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The HdfsPathItem_classification of this HdfsPathItemClassification.  # noqa: E501
        :rtype: HdfsPathItemClassification
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sg(self):
        """Gets the sg of this HdfsPathItemClassification.


        :return: The sg of this HdfsPathItemClassification.
        :rtype: SecurityGovernanceItem
        """
        return self._sg

    @sg.setter
    def sg(self, sg):
        """Sets the sg of this HdfsPathItemClassification.


        :param sg: The sg of this HdfsPathItemClassification.
        :type sg: SecurityGovernanceItem
        """

        self._sg = sg
