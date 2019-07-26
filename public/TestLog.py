'''
Created on 2011-10-29

@author: ACER
'''

import sys
import time

class TestLog():
    LOGFILE = "log/testbs.log"
    def __init__( self ):
        self.flog = None
        try:
            self.flog = open( self.LOGFILE, "w" )
        except Exception , e:
             self.flog = open( "testbs.log", "w" )
             print sys.stderr, e

    def retTime( self , space = " [Debug] :" ):
        return time.strftime( "%Y-%m-%d %X", time.localtime() ) + space

    def __del__( self ):
        if self.flog:
            self.flog.close()

    def log( self , inf, *args ):
        print >> self.flog, self.retTime(), inf % args
        print  self.retTime(), inf % args

        return self

global testlog
testlog = TestLog()
if __name__ == "__main__":
    testlog.log( "TestLog log" )

