# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from det.models.base_model_ import Model
from det.models.competition_law_item import CompetitionLawItem  # noqa: F401,E501
from det.models.privacy_law_item import PrivacyLawItem  # noqa: F401,E501
from det.models.retainable import Retainable  # noqa: F401,E501
from det.models.security_governance_item import SecurityGovernanceItem  # noqa: F401,E501
from det import util


class HdfsPathItemClassification(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, sg: SecurityGovernanceItem=None, cl: CompetitionLawItem=None, pl: PrivacyLawItem=None, retainable: Retainable=None):  # noqa: E501
        """HdfsPathItemClassification - a model defined in Swagger

        :param sg: The sg of this HdfsPathItemClassification.  # noqa: E501
        :type sg: SecurityGovernanceItem
        :param cl: The cl of this HdfsPathItemClassification.  # noqa: E501
        :type cl: CompetitionLawItem
        :param pl: The pl of this HdfsPathItemClassification.  # noqa: E501
        :type pl: PrivacyLawItem
        :param retainable: The retainable of this HdfsPathItemClassification.  # noqa: E501
        :type retainable: Retainable
        """
        self.swagger_types = {
            'sg': SecurityGovernanceItem,
            'cl': CompetitionLawItem,
            'pl': PrivacyLawItem,
            'retainable': Retainable
        }

        self.attribute_map = {
            'sg': 'sg',
            'cl': 'cl',
            'pl': 'pl',
            'retainable': 'Retainable'
        }

        self._sg = sg
        self._cl = cl
        self._pl = pl
        self._retainable = retainable

    @classmethod
    def from_dict(cls, dikt) -> 'HdfsPathItemClassification':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The HdfsPathItem_classification of this HdfsPathItemClassification.  # noqa: E501
        :rtype: HdfsPathItemClassification
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sg(self) -> SecurityGovernanceItem:
        """Gets the sg of this HdfsPathItemClassification.


        :return: The sg of this HdfsPathItemClassification.
        :rtype: SecurityGovernanceItem
        """
        return self._sg

    @sg.setter
    def sg(self, sg: SecurityGovernanceItem):
        """Sets the sg of this HdfsPathItemClassification.


        :param sg: The sg of this HdfsPathItemClassification.
        :type sg: SecurityGovernanceItem
        """

        self._sg = sg

    @property
    def cl(self) -> CompetitionLawItem:
        """Gets the cl of this HdfsPathItemClassification.


        :return: The cl of this HdfsPathItemClassification.
        :rtype: CompetitionLawItem
        """
        return self._cl

    @cl.setter
    def cl(self, cl: CompetitionLawItem):
        """Sets the cl of this HdfsPathItemClassification.


        :param cl: The cl of this HdfsPathItemClassification.
        :type cl: CompetitionLawItem
        """

        self._cl = cl

    @property
    def pl(self) -> PrivacyLawItem:
        """Gets the pl of this HdfsPathItemClassification.


        :return: The pl of this HdfsPathItemClassification.
        :rtype: PrivacyLawItem
        """
        return self._pl

    @pl.setter
    def pl(self, pl: PrivacyLawItem):
        """Sets the pl of this HdfsPathItemClassification.


        :param pl: The pl of this HdfsPathItemClassification.
        :type pl: PrivacyLawItem
        """

        self._pl = pl

    @property
    def retainable(self) -> Retainable:
        """Gets the retainable of this HdfsPathItemClassification.


        :return: The retainable of this HdfsPathItemClassification.
        :rtype: Retainable
        """
        return self._retainable

    @retainable.setter
    def retainable(self, retainable: Retainable):
        """Sets the retainable of this HdfsPathItemClassification.


        :param retainable: The retainable of this HdfsPathItemClassification.
        :type retainable: Retainable
        """

        self._retainable = retainable
