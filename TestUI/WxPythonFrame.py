'''
Created on 2012-4-2

@author: leijm
'''
from wxPython.wx import *
from wx import wx

import threading
import os
import random
import sys
from WxPythonHelper import *


class TestUIMenu:
    def __init__( self , frame ):
        self.frame = frame

        filemenu = wxMenu()
        filemenu.Append( ID_ABOUT, "&About", " Information about this program" )
        filemenu.AppendSeparator()
        filemenu.Append( ID_EXIT, "E&xit", " Terminate the program" )

        self.menuBar = wxMenuBar()
        self.menuBar.Append( filemenu, "&File" ) # Adding the "filemenu" to the MenuBar
        self.frame.SetMenuBar( self.menuBar )  # Adding the MenuBar to the Frame content.
        EVT_MENU( self.frame, ID_ABOUT, self.OnAbout )
        EVT_MENU( self.frame, ID_EXIT, self.OnExit )


    def OnAbout( self, e ):
       d = wxMessageDialog( self.frame, " A sample editor  "
                           " in wxPython", "About Sample Editor", wxOK )

       d.ShowModal()
       d.Destroy()

    def OnExit( self, e ):
       self.frame.Close( true )  # Close the frame.

class WxPythonFrame( wxFrame ):

    def __init__( self, parent, id, title ):
        """Create a Frame instance and display image."""

        wxFrame.__init__( self, parent, wxID_ANY, title, size = ( 1800, 1600 ), style = wxDEFAULT_FRAME_STYLE | wxNO_FULL_REPAINT_ON_RESIZE )
        self.SetTitle( "TestWxPython Frame" )

        self.testmenu = TestUIMenu( self )
        self.initSplitWnd()
        self.initTreeCtrl()
        self.initBtn()

        self.control = wxTextCtrl( self.panelbtn, 1, style = wxTE_MULTILINE, pos = ( 150, 200 ) )
        center = wx.StaticText( self.panelbtn, -1, "align center", ( 300, 50 ), ( 360, -1 ), wx.ALIGN_CENTER )
        center.SetForegroundColour( 'white' )
        center.SetBackgroundColour( 'black' )
        #sizer = wx.BoxSizer( wx.BOTH )
        #sizer.AddMany( [ self.splitwnd] );
        self.Show( True )
        self.Maximize()

    def initSplitWnd( self ):

        self.splitwnd = wx.SplitterWindow( self, id = -1, pos = ( 10, 20 ), size = ( 1800, 1600 ), style = wx.SP_BORDER, name = "splitterWindow" )
        self.panel = wx.Panel( self.splitwnd )
        self.panelbtn = wx.Panel( self.splitwnd )
        self.splitwnd.SplitVertically( window1 = self.panelbtn  , window2 = self.panel , sashPosition = 200 )
        self.splitwnd.SetClientSize( self.GetMaxSize() )

        self.wxHelper = WxPythonHelper( self.panel )
        #self.wxHelper.drawImg( self.panel, image )
        self.wxHelper.initTimer()

    def initTreeCtrl( self ):
        self.tree = wx.TreeCtrl( self.panelbtn )
        self.root = self.tree.AddRoot( "wx.Object" )
        #self.tree.AddTreeNodes( root, [], self.tree ) 
        dataid = wx.TreeItemId()
        self.tree.AppendItem( self.root, "server" )
        self.tree.ExpandAll()

    def initBtn( self ):
        self.btn = wx.Button( self.panelbtn, id = wxID_WXFRAMEBTN, label = "close", pos = ( 150, 100 ), size = ( 50, 50 ) )
        self.btnabout = wx.Button( self.panelbtn, id = wxID_WXFRAMEBTNABOUT, label = "about", pos = ( 150, 250 ), size = ( 50, 110 ) )
        EVT_BUTTON( self.btn , wxID_WXFRAMEBTN , self.onClosed )
        EVT_BUTTON( self.btnabout , wxID_WXFRAMEBTNABOUT, self.testmenu.OnAbout )


    def onClosed( self , event ):
           self.Close( True )
    '''def initTimer( self ):
       self.timer = wx.Timer( self, wxID_WXTIMER )
       self.Bind( wx.EVT_TIMER, self.onTimer, self.timer )
       self.timer.Start( 1000 )
    def onTimer( self , event ):
       self.wxHelper.redrawImg( self.panel )'''


class TestFrameThread( threading.Thread ):

    def run( self )    :
            print "TestFrameThread run"
            #TestMngr().uiMain()
            app = wxPySimpleApp()

            frame = WxPythonFrame( None, -1, "Sample editor" )
            #frame = wx.Frame( parent = None )
            frame.Show( True )
            #frame.Maximize()
            app.MainLoop()

if ( __name__ == '__main__' ):
        if True:
            TestFrameThread().start()
        else:
            pass

