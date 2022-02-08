import RPi.GPIO as GPIO
import time
import numpy

CLK=11
CS=8
Din=10

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(CLK,GPIO.OUT)
GPIO.setup(CS,GPIO.OUT)
GPIO.setup(Din,GPIO.OUT)

def Write_Data_byte(Data) :
    GPIO.output(CS,GPIO.LOW)
    for i in range(0,8) :
        GPIO.output(CLK,GPIO.LOW)
        GPIO.output(Din,Data&0x80)
        Data = Data << 1
        GPIO.output(CLK,GPIO.HIGH)
        
def Write_Data(address, dat) :
    GPIO.output(CS,GPIO.LOW)
    Write_Data_byte(address)
    Write_Data_byte(dat)
    GPIO.output(CS,GPIO.HIGH)
    
Write_Data(0x09,0x00) #No decode mode
Write_Data(0x0A,0x08) #Intensity 
Write_Data(0x0B,0x07) #All digit on
Write_Data(0x0C,0x01) #Shutdown mode - Normal
Write_Data(0x0F,0x00) #Normal 
    
dot = [
    [ 0x3c, 0x7e, 0xc3, 0xc3, 0xc3, 0xc3, 0x7e, 0x3c ], 
    [ 0x04, 0xc6, 0xc3, 0xff, 0xff, 0xc0, 0xc0, 0x00 ],
    [ 0x06, 0xc7, 0xe3, 0xf3, 0xdb, 0xcf, 0xc6, 0x00 ], 
    [ 0x22, 0x63, 0x49, 0x49, 0x7F, 0x36, 0x00, 0x00 ], 
    [ 0x18, 0x1C, 0x16, 0x53, 0x7F, 0x7F, 0x50, 0x00 ], 
    [ 0x27, 0x67, 0x45, 0x45, 0x7D, 0x39, 0x00, 0x00 ],
    ]

while True :
    for i in range(0,6) :
        for j in range(0,8) :
            Write_Data(j+1,dot[i][j])
    time.sleep(0.1)
        for j in range(0,8) :
            Write_Data(j+1,0)
            time.sleep(0.01)
            
GPIO.cleanup()
