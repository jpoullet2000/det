# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO
from unittest.mock import Mock

from det.models.classification_defs_item import ClassificationDefsItem  # noqa: E501
from det.models.cluster import Cluster  # noqa: E501
from det.models.entity_defs_item import EntityDefsItem  # noqa: E501
from det.models.enum_defs_item import EnumDefsItem  # noqa: E501
from det.models.hdfs_path_item import HdfsPathItem  # noqa: E501
from det.models.process import Process  # noqa: E501
from det.models.hdfs_path_item_classification import HdfsPathItemClassification
from det.operators.hdfspath_create_operator import HdfsPathCreateOperator
from det import __version__
from det.utils.ambari import Ambari
from det.utils.atlas import Atlas
from . import BaseTestCase



hdfs_path_item_classification = HdfsPathItemClassification(sg='SG_CONF',
                                                           cl='CL_RT',
                                                           pl='PL_HEALTH',
                                                           retainable={'retentionPeriod': 315})


class TestDevelopersController(BaseTestCase):
    """DevelopersController integration test stubs"""

    def test_clusters_cluster_name_get(self):
        """Test case for clusters_cluster_name_get

        get cluster info
        """
        MockAmbari = Ambari
        Ambari.get_cluster_info = Mock(return_value={'cluster_name': 'cluster_name'})
        response = self.client.open(
            '/detapi/{version}/clusters/{cluster_name}'.format(version=__version__, 
                                                             cluster_name='cluster_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_clusters_cluster_name_services_get(self):
        """Test case for clusters_cluster_name_services_get

        get cluster services
        """
        MockAmbari = Ambari
        Ambari.get_cluster_services = Mock(return_value={'service_name': 'HDFS'})
        response = self.client.open(
            '/detapi/{version}/clusters/{cluster_name}/services'.format(version=__version__,
                                                                      cluster_name='cluster_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_clusters_get(self):
        """Test case for clusters_get

        get cluster names
        """
        MockAmbari = Ambari
        Ambari.get_clusters = Mock(return_value=['cluster_name'])
        response = self.client.open(
            '/detapi/{version}/clusters'.format(version=__version__),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_hdfs_path(self):
        """Test case for create_hdfs_path

        create hdfs_path
        """

        hdfsPath = HdfsPathItem(env='d0', app='myapp', classification=hdfs_path_item_classification)
        MockHdfsCreateOperator = HdfsPathCreateOperator
        MockHdfsCreateOperator.execute = Mock(return_value=False)
        response = self.client.open(
            '/detapi/{version}/entity/hdfs_path'.format(version=__version__),
            method='POST',
            data=json.dumps(hdfsPath),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_process(self):
        """Test case for create_process

        Create process
        """
        process = Process()
        response = self.client.open(
            '/detapi/{version}/process'.format(version=__version__),
            method='POST',
            data=json.dumps(process),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_hdfs_maintenance(self):
        """Test case for hdfs_maintenance

        Maintenance of hdfs_path
        """
        hdfsPath = HdfsPathItem(env='d0', app='myapp', classification=hdfs_path_item_classification)
        query_string = [('HdfsMaintenanceService', 'purge')]
        response = self.client.open(
            '/detapi/{version}/entity/hdfs_path/maintain'.format(version=__version__),
            method='POST',
            data=json.dumps(hdfsPath),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_typedefs_classificationdefs_get(self):
        """Test case for typedefs_classificationdefs_get

        get classification defs
        """
        MockAtlas = Atlas
        Atlas.get_classification_defs = Mock(return_value=[{'category': 'CLASSIFICATION'}])
        response = self.client.open(
            '/detapi/{version}/typedefs/classificationdefs'.format(version=__version__),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_typedefs_entitydefs_get(self):
        """Test case for typedefs_entitydefs_get

        get entity defs
        """
        MockAtlas = Atlas
        Atlas.get_entity_defs = Mock(return_value=[{'category': 'ENTITY'}])
        response = self.client.open(
            '/detapi/{version}/typedefs/entitydefs'.format(version=__version__),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_typedefs_enumdefs_get(self):
        """Test case for typedefs_enumdefs_get

        get enum defs
        """
        MockAtlas = Atlas
        Atlas.get_enum_defs = Mock(return_value=[{'category': 'ENUM'}])
        response = self.client.open(
            '/detapi/{version}/typedefs/enumdefs'.format(version=__version__),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
