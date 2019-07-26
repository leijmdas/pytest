'''
Created on 2011-11-11

@author: ACER
'''
import struct
import textwrap

class ByteBuffer( object ):
    '''
    classdocs
    '''


    def __init__( self ):
        self.buffer = ""
        self.position = 0
        '''
        Constructor
        '''

    def getInt4( self, data ):
        retint = struct.unpack( "!i", data[0:4] )
        self.position += 4;

        return retint[0]
    def putInt4( self, ivalue ):
        s = struct.pack( "!i", ivalue )
        self.buffer += s
    def putInt8( self, lvalue ):
        s = struct.pack( "!q", lvalue )
        self.buffer += s
    def putString( self, str ):
        l = struct.pack( "!i", len( str ) )
        self.buffer += l + str
    def putStringFix( self, str, width ):
        l = struct.pack( "!i", width )
        '''str=textwrap.fill(str,width)
        
        print str.ljust(width,'\0')'''
        while( len( str ) < width ):
            str += '\x00'
        self.buffer += l + str

    def getBuffer( self ):
        return self.buffer
    def getSize( self ):
        return len( self.buffer )
