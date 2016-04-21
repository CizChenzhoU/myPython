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

# # ************************类和实例************************
# # class后面紧接着是类名，类名一般首字母大写
# # 然后是object，表示该类从哪里继承下来，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
# class Student(object):
#     pass
# # 定义好Student类，就可以创建Student实例了，创建实例是通过类名加（）实现的
# bart = Student()
# # 可以自由的给实例变量绑定属性
# bart.name = 'bart Simpson'
# print(bart.name)

# # ************************访问限制************************
# # 在class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，
# # 这样就隐藏了内部复杂逻辑
# # 但是从Student类的定义来看，外部代码可以自由地修改一个实例的name、score属性
# # 建立一个Student类
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
# # 封装数据
#     def print_score(self):
#         print('%s: %s' % (self.name, self.score))
# # 修改实例属性
# Bart = Student('Bart Simpson', 98)
# # 输出
# print(Bart.score)
# # 修改实例属性
# Bart.score = 88
# print(Bart.score)
# # 如果要让内部属性不被外部访问，可以在属性名称前加上__,在python中，实例的变量名如果以__开头
# # 就变成了一个私有变量private，只有内部访问，外部无法访问。Student类可以这样改一改
# class Student(object):
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score
#
#     # 封装数据
#     def print_score(self):
#         print('%s:%s' % (self.__name, self.__score))
#
# # 继续修改实例属性会发现提示报错AttributeError:'Student' object has no attribute 'score'
# # 找不到属性，因为属性已经被私有了。
# Bart = Student('Bart Simpson', 99)
# print(Bart.score)

# # 这样就确保了外部代码不能随意修改对象内部状态，这样通过访问限制的保护，代码更加健壮。
# # 但是如果外部需要获得内部的name、score怎么处理？
# # 可以给Student增加get_name和get_score方法
# # 但是如果又允许外部修改name、score怎么处理？
# # 可以给Student增加set_name和set_score方法
# class Student(object):
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score
#
#     # 封装数据
#     def print_score(self):
#         print('%s:%s' % (self.__name, self.__score))
#
#     def get_name(self):
#         return self.__name
#
#     def get_score(self):
#         return self.__score
#
#     def set_name(self, name):
#         self.__name = name
#
#     def set_score(self, score):
#         self.__score = score
#
#
# Bart = Student('Bart Simpson', 98)
# Bart.set_name('Lisa')
# Lisa = Bart.get_name()
# print(Lisa)
#
# # 为什么需要通过set/get方法而不直接使用Stendent.name='Lisa'。
# # 因为在方法中可以对参数进行检查，避免无效参数的传人
# class Student(object):
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score
#
#     # 封装数据
#     def print_score(self):
#         print('%s:%s' % (self.__name, self.__score))
#
#     def get_name(self):
#         return self.__name
#
#     def get_score(self):
#         return self.__score
#
#     def set_name(self, name):
#         self.__name = name
#
#     def set_score(self, score):
#         if 0<= score <=100:
#             self.__score = score
#         else:
#             raise ValueError('Bad score')
#
#
# Bart = Student("Bart Simpson", 75)
# print(Bart)
# Bart.set_score(10)
# print(Bart.get_score())

# 小结
# 需要注意的是，在Python中，变量名类似__**__的，也就是以双下划线开头，并且以双下划线结尾，是特殊变量
# 特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名称

# 有时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是
# 按照约定成俗的规定，当你看到这样的变量时，意思就是，"虽然我可以被访问，但是，请把我视为私有变量，不要随意访问"

# 注：双下划线开头的变量是不是一定不能从外部访问呢?其实也不是。不能直接访问__name
# 是因为Python解释器对外把__name变量改成了_Student__name，所以,
# 仍然可以通过_Student__name来访问__name变量 ：Bart._Student__name
# 但是强烈不建议如此处理，因为不同版本的Python解释器可能会把__name改成不同的变量名

# # ************************获取对象************************
# 使用type 判断对象类型
# print(type(124))  # 输出<class 'int'>
# print(type('str'))  # 输出<class 'str'>
# print(type(None))  # 输出<class 'NoneType'>

# 但是type()函数返回的是什么类型？它返回对应的Class类型。如果我们要在if语句中判断，
# 就需要比较两个变量的type类型是否相同
# print(type(123) == type(456))
# print(type(123) == int)
# print(type('str') == type('abc'))
# print(type('SSS') == str)
# print(type('str') == type(123))
# 使用dir()
# 如果要获得一个对象的所以属性和方法，可以使用dir()函数，它返回一个保护字符串的list
# print(dir('abc'))
# print('--------------------')
# print(dir(123))

