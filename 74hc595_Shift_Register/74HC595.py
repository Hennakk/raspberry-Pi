import RPi.GPIO as GPIO
import time

SCK = 24
data = 23
RCK = 25
OE = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SCK,GPIO.OUT)
GPIO.setup(RCK,GPIO.OUT)
GPIO.setup(data,GPIO.OUT)
#GPIO.setup(OE,GPIO.OUT)

#GPIO.output(OE,HIGH)

def shiftOut(pin, sck, msb, temp) :
    if msb == 'MSBFIRST' :
        for i in range(7,-1,-1) :
            GPIO.output(pin,temp & (0x01 <<i))
            GPIO.output(sck,GPIO.HIGH)
            time.sleep(0.005)
            GPIO.output(sck,GPIO.LOW)
            time.sleep(0.005)
    else :
        for i in range(0,8) :
            GPIO.output(pin,temp & (0x01 <<i))
            GPIO.output(sck,GPIO.HIGH)
            time.sleep(0.005)
            GPIO.output(sck,GPIO.LOW)
            time.sleep(0.005)

while True :
    for i in range(0,255) :
        GPIO.output(RCK,GPIO.LOW)
        shiftOut(data,SCK,’MSBFIRST’,i)
        GPIO.output(RCK,GPIO.HIGH)
        time.sleep(0.01)
