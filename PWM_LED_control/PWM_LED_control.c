#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>
#include <softPwm.h>
#include <stdint.h>
int main (void)
{
    int bright1, birght2;
    if (wiringPiSetup() == -1)
        exit(1);
    pinMode (1, PWM_OUTPUT); 
    pinMode (6, PWM_OUTPUT);                         
softPwmCreate(6, 0, 100);
    while (1)                              
    {
        for (bright1 = 0 ; bright1 < 1024 ; ++bright1)
        {
            pwmWrite(1, bright1);
            delay(1);
        }
        for (bright1 = 1023 ; bright1>= 0 ; --bright1)
        {
            pwmWrite(1, bright1);
            delay(1);
        }

for (bright2 = 0 ; bright2 < 100 ; ++bright2)
        {
            softPwmWrite(6, bright2);
            delay(10);
        }
        for (bright = 100 ; bright >= 0 ; --bright)
        {
            softPwmWrite(6, bright2);
            delay(10);
    }
}
}
