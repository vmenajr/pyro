import random
import Pyro4

class Metadata(object):

    def __init__(self, name, site_id, role='enterprise'):
        self._cluster_name = name
        self._site_id = site_id
        self._cluster_role = role

    def _node_is_disabled(self, node_id):
        # lookup node disabled status.
        return random.choice([True, False])

    def cluster_name(self):
        return self._cluster_name

    def site_id(self):
        return self._site_id

    def cluster_role(self):
        return self._cluster_role

    def am_i_disabled(self, node_id):
        return self._node_is_disabled(node_id)

    #... Additional operations as needed by your specific situation.

def main():
    host = 'localhost'
    ns = Pyro4.locateNS(host=host)
    metadata = Metadata(name='Vick', site_id='0')
    daemon = Pyro4.Daemon()
    metadata_uri = daemon.register(metadata)
    ns.register(
        name='shared_metadata:{host}'.format(host=host),
        uri=metadata_uri
    )
    daemon.requestLoop()

if __name__ == '__main__':
    main()
