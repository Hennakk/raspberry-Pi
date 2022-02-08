from board import SCL, SDA
import busio
from PIL import Image
import adafruit_ssd1306

# I2C 활성화
i2c = busio.I2C(SCL, SDA)

# Create the SSD1306 OLED class.
#처음 두개의 파라미터는 픽셀의 넓이와 높이로 만약 디스플레이의 사이즈가 다르다면 이부분을 수정
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Clear display.
disp.fill(0)
disp.show()

# OLED사이즈로 크기를 조정, 1bit color로 변환
image = Image.open('dog.png').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')

#다른 형식(ppm)의 이미지 로드 할 때
#image=Image.open("happycat_oled_32.ppm").convert("1")

# Display image.
disp.image(image)
disp.show()
