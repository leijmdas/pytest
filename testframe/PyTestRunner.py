'''
Created on 2012-3-25

@author: leijm
'''
import glob, os, sys, struct
from  testframe.TestSuite  import *
from  testframe.ByteBuffer import *

import  threading, SocketServer
import socket
import sys

sys.path.append( os.getcwd() + "/testcase" )
sys.path.append( os.getcwd() + "/testframe" )

class PyTestRunner:


    def __init__( self ):
        pass


    files = []
    def listTestcasePy( self, curpath ):

        for fname in os.listdir( curpath ):

            if( fname.startswith( "Test" ) and fname.endswith( ".py" ) ):

                PyTestRunner.files.append( fname )                #print fname
            if os.path.isdir( fname ):
                self.listTestcasePy( fname )
                #self.files.extend(retfiles)
        return PyTestRunner.files

    @staticmethod
    def autoloadModule():
         files = PyTestRunner().listTestcasePy( os.getcwd() )
         for file in files:
             print file
         TestSuite.autoloadModuleFiles( files )



    @classmethod
    def run ( self, suite ):
        PyTestRunner.autoloadModule()
        TestSuite.run( suite )
        PyTestRunner.CountResult()

    @classmethod
    def runAll( self ):
        PyTestRunner.autoloadModule()
        PyTestRunner.run( TestSuite.allsuites )
        #PyTestRunner.CountResult()
    @staticmethod
    def CountResult ():
        TestSuite.CountResult()








