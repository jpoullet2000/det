from __future__ import absolute_import

import pytest
import logging
from pytest_mock import mocker

from det.operators.atlas_entity_create import AtlasEntityCreateOperator
from det.exceptions import DETException
from det.operators.atlas_entity_create import atlas_client
from det.models.hdfs_path_item import HdfsPathItem


attributes = {'clusterName': 'bdlab', 'owner': 'username', 'description': 'Customer address', 'name': 'data_d0_app_workflowid_appfolder', 'qualifiedName': '/data/d0/app/workflowid/appfolder'}
classifications = ['PL_BILLING', 'CL_RT', 'SG_CONF']
entity_type = 'hdfs_path'
atlas_create_operator = AtlasEntityCreateOperator(attributes=attributes,
                                                       classifications=classifications
                                                       )
@pytest.fixture(scope='module')
def hdfs_path_item():
    item = HdfsPathItem(data_code='data',
                        env='d0',
                        delivery_ingestion='delivery')
    return(item)


class TestAtlasEntity():

    def test_validate_body(self):
        atlas_create_operator.validate_body()

        with pytest.raises(DETException) as e:
            logging.info('Creating Atlas "create entity operator" without qualified name variable') 
            bad_atlas_create_operator = AtlasEntityCreateOperator(attributes={'name': 'bad_entity'})
            bad_atlas_create_operator.validate_body()

    def test_body(self):
        assert 'qualifiedName' in atlas_create_operator.body
        assert 'CL_RT' in atlas_create_operator.body

    def test_atlas_entity_create(self, mocker):
        with mocker.patch.object(atlas_client, 'entity_post'):
            mocker.patch.object(atlas_client.entity_post, 'create', return_value={})
            atlas_create_operator.execute() 
            atlas_client.entity_post.create.assert_called_with(data=atlas_create_operator.body)


class TestHDFSCreateOperator():
    pass
