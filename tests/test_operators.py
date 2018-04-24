from __future__ import absolute_import

import pytest
import logging
from pytest_mock import mocker

from det.operators.atlas_entity_create import AtlasEntityCreateOperator
from det.operators.hdfspath_create_operator import HdfsPathCreateOperator
from det.exceptions import DETException
from det.operators.atlas_entity_create import atlas_client
from det.models.hdfs_path_item import HdfsPathItem
from det.cli import hdfs_client
import det.operators.hdfspath_create_operator

ATTRIBUTES = {'clusterName': 'bdlab',
              'owner': 'username',
              'description': 'Customer address',
              'name': 'data_d0_app_workflowid_appfolder',
              'qualifiedName': '/data/d0/app/workflowid/appfolder'}
CLASSIFICATIONS = ['PL_BILLING', 'CL_RT', 'SG_CONF']
ENTITY_TYPE = 'hdfs_path'
ATLAS_CREATE_OPERATOR = AtlasEntityCreateOperator(attributes=ATTRIBUTES,
                                                  classifications=CLASSIFICATIONS
                                                 )
@pytest.fixture(scope='module',
                params=[('data', 'delivery', None),
                        ('data', 'ingestion', None),
                        ('data', 'ingestion', 'subfolder1/subfolder2'),]
               )
def hdfs_path_item(request):
    item = HdfsPathItem(data_code=request.param[0],
                        env='d0',
                        app='myapp',
                        delivery_ingestion=request.param[1],
                        subfolder=request.param[2])
    return item


class TestAtlasEntity():

    def test_validate_body(self):
        ATLAS_CREATE_OPERATOR.validate_body()

        with pytest.raises(DETException) as e:
            logging.info('Creating Atlas "create entity operator" without qualified name variable') 
            bad_atlas_create_operator = AtlasEntityCreateOperator(attributes={'name': 'bad_entity'})
            bad_atlas_create_operator.validate_body()

    def test_body(self):
        assert 'qualifiedName' in ATLAS_CREATE_OPERATOR.body
        assert 'CL_RT' in ATLAS_CREATE_OPERATOR.body

    def test_atlas_entity_create(self, mocker):
        with mocker.patch.object(atlas_client, 'entity_post'):
            mocker.patch.object(atlas_client.entity_post, 'create', return_value={})
            ATLAS_CREATE_OPERATOR.execute() 
            atlas_client.entity_post.create.assert_called_with(data=ATLAS_CREATE_OPERATOR.body)


class TestHDFSCreateOperator():
    def test_hdfs_path(self, hdfs_path_item):
        hdfspath_create_operator = HdfsPathCreateOperator(hdfs_path_item=hdfs_path_item)
        assert hdfs_path_item.data_code in hdfspath_create_operator.hdfs_path
        assert 'd0' in hdfspath_create_operator.hdfs_path
        if hdfs_path_item.subfolder:
            assert hdfs_path_item.subfolder in hdfspath_create_operator.hdfs_path

    def test_get_conn(self, mocker, hdfs_path_item):
        mocker.patch.object(hdfs_client, 'get_uri', return_value='hdfs://localhost:50070')
        mocker.patch.object(det.operators.hdfspath_create_operator, 'InsecureClient') 
        hdfspath_create_operator = HdfsPathCreateOperator(hdfs_path_item=hdfs_path_item)
        client = hdfspath_create_operator.get_conn()

    def test_create_hdfs_folder(self, mocker, hdfs_path_item):
        mocker.patch.object(det.operators.hdfspath_create_operator, 'InsecureClient') 
        hdfs_insecure_client = det.operators.hdfspath_create_operator.InsecureClient('hdfs://localhost:50070')
        det.operators.hdfspath_create_operator.InsecureClient.return_value = hdfs_insecure_client
        mocker.patch.object(hdfs_insecure_client, 'makedirs')
        hdfspath_create_operator = HdfsPathCreateOperator(hdfs_path_item=hdfs_path_item)
        hdfspath_create_operator.create_hdfs_folder(hdfs_insecure_client)

    def test_delete_hdfs_folder(self, mocker, hdfs_path_item):
        mocker.patch.object(det.operators.hdfspath_create_operator, 'InsecureClient') 
        hdfs_insecure_client = det.operators.hdfspath_create_operator.InsecureClient('hdfs://localhost:50070')
        det.operators.hdfspath_create_operator.InsecureClient.return_value = hdfs_insecure_client
        mocker.patch.object(hdfs_insecure_client, 'delete')
        hdfspath_create_operator = HdfsPathCreateOperator(hdfs_path_item=hdfs_path_item)
        hdfspath_create_operator.delete_hdfs_folder(hdfs_insecure_client)
         

    def test_create_atlas_hdfs_path(self, mocker, hdfs_path_item):
        mocker.patch.object(det.operators.hdfspath_create_operator, 'AtlasEntityCreateOperator')
        atlas_entity_create_operator = det.operators.atlas_entity_create.AtlasEntityCreateOperator(attributes={}, classifications=[])
        
        mocker.patch.object(det.operators.hdfspath_create_operator, 'InsecureClient') 
        det.operators.atlas_entity_create.AtlasEntityCreateOperator.return_value = atlas_entity_create_operator
        hdfs_insecure_client = det.operators.hdfspath_create_operator.InsecureClient('hdfs://localhost:50070')
        hdfspath_create_operator = HdfsPathCreateOperator(hdfs_path_item=hdfs_path_item)
        hdfspath_create_operator.create_atlas_hdfs_path(hdfs_insecure_client)
