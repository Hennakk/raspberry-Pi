import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

Relay = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(Relay,GPIO.OUT)

while 1 :
    GPIO.output(Relay,True)
    time.sleep(1)
    GPIO.output(Relay,False)
    time.sleep(1)
    

GPIO.cleanup()
