#include <wiringPi.h>
#include <stdio.h>

#define SEG_A   27
#define SEG_B   26
#define SEG_C   23
#define SEG_D   24
#define SEG_E   25
#define SEG_F   28
#define SEG_G   29
#define SEG_DP  22

int segmentPinNumber[8] = { SEG_A, SEG_B, SEG_C, SEG_D, SEG_E, SEG_F, SEG_G, SEG_DP};

int segmentValue[11][8] = {
    {1,1,1,1,1,1,0,0}, // 0
    {0,1,1,0,0,0,0,0}, // 1
    {1,1,0,1,1,0,1,0}, // 2
    {1,1,1,1,0,0,1,0}, // 3
    {0,1,1,0,0,1,1,0}, // 4
    {1,0,1,1,0,1,1,0}, // 5
    {1,0,1,1,1,1,1,0}, // 6
    {1,1,1,0,0,0,0,0}, // 7
    {1,1,1,1,1,1,1,0}, // 8
    {1,1,1,1,0,1,1,0}, // 9
    {0,0,0,0,0,0,0,1}, // DOT
};

int main(void)
{
    wiringPiSetup();

    for(int i=0;i<8;i++)
    {
        pinMode(segmentPinNumber[i],OUTPUT);
    }

    while(1)
    {
        for(int j=0;j<11;j++)
        {
            for(int i=0;i<8;i++)
            {
                digitalWrite(segmentPinNumber[i],segmentValue[j][i]);
            }

            delay(1000);
        }
    }

    return 0;
}
