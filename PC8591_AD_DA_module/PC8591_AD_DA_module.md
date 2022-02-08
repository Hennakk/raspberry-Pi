# PC8591_AD_DA_module

I2C(Inter-Integrated Circuit)
두 개의 신호선(SAD, SCL)로 다수의 디바이스와 데이터를 송/수신할 수 있는 통신방식이다. 버스 형태로 라인을 공유하며 address에 따라서 여러 개의 주변 장치와 통신이 가능하다.    

![image](https://user-images.githubusercontent.com/98154707/153010726-b5688836-08f7-424a-818c-1cfda4cb290a.png)   

마스터에서 기준 클럭을 생성하고(SCL) 이 클럭에 맞추어 마스터와 슬레이브 간에 데이터(SDA)를 전송하고 수신한다. SDA와 SCL은 풀-업저항으로 HIGH가 디폴트이다.   
![image](https://user-images.githubusercontent.com/98154707/153011078-50ed40f6-7410-41be-87e0-207167d1ca10.png)   

두 신호 모두 HIGH 상태에서 SDA신호만 LOW로 떨어지면 시작신호로 판단하고 SCL신호는 클럭 신호 만들어 진다. 클럭이 LOW일 때 SDA신호를 비트신호로 바꾼 후 클럭이 HIGH가 될 때 SDA신호를 읽는다. 모든 비트 전송이 끝난 후 SCL신호가 HIGH가되면 SDA신호도 HIGH로 만들어 데이터 전송을 정지한다. 처음 7bit는 슬레이브의 주소, 8번째 비트는 R/W이다. 이때 슬레이브의 주소를 R/W를 쉬프트 시킨 확장형8bit로 표기할 수 있음을 주의한다.   


PCF8591   
라즈베리파이에는 아날로그 신호를 읽을 수 있는 기능이 없기 때문에 A/D, D/A converter PCF8591모듈을 사용하여 아날로그 값을 읽을 수 있게 한다. 이때 I2C 통신을 이용하여 아날로그 값을 읽는다.    
![image](https://user-images.githubusercontent.com/98154707/153011587-4e765360-0ef0-4214-97b5-400e181bd1f7.png)   
PCF8591의 주소는 1001000이므로 16진수로 변환하면 0x48임을 데이터 시트에서 알 수 있다. 소자를 원하는 아날로그 채널에 연결한 후 아날로그 핀번호(A0~A2)를 선택하여 프로그램을 구성한다. 또는 $sudo i2cdetect -y 1 명령어를 사용하여 버스에 연결된 모듈의 주소를 확인할 수 있다.    



I2C통신 오실로스코프로 파형 관찰   
![image](https://user-images.githubusercontent.com/98154707/153013354-843612c4-b070-4e2e-b550-6eadf1688869.png)노란색 파형이 SCL 파란색 파란색 파형이 SDA를 나타낸다.
