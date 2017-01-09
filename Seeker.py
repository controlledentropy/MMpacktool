#!/usr/bin/env python    #instillation of unix
# _*_ coding: utf-8 _*_
import re
import os

class Seeker(object):

    def  __init__(self):
        self.Mship = []
        self.Mpack = []
        self.Mquene = []
        self.Mseeker = re.compile(r'[a-zA-Z]{2,5}-?[\d]{3}')
        
    def seek(self, Mlist, Rootpath):
        self.Mquene = []
        
        if (Mlist == []) is True:
            pass
        else: 
            self.Mship = Mlist
            while self.Mship:
                mm = self.Mship.pop()
                clean = (mm.replace('sis001', '')).replace('SIS001', '')
                MMpatch = self.Mseeker.search(clean)
                if MMpatch:
                    self.Mpack = []
                    MMkey = MMpatch.group()
                    rootmm = os.path.join(Rootpath, mm)
                    Fsize = os.path.getsize(rootmm)
                    self.Mpack.append(rootmm)

                    for mms in self.Mship:
                        MMSpatch = re.search(MMkey, mms)

                        if MMSpatch:
                            rootmms = os.path.join(Rootpath, mms)
                            self.Mship.remove(mms)
                            Fsize += os.path.getsize(rootmms)
                            self.Mpack.append(rootmms)
                        else:
                            continue
                        
                    if (self.Mpack == []) == False  and (Fsize <= 4*1024**3) == True:
                        self.Mpack.append(MMkey)
                        self.Mquene.append(self.Mpack)

                    else:
                        print "the MM is too FAT to Hug..."
                    

                else:
                    pass
        return self.Mquene    

            
