import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.OUT)

While True ::
    GPIO.output(25,True)
    time.sleep(1)
    GPIO.output(25,False)
    time.sleep(1)
    
GPIO.cleanup()
