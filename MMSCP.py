#!usr/bin/python    #just for Unix
# _*_ coding: utf-8 _*_

import subprocess

class MMSCP(object):


    def __init__(self):
        self.mmsquene = []
        self.mmslist = []
        self.CMD_RAR = 'D:\\Program Files\\WinRAR\\RAR.exe '
        self.CMD_ARGV = 'a -df -ep -m0 -hp', '<a longlong powerful password here>'
        self.CMD_DOCNAME = ' '
        self.CMD_MMS = ' '
        
    def MMSCP(self, mmship):
        print mmship
        if mmship == []:
            return 0
        else:
            self.mmsquene = mmship
            for mmslist in self.mmsquene:
                self.CMD_DOCNAME = '_'.join(mmslist.pop())
                self.CMD_MMS = '" "'.join(mmslist)
                CMD = self.CMD_RAR + self.CMD_ARGV + self.CMD_DOCNAME + ' "' + self.CMD_MMS + '"'
#                print CMD
                subprocess.Popen(CMD).wait()

