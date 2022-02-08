import RPi.GPIO as GPIO
import time

switch1 = 25
LED = 18
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(switch1, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED,GPIO.OUT)

try :
    while True :
        if GPIO.input(switch1) == 0:
            GPIO.output(LED,True)
            print ("pushed")
            time.sleep(2)
        else :           
            GPIO.output(LED,False)
            print("not press")
            time.sleep(0.5)

except KeyboardInterrupt :
    GPIO.cleanup()
