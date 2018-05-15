from det.app import AMBARI_CLIENT


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
     
    def get_clusters(self):
        """ Get clusters
        """
        clusters = []
        for cluster in self.ambari_client.clusters:
            clusters.append(cluster.cluster_name)
        return clusters

    def get_cluster_info(self, cluster_id):
        cluster_info = {}
        cluster = self.ambari_client.clusters(cluster_id)
        for field in cluster.fields:
            cluster_info[field] = getattr(cluster, field)
        return cluster_info

    def get_cluster_services(self, cluster_id):
        services = []
        for cluster_service in self.ambari_client.clusters(cluster_id).services:
            service = {}
            for field in cluster_service.fields:
                service[field] = getattr(cluster_service, field)
            services.append(service)
        return services

    def get_classification_defs(self):
        classifications = []
        for typedefs in self.ambari_client.typedefs:
            for classification_def in typedefs.classificationDefs:
                for field in classification_def.fields:
                    classification[field] = getattr(classification_def, field)
                    classifications.append(classification)
        return classifications
