## IR-remote
적외선 수신 센서를 사용하여 리모컨을 이용하여 리모컨 버튼의 입력을 받는다. 리모컨 앞의 적외선 LED를 통해 빛으로 신호를 발사하고 적외선 수신 센서가 그 신호를 읽는다. 이의 세부적인 원리를 알아본다.   
적외선 수신 센서는 특정 주파수에서의 신호를 수신한다. 위의 실습에서 사용한 VS1838B는38kHz의 캐리어 주파수를 가진다. 즉, 리모컨이 38kHz의 주파수에서의 신호를 발사한다면(초당 3만8천회 LED Blink) 적외선 수신기에서 신호를 받을 수 있다.  

* 라즈베리 파이에서 IR을 사용하기 위해 라이브러리 설치와 송수신 설정, 하드웨어 설정  
#LIRC라이브러리 설치  
```
$ sudo apt-get install lirc -y
```

#부트 로더를 설정하여 라즈베리 파이 시작 시 LIRC 모듈을 구동하도록 한다.   
#txt내용에서 아래의 내용을 주석 해제한다. pin번호 변경 가능하다.   
```
$ sudo nano /boot/config.txt
```
```
>>#Uncomment this to enable infrared communication.
>>dtoverlay=gpio-ir,gpio_pin=17 
>>#dtoverlay=gpio-ir-tx,gpio_pin=18
```
#하드웨어 모듈을 설정  
#명령어 입력 후 아래 코드를 작성한다.   
```
$sudo nano /etc/lirc/hardware.conf
```
```
>>LIRCD_ARGS="--uinput --listen"
>>LOAD_MODULES=true
>>DRIVER="default"
>>DEVICE="/dev/lirc0"
>>MODULES="lirc_rpi"
```

#LIRC 라이브러리의 driver, device옵션 값을 변경한다.  
```
$sudo nano /etc/lirc/lirc_options.conf
```
```
driver = default
device = /dev/lirc0
```
#재부팅 후 모듈이 잘 작동하는지 확인 (active가 됨을 확인)  
```
$sudo /etc/init.d/lircd status
```
#리모컨 신호를 받을 수 있도록 한다.  
```
$sudo mode2 -m -d /dev/lirc0
```

![image](https://user-images.githubusercontent.com/98154707/153116012-8a7456ed-083b-4191-be5d-32499b7ea080.png)  

신호가 정상적으로 수신 됨을 확인

리모컨 신호 등록  
https://blog.nakwonelec.com/2017/09/14/%EB%9D%BC%EC%A6%88%EB%B2%A0%EB%A6%AC%ED%8C%8C%EC%9D%B4-lirc%EB%A6%AC%EB%AA%A8%EC%BB%A8-%EC%86%A1%EC%88%98%EC%8B%A0-%EC%84%A4%EC%A0%95-2/

참고  
https://viewise.tistory.com/entry/%EC%A0%81%EC%99%B8%EC%84%A0-%EB%A6%AC%EB%AA%A8%EC%BD%98-IR-Remote-Controller-v1   
https://blog.aliencube.org/ko/2020/08/12/turning-raspberry-pi-into-remote-controller/



