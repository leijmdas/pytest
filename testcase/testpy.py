'''
Created on 2011-10-23

@author: ACER
'''
#import TestDemo   
from testframe.TestSuite import *


class testpy( ITestFixture ):
   # public TestDemo2( s): .__init__(s) 
  # You can even use the same name 
  # as the test class in the base class:
    def testA( self ):
        print "testoy"
    class Test( ITestFixture ):
        def testA( self ):
            print "testDemo2.testA"
            '''affirm(1 + 1 == 2)'''

        def testB( self ):
            print " stDemo2.testB"
            '''affirm(2 * 2 == 4)'''
    def setUp( self ):
        pass #print "testme setup"
    def tearDown( self ):
        pass#print "testme teardown"
class Point:
    a = "a"
    def __init__( self, x = 0, y = 0 ):
        self.x = x
        self.y = y
    def __str__( self ):
        return "x-value" + str( self.x ) + " y-value" + str( self.y )
    def __add__( self, other ):
        p = Point()
        p.x = self.x + other.x
        p.y = self.y + other.y
        return p
    def testpyme( self ):
        print 'dhhh'

def Print( self ):
    p1 = Point( 3, 4 )
    p2 = Point( 2, 3 )
    print p1
    print p1.y
    print ( p1 + p2 )
    try:
        f = open( "c:\\testjavabs.log" )
        lines = f.readlines()
        for line in lines:
            print line.replace( "\n", "" )

            #line=f.readline()
        f.close()
    except IOError :
        print   "111";



