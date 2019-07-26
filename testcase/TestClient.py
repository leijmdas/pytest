'''
Created on 2012-3-25

@author: leijm
'''
import socket
from testframe.TestSuite import *
from testproxy.TestTcpSrv import TestPyServerThread
HOST, PORT = "localhost", 3884

class TestClient( ITestFixture ):

    def sendMsg( self, Msg = "test client" ):

        sock = socket.socket()
        try :
            sock.connect( ( HOST, PORT ) )
        except Exception , e :
            print e
        print "Client Send %s " % Msg
        sock.sendall( Msg )
        sock.close()

    def TtestClientSend( self ):
            t = TestPyServerThread()
            t.start()
            TestClient().sendMsg( "Test Client" )
            TestClient().sendMsg( "quit" )
