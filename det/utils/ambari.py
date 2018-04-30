from det import AMBARI_CLIENT


class Ambari():
    """Utils to get info from the Ambari API 
    """
    def __init__(self, ambari_client=AMBARI_CLIENT):
        """
        """
        self.ambari_client = ambari_client

    def get_namenodes(self, cluster_name, service_name):
        """ Get the namenode from a given service, e.g. hdfs

        Args: 
           cluster_name(str): cluster name as retrieved by ambari
           service_name(str): cluster service (e.g. hdfs, hbase, ...)
        """
        namenodes = []
        for hc in self.ambari_client.clusters(cluster_name).services(service_name).components('NAMENODE').host_components:
            namenodes.append(hc.host_name)
        return(namenodes)
         
