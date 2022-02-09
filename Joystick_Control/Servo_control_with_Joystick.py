import RPi.GPIO as GPIO
import time
import smbus

address = 0x48
A0 = 0x40
A1 = 0x41
button = 4
servo1 = 18
servo2 = 17

GPIO.setwarnings(False)
bus = smbus.SMBus(1)

GPIO.setmode(GPIO.BCM)
GPIO.setup(button,GPIO.IN)
GPIO.setup(servo1,GPIO.OUT)
GPIO.setup(servo2,GPIO.OUT)

while True :
    
    bus.write_byte(address, A0)
    bus.write_byte(address, A1)
    X = bus.read_byte_data(address,A1)
    Y = bus.read_byte_data(address,A0) 
    
    # 조이스틱으로부터 받은 아날로그 값 0~255를 서보 모터의 출력 주기 0.0006~0.0026범위로 맞추어야 한다.
    X_value = ((X-4)*0.00000717) + 0.0006
    Y_value = ((Y-4)*0.00000717) + 0.0006
    
    for i in range(0,25):
        GPIO.output(servo1,GPIO.HIGH)
        time.sleep(X_value)
        GPIO.output(servo1,GPIO.LOW)
        time.sleep(0.02)
        GPIO.output(servo2,GPIO.HIGH)
        time.sleep(Y_value)
        GPIO.output(servo2,GPIO.LOW)
        time.sleep(0.02)
    time.sleep(0.001)
    
GPIO.cleanup
