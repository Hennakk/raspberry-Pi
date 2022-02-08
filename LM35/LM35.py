import time
import smbus
import math

address = 0x48
A0 = 0x40

bus = smbus.SMBus(1)

while True :
    bus.write_byte(address, A0)
    value = bus.read_byte(address)
*   value = (value*1.92) 
    temp = round(value/10,2)
    print(temp)
    time.sleep(0.2)
/*
PCF8591모듈은 8bit의 아날로그 할당비트를 가져 ADC정밀도가 낮다.
500mV(50도) 이하의 낮은 전압체서는 최대 100mV의 오차가 발생한다. 
이러한 오차를 보정하기 위해 온도계산식을 이용하여 계산한 후 10으로 나누어 주어 10배의 오차율을 줄여준다.
*/
