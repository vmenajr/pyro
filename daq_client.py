import Pyro4

def business_as_usual():
    print 'doing business'

def stop_doing_stuff():
    print "I have been disabled so can't continue working"


metadata = Pyro4.Proxy('PYRONAME:shared_metadata:localhost')
cluster_name = metadata.cluster_name()

if not metadata.am_i_disabled('node1'):
    business_as_usual()
else:
    stop_doing_stuff()
