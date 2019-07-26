'''
Created on 2011-11-11

@author: ACER
'''
from ByteBuffer import *

class ITestHeader( ByteBuffer ):
    def __init__( self ):
        self.hasBusHeader = 1
        self.cmddesp = "cmddesp";
    def decode( self ):
        pass
    def encide( self ):
        pass
