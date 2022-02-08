#5678 출력

import RPi.GPIO as GPIO
import time
import math
import smbus

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

segments = (21,16,6,19,17,20,5,13)

for seg in segments :
    GPIO.setup(seg,GPIO.OUT)
    GPIO.output(seg, 1)
    
digits = (24,23,18,4)

for dig in digits :
    GPIO.setup(dig, GPIO.OUT)
    GPIO.output(dig, 0)
    

seg = {
    0 : (1,1,1,1,1,1,0,0),
    1 : (0,1,1,0,0,0,0,0),
    2 : (1,1,0,1,1,0,1,0),
    3 : (1,1,1,1,0,0,1,0),
    4 : (0,1,1,0,0,1,1,0),
    5 : (1,0,1,1,0,1,1,0),
    6 : (1,0,1,1,1,1,1,0),
    7 : (1,1,1,0,0,1,0,0),
    8 : (1,1,1,1,1,1,1,0),
    9 : (1,1,1,1,0,1,1,0),

}

while True:
    value = 5678
    value = value % 10000
    
    f1 = math.trunc(value/1000) 
    f2 = math.trunc(value/100) % 10
    f3 = math.trunc(value/10) % 10
    f4 = value % 10
        
    fnd = (f1,f2,f3,f4)
        
    for digit in range(4):
        for loop in range(0,8):
            GPIO.output(segments[loop], seg[fnd[digit]][loop])
        GPIO.output(digits[digit], 0)
        time.sleep(0.001)
        GPIO.output(digits[digit], 1)

GPIO.cleanup()
