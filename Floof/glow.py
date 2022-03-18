#Filename: glow.py
#Description: Used to light the sensehat LEDs

import threading
import time
from sense_hat import SenseHat

sense = SenseHat()

_ = [  0,   0,   0] # off
r = [255, 0, 0] # red
#r = [0, 255, 0] # green

HEART = [
    _,_,_,r,r,_,_,_,
    _,_,r,r,r,r,_,_,
    _,_,r,r,r,r,r,_,
    _,_,_,r,r,r,r,r,
    _,_,r,r,r,r,r,_,
    _,_,r,r,r,r,_,_,
    _,_,_,r,r,_,_,_,
    _,_,_,_,_,_,_,_,
]

def setHeart(brightness):
    r = [brightness, 0, 0]
    HEART = [
        _,_,_,r,r,_,_,_,
        _,_,r,r,r,r,_,_,
        _,_,r,r,r,r,r,_,
        _,_,_,r,r,r,r,r,
        _,_,r,r,r,r,r,_,
        _,_,r,r,r,r,_,_,
        _,_,_,r,r,_,_,_,
        _,_,_,_,_,_,_,_,
    ]


def HeartBeat():
    while(True):
        for i in range(50, 256):
            setHeart(i)
            sense.set_pixels(HEART)
            time.sleep(0.005)
        
        for i in range(256, 50, -1):
            setHeart(i)
            sense.set_pixels(HEART)
            time.sleep(0.005)
        
def HeartBeatThread():
    th = threading.Thread(target = HeartBeat)
    th.start()

#HeartBeatThread()

