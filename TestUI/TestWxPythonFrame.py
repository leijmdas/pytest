'''
Created on 2012-4-2

@author: leijm
'''
from testframe.ITestFixture import ITestFixture
from WxPythonFrame import *

class TestWxPythonFrame( ITestFixture ):
   # You can even use the same name 
   # as the test class in the base class:
    def __init__( self ):
        ITestFixture.__init__( self )

    def setUp( self ):
        pass

    def tearDown( self ):
        pass

    def testFrame( self ):
        pass
        #TestFrameThread().start()


