# LED
*	GPIO(General Purpose Input/Output)   
GPIO란 범용 입출력 인터페이스로 전자기판에서 내부 회로 이외에 물리적으로 소통할 수 있는 장치로 이를 이용하여 다양한 물리적 외부 장치들을 배선하고 연결하여 라즈베리파이를 통해 제어할 수 있다.
 ![image](https://user-images.githubusercontent.com/98154707/153034867-583c26aa-6aae-4b82-9527-5fad82431b27.png)
RPi.GPIO 라이브러리   
파이썬에서 라즈베리 파이의 GPIO핀을 제어할 수 있도록 해주는 라이브러리   
GPIO.setmode(GPIO.BOARD) -> 보드의 핀 번호로 설정   
GPIO.setmode(GPIO.BCM) -> GPIO의 핀번호로 설정   
note. GPIO 19번 사용시 BCM모드인경우 19, BOARD모드인경우 35로 설정한다.   
***
*	Wiring Pi    
C언어로 GPIO핀을 제어할 수 있는 기능을 제공하는 라이브러리     
![image](https://user-images.githubusercontent.com/98154707/153034943-4688b46b-37fd-4f48-b6c3-9033a7e5086c.png)
$sudo apt-get install git-core   
$git clone git://git.drogon.net/wiringPi		 //라이브러리 설치   
$gpio -v                                  	//설치와 버전확인   
$ gpio readall 					//핀배열을 확인할 수 있다.    
  	note. Wiring Pi 라이브러리에서 BCM모드GPIO 19은 Wpi 의 24번 핀 임을 알 수 있다. Wiring Pi 사용하여 코드 작성시 pinMode를24로 설정하여 작성한다.
 
