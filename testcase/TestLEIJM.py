'''
Created on 2012-3-25

@author: leijm
'''
from testframe.ITestFixture import ITestFixture

class TestLeijm( ITestFixture ):
    '''
    classdocs
    '''


    def __init__( self ):
        '''
        Constructor
        '''
        ITestFixture.__init__( self )
        print 1
        a = "aadff1"
        print a.capitalize()

    def testAAA( self ):
        pass

