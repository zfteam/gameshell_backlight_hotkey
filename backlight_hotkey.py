import time
from evdev import InputDevice
from select import select
from tools.brightness_tool import BrightnessTool

dev = InputDevice('/dev/input/event1')
while True:
    select([dev], [], [])
    for event in dev.read():
        #print "code:%s value:%s" % (event.code, event.value)
        if (event.code==38 and event.value==1):
            brightnessTool = BrightnessTool()
            brightnessTool.Further()
            del brightnessTool
        elif(event.code==35 and event.value==1):
            brightnessTool = BrightnessTool()
            brightnessTool.StepBack()
            del brightnessTool



