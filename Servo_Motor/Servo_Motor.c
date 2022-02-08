#include <stdio.h>
#include <wiringPi.h>
#include <softPwm.h> 

#define SERVO_PIN   1   // BCM #18

int main(void)
{
    wiringPiSetup();

    softPwmCreate(SERVO_PIN, 0, 200);  

    while(1)
    {   
 //180도 서보모터의 사용 가능 Duty 범위500us(5)~2400us(24) 
softPwmWrite(SERVO_PIN,15);   // 0 degree
        delay(500);

        softPwmWrite(SERVO_PIN,5);    // -90 degree
        delay(500);

        softPwmWrite(SERVO_PIN,15);   // 0 degree
        delay(500);

        softPwmWrite(SERVO_PIN,24);   // 90 degree
        delay(500);
            
    }   

    return 0;
}
