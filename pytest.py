'''
Created on 2011-11-2

@author: ACER
'''
import os, sys
import xml.dom
import threading
from public.TestLog import testlog

import public.ITestHelper
import testframe.PyTestRunner
from TestUI.WxPythonFrame import TestFrameThread

public.ITestHelper.testhelper.getMainPath()
def main():
        testframe.PyTestRunner.PyTestRunner().runAll()
        print os.path.dirname( sys.argv[0] )

if __name__ == "__main__":
    #main()
    TestFrameThread().start()

    
    

