#include <wiringPi.h>
#define LED 6         // Wpi : 6 | BCM : #25
int main(void)
{ 
    wiringPiSetup();
    pinMode(LED,OUTPUT);
    while(1)
    { 
        digitalWrite(LED,HIGH); // LED ON
        delay(1000);
        digitalWrite(LED,LOW);  // LED OFF
        delay(1000); 
    }
    return 0;
}
