#include <wiringPi.h>
#include <pc8591.h>    // Need i2C Enable
#include <stdio.h>

#define Q2WABASE   120
#define ADCCH        0
int main(void)

    int value, da, temp;
    wiringPiSetup();
    pcf8591Setup(Q2W_ABASE, 0x48);
while(1)
{
  value=analogRead(Q2W_ABASE + ADC_CH);
dat = (value * 1.294);
   temp = dat / 10;
   printf("dat : %d mV | temp : %d 'C \n", dat, temp);
   delay(100);
   }
    return 0;
}
