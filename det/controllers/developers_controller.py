import connexion
import six

from det.models.classification_defs_item import ClassificationDefsItem  # noqa: E501
from det.models.cluster import Cluster  # noqa: E501
from det.models.entity_defs_item import EntityDefsItem  # noqa: E501
from det.models.enum_defs_item import EnumDefsItem  # noqa: E501
from det.models.hdfs_path_item import HdfsPathItem  # noqa: E501
from det.models.process import Process  # noqa: E501
from det import util
from det.utils.security import token_required

def clusters_cluster_name_get(cluster_name):  # noqa: E501
    """get cluster info

    Get the cluster info  # noqa: E501

    :param cluster_name: cluster name
    :type cluster_name: str

    :rtype: List[Cluster]
    """
    from det.utils.ambari import Ambari
    cluster_info = Ambari().get_cluster_info(cluster_name)
    return cluster_info


def clusters_cluster_name_services_get(cluster_name):  # noqa: E501
    """get cluster services

    Get the services from the specified cluster  # noqa: E501

    :param cluster_name: cluster identifier
    :type cluster_name: str

    :rtype: List[Cluster]
    """
    from det.utils.ambari import Ambari
    cluster_services = Ambari().get_cluster_services(cluster_name)
    return cluster_services


def clusters_get():  # noqa: E501
    """get cluster names

    Get the cluster names  # noqa: E501


    :rtype: List[Cluster]
    """
    from det.utils.ambari import Ambari
    clusters = Ambari().get_clusters()
    return clusters

@token_required
def create_hdfs_path(hdfsPath):  # noqa: E501
    """create hdfs_path

    Add hdfs path  # noqa: E501

    :param hdfsPath: Hdfs path to add
    :type hdfsPath: dict | bytes

    :rtype: None
    """
    from det.operators.hdfspath_create_operator import HdfsPathCreateOperator
    if connexion.request.is_json:
        hdfsPath = HdfsPathItem.from_dict(connexion.request.get_json())  # noqa: E501
    return HdfsPathCreateOperator(hdfsPath).execute() 

def create_process(process=None):  # noqa: E501
    """Create process

    Maintenance of hdfs_path - archiving/compressing/purging  # noqa: E501

    :param process: Create process
    :type process: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        process = Process.from_dict(connexion.request.get_json())  # noqa: E501
    return 'Not yet implemented'


def hdfs_maintenance(hdfsPath, HdfsMaintenanceService):  # noqa: E501
    """Maintenance of hdfs_path

    Maintenance of hdfs_path - archiving/compressing/purging  # noqa: E501

    :param hdfsPath: Hdfs path to maintain
    :type hdfsPath: dict | bytes
    :param HdfsMaintenanceService: all/archive/purge/compress
    :type HdfsMaintenanceService: str

    :rtype: None
    """
    if connexion.request.is_json:
        hdfsPath = HdfsPathItem.from_dict(connexion.request.get_json())  # noqa: E501
    return 'Not yet implemented'


def typedefs_classificationdefs_get():  # noqa: E501
    """get classification defs

    Get the classification or tag definitions  # noqa: E501


    :rtype: List[ClassificationDefsItem]
    """
    from det.utils.atlas import Atlas
    classification_defs = Atlas().get_classification_defs()
    return classification_defs


def typedefs_entitydefs_get():  # noqa: E501
    """get entity defs

    Get the entity definitions  # noqa: E501


    :rtype: List[EntityDefsItem]
    """
    from det.utils.atlas import Atlas
    entity_defs = Atlas().get_entity_defs()
    return entity_defs


def typedefs_enumdefs_get():  # noqa: E501
    """get enum defs

    Get the enum definitions  # noqa: E501


    :rtype: List[EnumDefsItem]
    """
    from det.utils.atlas import Atlas
    enum_defs = Atlas().get_enum_defs()
    return enum_defs
