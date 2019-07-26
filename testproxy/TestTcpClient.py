'''
Created on 2012-3-25

@author: leijm
'''
import socket
from public.TestConfig import TestConfig
import testproxy
import testproxy.TestTcpSrv
import os
import sys
from testframe.ITestFixture import *
ss = "111"
ss.upper()

class TestTcpClient( ITestFixture ):
    def __init__( self ):
        ITestFixture.__init__( self )

    def testClient( self ):
        tserver = testproxy.TestTcpSrv.TestPyServerThread()
        tserver.start()
        print sys.argv
        try:
            config = TestConfig()
            ip, port = config.readCfg()
            print
            print ip, port
        except Exception , e:
            print e
            return

        sock = socket.socket()
        try :
            from ctypes.wintypes import INT
            sock.connect( ( ip, int( port ) ) )
        except Exception , e :
            print e
            return

        sock.sendall( "test client" )
        #sock.sendall( "quit" )
        sock.close()
if __name__ == "__main__" :
    os.chdir( "../" )

    TestTcpClient().testClient()
