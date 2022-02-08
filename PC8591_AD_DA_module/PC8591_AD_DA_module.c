#include <stdio.h>
#include <wiringPi.h>
#include <pcf8591.h>

#define	LED       1
#define Q2W_ABASE   120
#define ADC_CH        0
int main (void)
{
    int value ;
    wiringPiSetup () ;
pcf8591Setup (Q2W_ABASE, 0x48) ;
pinMode  (LED, PWM_OUTPUT) ;
    pwmWrite (LED, 0) ;

    while(1)
    {
        value=analogRead(Q2W_ABASE +ADC_CH) ;
        pwmWrite (LED, value * 4) ;
        printf("value=%d\n",value);
        delay (100) ;
    }
}
