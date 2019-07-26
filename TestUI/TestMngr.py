#-*- coding: gbk -*-
'''
Created on 2012-4-2

@author: leijm
'''
import Tkinter
from wx import wx


class TestMngr( object ):
    '''
    classdocs
    '''


    def __init__( self ):
        '''
        Constructor
        '''
    def uiMain( self ):

        top = Tkinter.Tk()

        #:建一个canvas,和一个Label
        Cc = Tkinter.Canvas( top, bg = "blue", height = 300, width = 300 )
        label = Tkinter.Label( Cc, text = 'hello' )

        #将Label放置到坐上点在Canvas的纵横30%的处
        label.place( height = 100, width = 100, relx = 0.3, rely = 0.3 )
        self.tree = wx.TreeCtrl()
        root = self.tree.AddRoot( "wx.Object" )

        Cc.pack()

        top.mainloop()

if ( __name__ == '__main__' ):
    #TestMngr().uiMain()
    app = wx.PySimpleApp()
    frame = wx.Frame( parent = None )
    frame.Show( True )
    app.MainLoop()
    #raw_input( "please enter any key!" )
