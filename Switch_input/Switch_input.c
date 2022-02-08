#include <stdio.h>
#include <wiringPi.h>
#define	LED1    4 
#define	LED2    5 
#define	TACTSW  0 
#define	TILTSW  2 

int main (void)
{
    int tactsw, tiltsw;
    wiringPiSetup();
pinMode(LED1, OUTPUT);
    pinMode(LED2, OUTPUT);

    pinMode(TACTSW, INPUT);
    pinMode(TILTSW, INPUT);

    while(1)
    {   
tactsw = digitalRead(TACTSW);
        tiltsw = digitalRead(TILTSW);

if(tactsw == 0)
        {
            digitalWrite(LED1, 1);
        }else{
            digitalWrite(LED1, 0);
        }
        if(tiltsw != 0)
        {
            digitalWrite(LED2, 1);
        }else{
            digitalWrite(LED2, 0);
        }
        delay(100);
    }
}
