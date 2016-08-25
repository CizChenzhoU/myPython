# 除了内建的模块外，Python还有大量的第三方模块
# 基本上，所有的第三方模块都会在PyPI - the Python Package Index上注册，只要找到对应的模块名字，即可用pip安装。

# PIL:Python Imaging Library 已经是Python平台事实上的图像处理标准库了。PIL功能非常强大，但API却非常简单易用。
# 由于PIL仅支持到Python2.7,加上年久失修，于是一群志愿者在PIL的基础上创建了兼容的版本，名字叫Pillow,支持最新Python3.x,又加入了许多新特性
# 因此，我们可以直接安装使用Pillow

# 安装Pillow
# 操作图像
# 来看看最常见的图像缩放操作，只需要三四行代码
# from PIL import Image
#
# # 打开一个jpg图像文件，注意是当前路径
# img = Image.open('C:/Users/chenz/Desktop/thumbnail.jpg')
# # 获得图像尺寸
# w,h = img.size
# print('LuHan image size: %sx%s' %(w,h))
# # 缩放到50%
# img.thumbnail((w//2, h//2))
# print('Resize image to: %sx%s' % (w//2, h//2))
# # 把缩放后的图像用jpeg格式保存:
# img.save('thumbnail.jpg', 'jpeg')

# 其他功能如切片、旋转、滤镜、输出文字、调色板等一应俱全。
# 比如，模糊效果也只需要几行代码
# from PIL import Image,ImageFilter
#
# # 打开一个jpg图像文件，注意是当前路径
# img = Image.open('C:/Users/chenz/Desktop/thumbnail.jpg')
# # 应用模糊滤镜 //BLUR 模糊 //CONTOUR 轮廊
# img2 = img.filter(ImageFilter.BLUR)
# img2.save('blur.jpg','jpeg')

# PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图。比如要生成字母验证码图片、
from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random
try:
    # 随机字母
    def radChar():
        return chr(random.randint(65,90))

    # 随机颜色
    def radColor():
        return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

    # 随机颜色2
    def radColor2():
        return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

    # 240 * 60

    width = 60 * 4
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建Font对象
    font = ImageFont.truetype('C:/Windows\WinSxS/amd64_microsoft-windows-font-truetype-arial_31bf3856ad364e35_10.0.10586.0_none_ff09088857b2471d/Arial.ttf',36)
    # 创建Draw对象
    draw = ImageDraw.Draw(image)
    # 填充每个像素
    for x in range(width):
        for y in range(height):
            draw.point((x,y),fill=radColor())
    # 输出文字:
    for t in range(4):
        draw.text((60 * t + 10, 10), radChar(), font=font, fill=radColor2())

    # 模糊
    image = image.filter(ImageFilter.BLUR)
    image.save('C:/Users/chenz/Desktop/blur.jpg','jpeg')
except Exception:
    print("The second number can't be zero!")


#要详细了解PIL的强大功能，请请参考Pillow官方文档：

#https://pillow.readthedocs.org/