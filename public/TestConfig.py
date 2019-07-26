'''
Created on 2012-4-2

@author: leijm
'''

import xml.dom
import xml.dom.minidom
from public.TestLog import testlog

class TestConfig:
    def __init__( self ):
        global CFGfile
        CFGfile = "config/pyserver.cfg.xml"
        pass

    def readCfg( self ):
        #xdom = xml.dom.minidom.Document()
        try:
            xdom = xml.dom.minidom.parse( CFGfile )
            root = xdom._get_documentElement()
            #doc = xml.dom.minidom.Document()
            #node = doc.createElement( "" )
            nodes = root.getElementsByTagName( "server" )
            serverinfo = ( nodes[0].getAttribute( "ip" ), \
                        nodes[0].getAttribute( "port" ) )
            return serverinfo
        except Exception , e :
            print e
            raise e
            return ( "127.0.0.1", "8888" )

    def writeCfg( self ):
            xdom = xml.dom.minidom.Document()
            root = xdom.createElement( "cfg" )
            xdom.appendChild( root )
            node = xdom.createElement( "server" )
            textnode = xdom.createTextNode( "127.0.0.1" )
            attr = xdom.createAttribute( "ip" )
            node.setAttribute( "ip", "127.0.0.1" )
            node.setAttribute( "port", "38888" )
            root.appendChild( node )
            print
            print xdom.toprettyxml( "\t" , "\n" , encoding = "utf-8" )
            file = open( "config/testleijm.cfg.xml", "w" )
            xdom.writexml( writer = file , newl = "\n", encoding = "utf-8" )
            testlog.log( "xdom.writexml :\n%s" , xdom.toprettyxml( "\t" , "\n" ) ).log( "end" )
            file.close()
