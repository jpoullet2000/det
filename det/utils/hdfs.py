import requests

class HDFS():
    """Utils for HDFS
    """
    def __init__(self, webhdfs_host, webhdfs_port=50070):
        self.webhdfs_host = webhdfs_host
        self.webhdfs_port = webhdfs_port

    def get_uri(self):
       params = (
                 ('qry', 'Hadoop:service=NameNode,name=NameNodeStatus'),
                )

       response = requests.get('http://{webhdfs_host}:{webhdfs_port}/jmx'
                               .format(webhdfs_host=self.webhdfs_host,
                                       webhdfs_port=self.webhdfs_port),
                               params=params)
       uri = response.json()['beans'][0].get('HostAndPort', '') 
       active = response.json()['beans'][0].get('State', '')
       return(uri if active else '')

