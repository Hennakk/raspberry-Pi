from board import SCL, SDA
import busio
import adafruit_ssd1306

# I2C 인터페이스 생성
i2c = busio.I2C(SCL, SDA)

# SSD1306 OLED class 생성
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# addr parameter 변수를 사용하여 장치 주소를 변경할 수 있음
#display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x31)

# 디스플레이를 지움
display.fill(0)
#픽셀 변경 후 항상 호출하여 OLED에 표시
display.show()

#1bit color는 반드시 ‘1’ 모드로 이미지를 생성
image = Image.new("1", (display.width, display.height))

#이미지에 그릴 객체를 가져옴
draw = ImageDraw.Draw(image)

font = ImageFont.load_default()  #폰트 설정(기본폰트)

text = "Simple test"
draw.text((2, 16), text, font=font, fill=255)
display.image(image) # image함수 호출하여 표시

#세번째 파라미터는 ‘1’ 모드
display.pixel(0, 0, 1)    # (0.0) 위치에 픽셀을 set
display.pixel(64, 16, 1)  # (64,16)
display.pixel(127, 31, 1) # (127,31)
display.show()  #OLED에 출력 하기 위해 호출
