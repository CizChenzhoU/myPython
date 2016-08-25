from PIL import Image

img = Image.open('C:/Users/chenz/Desktop/1.jpg')
img = img.resize((60, 140), Image.NEAREST)

# 打开图片
hight, weigh = img.size

# ascii_char = list("$@&#{}/|-_+~<>i!lI;:,\"^`'. ")

# ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

ascii_char = ['##', '@@', '%%', 'QQ', 'SS',
               'UU', 'OO', '??', '', 'oo',
               '++', '--', '::', '..', '  ']

# 将256灰度映射到70个字符上
def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]


txt = ""

for i in range(hight):
    for j in range(weigh):
        a = (i, j)
        txt += get_char(*img.getpixel(a))
    txt += '\n'


print(txt)
input()


