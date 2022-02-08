#0부터 9999R까지 증가

import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

segments = (21,16,6,19,26,20,5,13)

for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, GPIO.LOW)
    
digits = (24,23,18,4)

for digit in digits:
    GPIO.setup(digit,GPIO.OUT)
    GPIO.output(digit, GPIO.HIGH)

num = {' ':(0,0,0,0,0,0,0,0),
       '0':(1,1,1,1,1,1,0,0),
       '1':(0,1,1,0,0,0,0,0),
       '2':(1,1,0,1,1,0,1,0),
       '3':(1,1,1,1,0,0,1,0),
       '4':(0,1,1,0,0,1,1,0),
       '5':(1,0,1,1,0,1,1,0),
       '6':(1,0,1,1,1,1,1,0),
       '7':(1,1,1,0,0,1,0,0),
       '8':(1,1,1,1,1,1,1,0),
       '9':(1,1,1,1,0,1,1,0)}   

def seg():
    for digit in range(4):
        GPIO.output(segments, (num[display_string[digit]]))
        GPIO.output(digits[digit], 0)
        time.sleep(0.001)
        GPIO.output(digits[digit], 1)
try:
    n = 0
    while n >= 0:
        display_string = str(n).rjust(4)
        n += 1
        if n == 9999 :
            n=0
        seg()
finally:
        GPIO.cleanup()
