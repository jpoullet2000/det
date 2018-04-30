import requests

class HDFS():
    """Utils for HDFS
    """
    def __init__(self, webhdfs_host, webhdfs_port=50070):
        self.webhdfs_host = webhdfs_host
        self.webhdfs_port = webhdfs_port
        self.webhdfs_uri = 'http://{}:{}'.format(webhdfs_host, webhdfs_port)

    def get_hdfs_namenode_info(self):
       params = (
                 ('qry', 'Hadoop:service=NameNode,name=NameNodeStatus'),
                )

       response = requests.get('http://{webhdfs_host}:{webhdfs_port}/jmx'
                               .format(webhdfs_host=self.webhdfs_host,
                                       webhdfs_port=self.webhdfs_port),
                               params=params)
       hdfs_namenode_host_and_port = response.json()['beans'][0].get('HostAndPort', '')
       hdfs_info = dict(
           hdfs_namenode_uri = 'hdfs://' + hdfs_namenode_host_and_port,
           hdfs_namenode_host = hdfs_namenode_host_and_port.split(':')[0],
           hdfs_namenode_port = hdfs_namenode_host_and_port.split(':')[1],
           )
       active = response.json()['beans'][0].get('State', '')
        
       return(hdfs_info if active else '')

