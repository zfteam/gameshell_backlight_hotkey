import time
from evdev import InputDevice
from select import select
from tools.brightness_tool import BrightnessTool
import alsaaudio

m = alsaaudio.Mixer()
sound_volume=m.getvolume()[0]
# print("cur aound volume:%d",sound_volume)

dev = InputDevice('/dev/input/event1')

select_press=False
while True:
    select([dev], [], [])
    for event in dev.read():
        # print "code:%s value:%s" % (event.code, event.value)
        if (event.code==57 and event.value==1):
            select_press=True
            # print("sel press")
        elif(event.code==57 and event.value==0):
            select_press=False
        
        if(select_press==True and event.code==103 and event.value==1):
            brightnessTool = BrightnessTool()
            brightnessTool.StepBack()
            del brightnessTool
        elif(select_press==True and event.code==108 and event.value==1):
            brightnessTool = BrightnessTool()
            brightnessTool.Further()
            del brightnessTool
        elif(select_press==True and event.code==105 and event.value==1):
            sound_volume=sound_volume - 20
            if(sound_volume<0):
                sound_volume=0
            try:
                m = alsaaudio.Mixer()
                m.setvolume(sound_volume)
            except Exception,e:
                print(str(e))
        elif(select_press==True and event.code==106 and event.value==1):
            sound_volume=sound_volume + 20
            if(sound_volume>100):
                sound_volume=98

            try:
                m = alsaaudio.Mixer()
                m.setvolume(sound_volume)
            except Exception,e:
                print(str(e))

        
            


