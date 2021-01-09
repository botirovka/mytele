import time
from PIL import ImageDraw, Image, ImageFont
from datetime import datetime, timedelta

FONT_SIZE = 70
TEXT_Y_POSITION = 1
TEXT_X_POSITION = 1
Tashkent_UTC = 2 #укажите ваш часовой по€с 

def convert_time_to_string(dt):
    dt += timedelta(hours=Tashkent_UTC)
    return f"{dt.hour}:{dt.minute:02}"

def change_img():
    start_time = datetime.utcnow()
    text = convert_time_to_string(start_time)
    row = Image.new('RGBA', (200, 200), (50, 13, 62))# ÷вет фона black,white тд
    parsed = ImageDraw.Draw(row)
    font = ImageFont.truetype("HEADPLANE.ttf", FONT_SIZE)#стиль шрифта
    font2 = ImageFont.truetype("HEADPLANE.ttf", 20)
    parsed.text((int(row.size[0]*0.10), int(row.size[1]*0.31)), f'{text}', 
                 align="middle", font=font, fill=(217,2,238))
    parsed.text((55, 130),'Kiev time', # подтекст
                 align="middle", font=font2, fill=(241,98,255))
    row.save(f'time.png', "PNG")

if __name__ == '__main__':
    change_img()
