import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

segments = (2,3,4,5,6,7,8,9)

for segment in segments :
    GPIO.setup(segment,GPIO.OUT)
    GPIO.output(segment,0)


seg = {
    '0' : (1,1,1,1,1,1,0,0),
    '1' : (0,1,1,0,0,0,0,0),
    '2' : (1,1,0,1,1,0,1,0),
    '3' : (1,1,0,1,1,0,1,0),
    '4' : (0,1,1,0,0,1,1,0),
    '5' : (1,0,1,1,0,1,1,0),
    '6' : (1,0,1,1,1,1,1,0),
    '7' : (1,1,1,1,1,1,1,0),
    '8' : (1,1,1,1,0,1,1,0),
    '9' : (0,0,0,0,1,0,0,1),
  # 'DOT' : (0,0,0,0,0,0,0,1)
}

for index in range(0,10) :
    s=str(index)
    for loop in range(0,8) :
        GPIO.output(segments[loop],seg[s][loop])
    time.sleep(1)
GPIO.cleanup()
