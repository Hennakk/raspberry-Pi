import RPi.GPIO as GPIO
import time
pin0 = 4
pin1 = 17
pin2 = 27
pin3 = 22
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(pin0,GPIO.OUT)
GPIO.setup(pin1,GPIO.OUT)
GPIO.setup(pin2,GPIO.OUT)
GPIO.setup(pin3,GPIO.OUT)

step = (
    (1,0,0,0),
    (1,1,0,0),
    (0,1,0,0),
    (0,1,1,0),
    (0,0,1,0),
    (0,0,1,1),
    (0,0,0,1),
    (1,0,0,1)
)

def Step_moter(stem) :
    GPIO.output(pin0,step[stem][0])
    GPIO.output(pin1,step[stem][1])
    GPIO.output(pin2,step[stem][2])
    GPIO.output(pin3,step[stem][3])
    
    
while 1 :
    for loop in range(0,300) :
        for i in range(0,8) :
            Step_moter(i)
            time.sleep(0.001)
                
    for loop in range(0,300) :
        for i in range(7,-1,-1) :
            Step_moter(i)
            time.sleep(0.001)
            
GPIO.cleanup()


