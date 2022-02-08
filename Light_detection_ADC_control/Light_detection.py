import RPi.GPIO as GPIO
import smbus
import time

bus = smbus.SMBus(1)
address = 0x48

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT)

buz = GPIO.PWM(14,100)
buz.start(100)
buz.ChangeDutyCycle(80)

def readLight() :
    adc = bus.read_byte(0x48)
    return adc

while True:
    bus.write_byte(address,0)
    time.sleep(0.1)
    an0 = readLight()
    print (an0)
    
    if an0 < 100 :
        buz.ChangeFrequency(an0)
    
GPIO.cleanup()
