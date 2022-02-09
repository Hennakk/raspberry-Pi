#include <stdio.h>
#include <wiringPi.h>

#define RELAY    7  // #4


int main(void){

    if(wiringPiSetup()==-1){
        return 1;
    }
    
    // 릴레이 GPIO 설정
    pinMode(RELAY,OUTPUT);
    digitalWrite(RELAY,LOW);


    while(1){         // 무한반복 - 릴레이 On-Off

        digitalWrite(RELAY,HIGH);
        delay(1000);

        digitalWrite(RELAY,LOW);
        delay(1000);

    }
}
