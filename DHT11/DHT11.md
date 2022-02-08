# DHT11   
DHT11은 온도와 습도에 따라 저항이 변하는 특성을 이용하는 센서이다. 온도가 증가하면 저항을 감소하고 습도변화에 따라 저항이 변한다.    
 ![image](https://user-images.githubusercontent.com/98154707/153037694-b87d07bf-d5d7-4a3a-975a-331183896e86.png)
라즈베리파이 또는 MCU가 start signal을 송신하면, DHT11은 80us의 HIGH 펄스를 송신한다. HIGH 펄스의 지속시간이 긴 펄스는 데이터 1, HIGH 지속시간이 짧은 펄스는 0을 의미한다.
DGT 온도센서 라이브러리를 다운받아 사용하며 라즈베리 터미널 창에서 라이브러리를 설치 하도록 한다.   

* 라이브러리 설치   
$pip3 install adafruit-blinka   
$pip3 install adafruit-circuitpython-dht   
$sudo apt install libgpiod2      

https://github.com/adafruit/Adafruit_Python_DHT
