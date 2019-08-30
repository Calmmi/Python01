# -*- coding:utf-8 -*-
# Auth:小米  Date : 2019-08-30 0:10

# 验证码

import random,string
from PIL import Image,ImageFont,ImageDraw

# 制作验证码

class Captcha(object):
    """
    captcha_size:验证码图片尺寸
    font_size:字体大小
    text_number:验证码中字符个数
    line_number:线条个数
    background_color:验证码的背景颜色auth_code.py
    sources:取样字符集，验证码中的字符就是随机从这里选取的
    save_format:图片格式
    """
    def __init__(self,captcha_size=(200,100),font_size=50,text_number=4,line_number=4,background_color=(255,255,255),sources=None,save_format="png"):
        self.captcha_size = captcha_size
        self.font_size = font_size
        self.text_number = text_number
        self.line_number = line_number
        self.background_color = background_color
        self.save_format = save_format


        if sources:
            self.sources = sources
        else:
            # 获取所有的英文大小写和0-9的数字
            self.sources = string.ascii_letters + string.digits

    # 获取随机字符
    def get_text(self):
        text = random.sample(self.sources,k=self.text_number)
        return ''.join(text)

    # 随机获取绘制字符的颜色
    def get_font_color(self):
        font_color = (random.randint(0,150),random.randint(0,150),random.randint(0,150))
        return font_color

    # 随即获取干扰线条的颜色
    def get_line_color(self):
        line_color = (random.randint(0,250),random.randint(0,255),random.randint(0,250))
        return line_color

    # 编写绘制文字的方法
    def draw_text(self,draw,text,font,captcha_width,captcha_height,spacing=10):
        """
        在图片上绘制传入的字符
        :param draw: 画笔对象
        :param text: 绘制要显示的字符
        :param font: 字体对象
        :param captcha_width:验证码图片的宽度
        :param captcha_height: 验证码图片的高度
        :param spacing: 字符之间的间隙
        :return:
        """

        # 获取绘制字符的高度和宽度
        text_width,text_height = font.getsize(text)
        # 获取每个字符的大概宽度
        every_value_width = int(text_width / 4)
        # 获取要绘制的字符的长度
        text_length = len(text)
        # 获取字符之间的总的间隙长度
        total_spacing = (text_length - 1) * spacing

        if total_spacing + text_width >= captcha_width:
            raise ValueError("字符和间隙总长度超多图片长度")

        # 获取第一个字符的绘制位置
        start_width = int((captcha_width - text_width - total_spacing) / 2)
        start_height = int((captcha_height - text_height) / 2)

        # 依次绘制每个字符
        for value in text:
            position = start_width,start_height
            print(position)
            # 绘制text
            draw.text(position,value,font=font,fill=self.get_font_color())
            # 改变下一个字符开始绘制的位置
            start_width = start_width + every_value_width + spacing

    # 绘制线条的方法
    def draw_line(self,draw,captcha_width,captcha_height):
        """
        绘制线条
        :param draw: 画笔对象
        :param captcha_width: 验证码图片的宽度
        :param captcha_height: 验证码图片的高度
        :return:
        """

        # 随机获取开始的位置
        begin = ((random.randint(0,captcha_width / 2),random.randint(0,captcha_height)))
        end = ((random.randint(captcha_width / 2,captcha_width),random.randint(0,captcha_height)))
        draw.line([begin,end],fill=self.get_line_color())


    # 绘制小圆点
    def draw_point(self,draw,point_chance,captcha_width,captcha_height):
       """
       绘制小圆点
       :param draw: 画笔对象
       :param point_chance: 绘制小圆点的概率 point_chance/100
       :param captcha_width: 验证码图片的高度
       :param captcha_height: 验证码图片的宽度
       :return:
       """

       # 按照概率随即绘制小圆点
       for wd in range(captcha_width):
           for ht in range(captcha_height):
               tmp = random.randint(0,100)
               if tmp < point_chance:
                   draw.point((wd,ht),fill=self.get_line_color())

    # 制作验证码
    def make_captcha(self):
        # 获取验证码图片的宽度、高度
        width,height = self.captcha_size
        # 生成一张图片
        captcha = Image.new("RGB",self.captcha_size,self.background_color)
        # 获取字体对象
        font = ImageFont.truetype("C:\Windows\Fonts\Arial.ttf",self.font_size)
        # 获取画笔对象
        draw = ImageDraw.Draw(captcha)
        # 获取绘制的字符
        text = self.get_text()
        # 绘制字符
        self.draw_text(draw,text,font,width,height)
        # 绘制线条
        for i in range(self.line_number):
            self.draw_line(draw,width,height)

        # 绘制小圆点 10% 的概率
        self.draw_point(draw,10,width,height)
        # 保存图片
        captcha.save("captcha",format=self.save_format)

        # 显示图片
        captcha.show()

if __name__ == "__main__":
    Auth_Code = Captcha()
    Auth_Code.make_captcha()