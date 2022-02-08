##  7-Segment
7Segment는 출력장치로, a~g까지의 7개의 LED를 이용하여 획으로 숫자나 문자를 나타낼 수 있다. 동작 방식에 따라 Common-Anode 타입과 Common-Cathode타입으로 구분된다.    
 ![image](https://user-images.githubusercontent.com/98154707/153040630-911f1bb9-a906-477d-84d7-8dc247597849.png)
Common-Anode(공통 양극)
LED의 Anode, +극끼리 묶은 후 Vcc에 연결한다. 다이오드의 특성에 따르면 양극의 전압이 음극의 전압보다 클 경우 정바이어스가 되면서 회로가 short된다. 각각의 LED의 -극의 cathode부분의 제어 핀에 LOW를 인가하면 다이오드가 도통되면서 LED의 불이 켜진다. 

![image](https://user-images.githubusercontent.com/98154707/153040712-bae717c8-d0ce-4f10-ab17-71720f857c4d.png)
Common-Cathode(공통 음극)
LED의 -극인 Cathode끼리 묶어 GND에 연결한다. 각각의 LED핀에 HIGH신호를 인가할 때 다이오드가 도통 되고 LED가 켜진다. 



## 	4Digit-7segment
4Digit-7Segment는 7Segment가 4개있는 방식으로 a~g까지의 7개의 핀, dot핀, 4개의 Digit 핀의 총 12개의 핀을 가진다.   
8개의 출력 segment 핀을 공유하고 4개의 digit단자만 분리하여 사용한다. 이는 각각의 digit핀에 데이터를 동시에 출력하는 것이 아닌 digit1만 켜서 데이터를 표시  
digit2만을 켜서 데이터를 표시하고 이때 잔상효과에 의해 눈에 잔상이 남아 동시에 나타나는 것처럼 보이는 방법을 이용한다. 
 ![image](https://user-images.githubusercontent.com/98154707/153041062-61f8bf52-b33c-4d36-8666-7f54bc079dd2.png)
Anode와 Cathode를 잘 구분하여 쓰도록 한다.
