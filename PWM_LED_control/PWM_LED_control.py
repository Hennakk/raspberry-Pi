import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(5,GPIO.OUT,initial=GPIO.LOW)


pwm = GPIO.PWM(5, 1000)
pwm.start(0)

for dc in range(0, 101, 5) :
    pwm.ChangeDutyCycle(dc)
for dc in range(100, -1, -5) :
    pwm.ChangeDutyCycle(dc)
    time.sleep(0.1)

pwm.stop()
GPIO.cleanup()
