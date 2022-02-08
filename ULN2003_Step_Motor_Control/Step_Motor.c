#include <stdio.h>
#include <wiringPi.h>
#define PIN_0   7    // #4
#define PIN_1   0    // #17
#define PIN_2   2    // #27
#define PIN_3   3    // #22
int stepMoterWrite(int moveStep)
{
int step[8][4] = {
        {HIGH, LOW, LOW, LOW},  // step   1
        {HIGH,HIGH, LOW, LOW},  // step 1~2
        { LOW,HIGH, LOW, LOW},  // step   2
        { LOW,HIGH,HIGH, LOW},  // step 2~3
        { LOW, LOW,HIGH, LOW},  // step   3
        { LOW, LOW,HIGH,HIGH},  // step 3~4
        { LOW, LOW, LOW,HIGH},  // step   4
        {HIGH, LOW, LOW,HIGH},  // step 4~1  };
    digitalWrite(PIN_0, step[moveStep][0]);
    digitalWrite(PIN_1, step[moveStep][1]);
    digitalWrite(PIN_2, step[moveStep][2]);
    digitalWrite(PIN_3, step[moveStep][3]);
}
int main(void)
{
    wiringPiSetup() 
    pinMode(PIN_0, OUTPUT);
    pinMode(PIN_1, OUTPUT);
    pinMode(PIN_2, OUTPUT);
    pinMode(PIN_3, OUTPUT);
    while(1){
for(int loop=0; loop < 535; loop++)         //정회전 
        {
            for(int i=0; i<8;i++){      
                stepMoterWrite(i);
                delay(1);
            }
        }
for(int loop=0; loop < 535; loop++)        //역회전 
        {
            for(int i=7; i>=0;i--){     
                stepMoterWrite(i);
                delay(1);
            }
        }
}
}
