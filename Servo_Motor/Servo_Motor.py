import RPi.GPIO as GPIO
import time

servo = 18
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)


while True :
    for i in range(0,25):
        GPIO.output(servo,GPIO.HIGH)
        time.sleep(0.0024)
        GPIO.output(servo,GPIO.LOW)
        time.sleep(0.02)
    time.sleep(0.1)
    
    for i in range(0,25):
        GPIO.output(servo,GPIO.HIGH)
        time.sleep(0.0015)
        GPIO.output(servo,GPIO.LOW)
        time.sleep(0.02)
    time.sleep(0.1)
    
    for i in range(0,25):
        GPIO.output(servo,GPIO.HIGH)
        time.sleep(0.0006)
        GPIO.output(servo,GPIO.LOW)
        time.sleep(0.02)
    time.sleep(0.15)
GPIO.cleanup()
