'''
Created on 2011-10-29

@author: ACER
'''
import os

import time, glob
from  ITestFixture  import *

class TestResultSum():
    def __init__( self ):
            self.total = 0
            self.success = 0
            self.failedmethods = []
    def incOK( self ):
            self.success += 1
    def incTotal ( self ):
            self.total += 1


class TestSuite:

    allsuites = {}
    resultsum = TestResultSum()
    exesuites = {}

    def __init__( self ):
            pass

    @staticmethod
    def CountResult():
              for key, obj in TestSuite.exesuites.items():
                   obj.CountResult( TestSuite.resultsum )
              print "================TestResult============="
              print "testcase Total\t:%d" % TestSuite.resultsum.total
              print "testcase success\t :%d" % TestSuite.resultsum.success
              print >> sys.stderr, "testcase failed\t:%d" % ( TestSuite.resultsum.total - TestSuite.resultsum.success )

              print "====================================="
              for fail in TestSuite.resultsum.failedmethods:

                    print >> sys.stderr, fail

    @staticmethod
    def run ( suite ):
        for key, obj in suite.items():
             TestSuite.exesuites[key] = obj

             obj.run()

    @staticmethod
    def addTestSuite( obj ):
        objname = str( obj ).split()
        print objname[0]
        TestSuite.allsuites[objname[0]] = obj
        obj.autoAddTest()
        #print "add obj %s " % obj

    @staticmethod
    def getTestSuite():
        return TestSuite.autoloadModuleFiles( glob.glob( "Test*.py" ) )

    @staticmethod
    def autoloadModule():
        pass

    @staticmethod
    def autoloadModuleFiles( files ):

            modules = []

            for module_file in files:
                try:
                    module_name, ext = os.path.splitext( os.path.basename( module_file ) )
                    module = __import__( module_name )
                    modules.append( module )
                    if( module_name.startswith( "Test" ) ):
                        for name in dir( module ):
                            obj = getattr( module, name )

                            if isinstance( obj, type ) and issubclass( obj, ITestFixture ):
                                TestSuite.addTestSuite( obj() )
                                print "testcase name %s  %s" % ( name, obj() )

                except ImportError , e:
                    print "ImportError=%s" % str( e )# ignore broken modules          


'''def addTest( tc,testmethod ):
    TestSuite.addTest(tc,testmethod)'''


'''print ctime()'''
#print os.dir()        
#raw_input("please inout:")

#if __name__=='__main__'  :
#    main()

