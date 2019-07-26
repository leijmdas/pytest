'''
Created on 2012-4-2

@author: leijm
'''
import sys, os
from public.TestLog import testlog

class ITestHelper:
    def __ini__( self ):
        pass

    def getMainPath( self ):
        sys.path.append( os.getcwd() + "/testcase" )
        sys.path.append( os.getcwd() + "/testframe" )
        sys.path.append( os.getcwd() + "/TestUI" )
        sys.path.append( os.getcwd() + "/public" )
        sys.path.append( os.getcwd() + "/testproxy" )


        main, ext = os.path.split( sys.argv[0] )
        print main
        testlog.log( main )
        return main

global testhelper
testhelper = ITestHelper()
