import RPi.GPIO as rp
import time

dac = [8,11,7,1,0,5,12,6]
number = [0,0,0,0,0,0,0,0]

rp.setmode(rp.BCM)
rp.setup(dac, rp.OUT)

rp.output(dac, number)
time.sleep(15)
rp.output(dac, 0)

rp.cleanup()