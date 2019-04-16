# -*- coding: utf-8 -*- 
import pygame

from config import BackLight
import os
import sys
        
class BrightnessTool():
    _value=5

    def __init__(self):
        brt  = self.ReadBackLight()
        self._value =brt 
    
    def ReadBackLight(self):
        try:
            f = open(BackLight)
        except IOError:
            return 0
        else:
            with f:
                content = f.readlines()
                content = [x.strip() for x in content]
                return int(content[0])

        return 0

    def SetBackLight(self,newbrt):
        try:
            f = open(BackLight,'w')
        except IOError:
            print("Open write %s failed %d" % (BackLight,newbrt))
            return False
        else:
            with f:
                f.write(str(newbrt))
                return True
         

    def Further(self):
        self._value+=1
        if self._value > 9:
            self._value = 9
        self.SetBackLight(self._value)
       
                    
    def StepBack(self):
        self._value-=1

        if self._value < 1:
            self._value = 1
        self.SetBackLight(self._value)


#test
#tool = BrightnessTool()
#tool.StepBack()
#print("test")

        
    
