# from PIL import Image
# im = Image.open('E:\myPython\photos\AzoresPortugal_ZH-CN12684313303_1920x1080.jpg')
# print('图片信息:', im.format, im.size, im.mode)
# #生成缩略图
# im.thumbnail((200, 100))
# im.save('E:\myPython\photos\Thumb.jpg', 'JPEG')

# # 假设要处理学生的成绩表，为了表示一个学生的成绩。面向过程的程序可以用一个dict表示
# std1 = {"name": "lily", "score": 98}
# std2 = {'name': 'lisa', 'score': 97}
# # 而处理学生的可以通过函数实现，比如打印学生的成绩print('%s: %s' % (std['name'], std['score']))
# def print_score(std):
#     print('%s: %s' % (std['name'], std['score']))
# print_score(std1)
# print_score(std2)

# 如果要采用面向对象的程序设计思想，首先思考的不是程序的执行流程。
# 而是将student视为一个对象，这个对象用于name、score两种属性
# 如果需要打印一个学生的成绩，首先需要创建这个学生对应的对象。然后给对象发一个print_score的消息
# 让对象自己把自己的属性打印出来
# __init__ 初始化实例的值.这些值一般要供其他方法调用,只初始化值,不要返回值(就是别用return)
# 注意到__init__方法的第一个参数永远是self，表示创建的实例本身
# class student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
# # 封装数据
#     def print_score(self):
#         print('%s: %s' % (self.name, self.score))
# # 给对象发消息实际上就是调用对象对应的关联函数，我们称之为对象的方法。面向对象的程序写出来就像这样
# bart = student('bart Simpson', 99)
# lisa = student('lisa Simpson', 85)
# bart.print_score()
# lisa.print_score()

# ************************类和实例************************
# class后面紧接着是类名，类名一般首字母大写
# 然后是object，表示该类从哪里继承下来，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
class Student(object):
    pass
# 定义好Student类，就可以创建Student实例了，创建实例是通过类名加（）实现的
bart = Student()
# 可以自由的给实例变量绑定属性
bart.name = 'bart Simpson'
print(bart.name)


