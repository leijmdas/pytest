'''
Created on 2011-10-28

@author: ACER
'''


import testframe
from  public.TestLog import testlog
import sys


class ITestFixture( object ):
    def __init__( self ):
        self.exemethods = set( [] )
        self.okmethods = set( [] )
        self.failmethods = list( [] )
        self.methods = list( [] )

    def setUp( self ):
        pass
    #@abstractmethod 
    def tearDown( self ):
        pass

    def autoAddTest( self ):
        for m in  dir( self ) :
           if( m.startswith( "test" ) ):
                method = getattr( self, m )
                if( callable( method ) ):
                    #print "callable method " + m
                    #if(self.methods.count(m) == 0):
                    try:
                        self.methods.append( m )
                    except Exception , e:
                        print e

    def addTest( self, method ):
        print "add method %s " % method

        try:
           self.methods.index( method )
        except:
          self.methods.add( method )


    def run( self ):
          if self.methods :
              pass#self.methods=self.methods.sort()
          for methodname in self.methods:

            if( not hasattr( self, methodname ) ):
                continue
            self.exemethods.add( methodname )
            method = getattr( self, methodname )
            print "\nEnter %s::%s" % ( type( self ).__name__, methodname )
            testlog.log( "" )
            testlog.log( "Enter %s::%s" , type( self ).__name__, methodname )
            try:
                self.setUp()
                method()
                self.okmethods.add( methodname )
            except AssertionError, e:
                self.failmethods.append( type( self ).__name__ + "::" + methodname + "==>" + str( e ) )
                print >> sys.stderr, "assert fail " , e  , methodname
                testlog.log( "assert fail  %s %s" , str( e )  , methodname )


            except Exception, e: #@IndentOk
               self.failmethods.append( type( self ).__name__ + "::" + methodname + "==>" + str( e ) )
               print >> sys.stderr, "run Exception ", e , methodname
               testlog.log( "run Exception  %s %s" , str( e )  , methodname )

            finally:
                self.tearDown()
                print "Exit %s::%s" % ( type( self ).__name__, methodname )
                testlog.log( "Exit %s::%s" , type( self ).__name__, methodname )

    @staticmethod
    def addTests( tc, testmethod ):
        pass#TestSuite.addTest( tc, testmethod )

    def CountResult( self , resultsum ):
        resultsum.total += len( self.exemethods )
        resultsum.success += len( self.okmethods )
        resultsum.failedmethods .extend ( self.failmethods )

