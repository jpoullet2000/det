# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO
import pytest
from pytest_mock import mocker


from det.models.classification_defs_item import ClassificationDefsItem  # noqa: E501
from det.models.cluster import Cluster  # noqa: E501
from det.models.entity_defs_item import EntityDefsItem  # noqa: E501
from det.models.enum_defs_item import EnumDefsItem  # noqa: E501
from det.models.hdfs_path_item import HdfsPathItem  # noqa: E501
from det.models.process import Process  # noqa: E501
from det.models.hdfs_path_item_classification import HdfsPathItemClassification
from . import BaseTestCase


hdfs_path_item_classification = HdfsPathItemClassification(sg='s1',
                                                           cl='s1',
                                                           fb='s1',
                                                           retainable=315)


class TestDevelopersController(BaseTestCase):
    """DevelopersController integration test stubs"""

    def test_clusters_cluster_id_get(self):
        """Test case for clusters_cluster_id_get

        get cluster info
        """
        response = self.client.open(
            '/detapi/0.0.1/clusters/{cluster_id}'.format(cluster_id='cluster_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_clusters_cluster_id_services_get(self):
        """Test case for clusters_cluster_id_services_get

        get cluster services
        """
        response = self.client.open(
            '/detapi/0.0.1/clusters/{cluster_id}/services'.format(cluster_id='cluster_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_clusters_get(self):
        """Test case for clusters_get

        get cluster names
        """
        response = self.client.open(
            '/detapi/0.0.1/clusters',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_hdfs_path(self):
        """Test case for create_hdfs_path

        create hdfs_path
        """

        hdfsPath = HdfsPathItem(env='d0', app='myapp', classification=hdfs_path_item_classification)
        response = self.client.open(
            '/detapi/0.0.1/entity/hdfs_path',
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
            '/detapi/0.0.1/process',
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
            '/detapi/0.0.1/entity/hdfs_path/maintain',
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
        response = self.client.open(
            '/detapi/0.0.1/typedefs/classificationdefs',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_typedefs_entitydefs_get(self):
        """Test case for typedefs_entitydefs_get

        get entity defs
        """
        response = self.client.open(
            '/detapi/0.0.1/typedefs/entitydefs',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_typedefs_enumdefs_get(self):
        """Test case for typedefs_enumdefs_get

        get enum defs
        """
        response = self.client.open(
            '/detapi/0.0.1/typedefs/enumdefs',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
