'''
Created on 2011-10-28

@author: ACER
'''

from testframe.ITestFixture import *

import sys, socket, struct
from public.TestConfig import TestConfig
from testproxy.TestPyServerThread import *
from testproxy.TestTcpSrv import TestPyServerThread

class TestAppFrame( ITestFixture ):
    '''
    classdocs
    '''

    def setUp( self ):
        pass #print "testme setup"
    def tearDown( self ):
        pass#print "testme teardown"

    def testAppDemo( self ):
        #assert 1==2,"1!=2"
        print  socket.ntohl( 65535 );
        assert False, "test  testAppDemo"

    def testASetunion( self ):
        print "TestDemo testsetunion"
        aset = set( [21, 221] )
        bset = set( [1, 2] )
        c = aset.union( bset )
        print str( c )

    def testPopen( self ):

        '''ret=popen("dir")
        lines=ret.readlines()'''


    def testDBSqlite3( self ):
            import sqlite3
            cxn = sqlite3.connect( 'd:\leijmdb' )
            cur = cxn.cursor()
            cur.execute( 'create table users1(login varchar(8),uid integer)' )
            cur.execute( 'insert into users1 values("j1",100)' )
            cur.execute( 'insert into users1 values("j2",100)' )
            cur.execute( 'select * from users1' )
            for eachuser in cur.fetchall():
                print eachuser
            cur.execute( 'drop table users1' )
            cur.close()
            cxn.commit()
            cxn.close()

    def sendMsg( self, Msg = "test client" ):
            HOST, PORT = TestConfig().readCfg()
            print HOST, PORT
            sock = socket.socket()
            try :
                sock.connect( ( HOST, int( PORT ) ) )
            except Exception , e :
                print e
            print "Client Send %s " % Msg
            sock.sendall( Msg )
            sock.close()


    def testSendClientOK( self ):
            tserver = TestPyServerThread()
            tserver.start()
            self.sendMsg( "Test Client" )
            self.sendMsg( "quit" )
