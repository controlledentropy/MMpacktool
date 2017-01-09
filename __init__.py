#!/usr/bin/python    # instillation of Unix like
# _*_ coding: utf-8 _*_
# __author__: Michael Clayton
# besure your Winrar is Reliable. and be sure your password is a powerful stringXD

import os
import Seeker
import MMSCP


seeker = Seeker.Seeker()
mmscp = MMSCP.MMSCP()

class MMSwalker(object):

    def __init__(self):
        self.rootpath = ''
        self.mmship = []

    def walker(self):
        i = 0
        for rootpaths, dirs, files in os.walk(self.rootpath):
##            print rootpaths
##            print '*'*10
##            print files
            if (files == []) == False:
                self.mmship = seeker.seek(files, rootpaths)
                mmscp.MMSCP(self.mmship)
                self.mmship
                
            else:
                continue

    def getroot(self):
        uip = ''
        while os.path.isdir(uip) == False:
            print "please check your input, dude..."
            uip = raw_input()
        self.rootpath = uip

mwalker = MMSwalker()

mwalker.getroot()
mwalker.walker()
