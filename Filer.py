#!/usr/bin/python #just for unix

import os
import Pathor

class Filer(object):


    def __init__(self):
        self.Rootlist = []
        self.Filelist = []
        self.root = 'None'
        
    def filer(self):
        self.root = self.Rootlist.pop()
        for files in os.listdir(self.root):
            files = Pathor.encap(self.root, files)
            if os.path.isdir(files):
                self.Rootlist.append(files)
            else:
                self.Filelist.append(files)
        return self.Filelist


    def Getroot(self):
        root = raw_input()
        if os.path.isdir(root):
            self.Rootlist.append(root)
        else:
            print("please check your input")
            self.Getroot()

    def IsRoot(self):
        if len(self.Rootlist):
            return True
        else:
            return False
