'''
Created on 2011-11-6

@author: ACER
'''
import  xml.dom
import  xml.dom.minidom
from testframe.TestSuite import *
sys.path.append( os.getcwd() + "../testcase" )
sys.path.append( os.getcwd() + "../testframe" )

class TestUseXml( ITestFixture ):
    def __init__( self ):
        ITestFixture.__init__( self )
        pass

    def setUp( self ):
        '''
        '''
        pass #print "testme setup"
    def tearDown( self ):
        pass#print "testme teardown"
    def testException( self ):
           assert 1 == 2, "testException"
           try:
                f = open( "d:\\pytest.log", "w" )
                print >> f, "testException open fal'"

                f.close()
           except Exception , e :
                print e

    def testMe( self ):
        try:
            f = open( "c:\\l.bin", "wb" )
            f.write( "ggg" )
            f.close()
        except Exception , e :
            print >> sys.stderr, e
            assert False, str( e )
    def testXml( self ):
        xdom = xml.dom.minidom.Document()
        root = xdom.createElement( "cfg" )
        xdom.appendChild( root )
        node = xdom.createElement( "ip" )
        textnode = xdom.createTextNode( "127.0.0.1" )
        node.appendChild( textnode )
        root.appendChild( node )

        print xdom.toprettyxml( "\t" )

def main():
       TestUseXml(). testXml()


