from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# Reset Pin 초기화
oled_reset = digitalio.DigitalInOut(board.D4)

#디스플레이 사이즈
WIDTH = 128
HEIGHT = 32  # Change to 64 if needed
BORDER = 5

# I2C 사용 설정
i2c = busio.I2C(SCL, SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# 디스플레이 화면 reset
oled.fill(0)
oled.show()

# Create blank image for drawing.
# 1-bit color를 위해 모드를 1로 설정
image = Image.new("1", (oled.width, oled.height))

# 출력할 객체를 가져옴
draw = ImageDraw.Draw(image)

# 기본 폰트로 설정
#font = ImageFont.load_default()
#다른 폰트와 글씨크기로 설정
font = ImageFont.truetype('PixelOperator.ttf', 16)

#이름 텍스트 출력
text = "Hyun A"
(font_width, font_height) = font.getsize(text)
draw.text((0,2),text,font=font,fill=255)

# 출력하기 위해 필수
oled.image(image)
oled.show()
