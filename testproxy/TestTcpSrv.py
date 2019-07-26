'''
Created on 2011-11-2

@author: ACER
'''

import glob, os, sys, struct
from  testframe.TestSuite import *
from  testframe.ByteBuffer import *

import  threading, SocketServer
import socket
from public.TestConfig import TestConfig



class MyTCPHandler( SocketServer.BaseRequestHandler ):
        global  HOST, PORT
        HOST, PORT = "localhost", 3284
        BUFFER_SIZE = 4096
        def handle( self ):
                #print "handle"
                while True:
                        #get input with wait if no data
                        data = self.request.recv( self.BUFFER_SIZE )

                        if ( data == "" ):
                                #print "break "
                                ##self.__server__.shutdown()
                                break
                        if ( data.strip() == "quit" ):
                                print "__server__ receive quit and shutdown!"
                                testlog.log ( "__server__ receive quit and shutdown!" )

                                self.server.shutdown()
                                break
                        #suspect many more data (try to get all - without stop if no data)
                        print >> sys.stdout, "tcp __server__ receive from %s:\t %s " % ( self.client_address, data.strip() )
                        testlog.log ( "tcp __server__ receive from %s:\t %s " , self.client_address, data.strip() )

class TestPyServerThread( threading.Thread ):
    def __init__( self ):
            self.server = None
            threading.Thread.__init__( self )

    def get_server( self ):
        return self.server


    def run( self ):
             import random
             r = random.randint( 1, 22 )
             HOST, PORT = TestConfig().readCfg()

             testlog.log( "Server HOST=%s, PORT=%s", HOST, PORT )
             try:
                 self.__server__ = SocketServer.ThreadingTCPServer( ( HOST, int( PORT ) ), MyTCPHandler )
                 self.__server__.serve_forever( 0.001 )
             except Exception , e :
                 print e
                 assert False, e

'''class TestClient():
    
    def sendMsg(self,Msg="test client"):
 
        sock=socket.socket()
        try :
            sock.connect((HOST,PORT))
        except Exception ,e :
            print e
        print "Client Send %s " % Msg    
        sock.sendall(Msg )
        sock.close()'''






