'''
Created on 2012-4-2

@author: leijm
'''

wxID_WXTIMER = 200
wxID_WXFRAMEBTN = 201
wxID_WXFRAMEBTNABOUT = 202
ID_ABOUT = 101
ID_EXIT = 110

import os, random
import sys, wx

global JPG_FILE, JPG_PATH
JPG_PATH = "d:/jpg"
JPG_FILE = "girl.jpg"

class WxPythonHelper( object ):
    '''
    classdocs
    '''


    def __init__( self , panel = None ):
        self.panel = panel
        if panel:
            self.frm = panel.Parent.Parent

    def initTimer( self ):
        if self.frm:
           self.timer = wx.Timer( self.frm, wxID_WXTIMER )
           self.frm.Bind( wx.EVT_TIMER, self.onTimer, self.timer )
           self.timer.Start( 1000 )

    def onTimer( self , event ):
       self.redrawImg( self.panel )

    def redrawImg( self, panel ):
          image = self.createImage()

          self.drawImg( panel, image )

    def drawImg( self , panel, image ):
          if panel and image:
                    tbmp = image.ConvertToBitmap()
                    size = tbmp.GetWidth(), tbmp.GetHeight()
                    panel.DestroyChildren()
                    self.bmp = wx.StaticBitmap( parent = panel, bitmap = tbmp )
                    panel.SetClientSize( size )

    def createImage( self ):
           #self.RemoveChild( self.panel )
           #self.panel.Destroy()           #self.panel = wx.Panel( self )
           try:
                image = wx.Image( os.path.join( JPG_PATH , self.__retFile__() ), wx.BITMAP_TYPE_JPEG )
           except Exception , e  :
                print >> sys.stderr, e

                image = None
           return image

    def __retFile__( self ):
        flist = os.listdir( JPG_PATH )
        retlist = []
        for f in flist:
            if f.upper().endswith( ".JPG" ):
                retlist.append( f )
            #from test.test_iterlen import len
        reti = random.randint( 1, len( retlist ) );
        return retlist[reti - 1]
