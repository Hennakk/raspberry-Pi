import RPi.GPIO as GPIO
import smbus
import time

bus = smbus.SMBus(1)
LED=18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT)

pwm=GPIO.PWM(LED,50)
pwm.start(0)

print("Read the A/D")

bus.write_byte(0x48,0)

def ReadVol() :
    adc = bus.read_byte(0x48)
    return adc


while True :
    dc = ReadVol()/10
    print(dc)
    pwm.ChangeDutyCycle(dc)
pwm.stop()
GPIO.cleanup()
