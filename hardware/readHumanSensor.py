#coding : UTF-8

import RPi.GPIO as GPIO
import time

# --- begin GPIO setup ---

GPIO.setmode(GPIO.BCM)

# num of pins for use (sum is 17)
pushnum = 4
pullnum = 0

# push
allpushpin = (21, 20, 16, 12, 25, 24, 23, 18, 5, 22, 27, 17, 4, 6, 13, 19, 26)
pushpin = allpushpin[:pushnum]
for i in pushpin :
    print "setup : " + str(i)
    GPIO.setup(i, GPIO.OUT)

# pull
allpullpin = (26, 19, 13, 6)
pullpin = allpullpin[:pullnum]
for i in pullpin :
    print "setup : " + str(i)
    GPIO.setup(i, GPIO.OUT)

# --- end GPIO setup ---
# --- begin define ---

# push
def _pushPerfume(decisec):
    for i in pushpin :
        print "high : " + str(i)
        GPIO.output(i, GPIO.HIGH)
    for _ in xrange(decisec):
        time.sleep(.01)
    for i in pushpin :
        print "low : " + str(i)
        GPIO.output(i, GPIO.LOW)

# pull
def _pullPerfume(decisec):
    for i in pullpin :
        print "high : " + str(i)
        GPIO.output(i, GPIO.HIGH)
    for _ in xrange(decisec):
        time.sleep(.01)
    for i in pullpin :
        print "low : " + str(i)
        GPIO.output(i, GPIO.LOW)

# all
def perfume():
    _pushPerfume(decisec = 5000)
    _pullPerfume(decisec = 100)

# --- end define ---
# --- begin main ---

perfume()

# --- end main ---
# --- begin GPIO terminate ---

GPIO.cleanup()

# --- end GPIO terminate ---
