#include <wiringPi.h>
#include <pcf8591.h>      
#include <stdio.h>

#define	BUZZER       15
#define Q2W_ABASE   120
#define ADC_CH        0

void voice_freq(int del)
{
    digitalWrite(BUZZER,HIGH);
    delay(del);
    digitalWrite(BUZZER,LOW);
    delay(del);
}

int main(void)
{
    int value;
 
    wiringPiSetup();
    pcf8591Setup(Q2W_ABASE,0x48);
    pinMode(BUZZER,OUTPUT);
    digitalWrite(BUZZER,LOW);

    while(1)
    {
        value = analogRead(Q2W_ABASE+ADC_CH);
        printf("> %d \r\n",value);  
        if (value<100)
            voice_freq(value);
        delay(1000);
    }
}
