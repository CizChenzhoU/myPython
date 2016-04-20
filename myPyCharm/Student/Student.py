# *********************面向对象高级编程**************************
# 数据封装、继承和多态只是面向对象程序设计中最基本的3个概念
# 在Python中，面向对象还有很多高级特性，允许我们写出非常强大的功能
# 我们会讨论多重继承、定制类、元类等概念
# class Student(object):
#     pass
#
#
# # 尝试给实例绑定一个属性
# s = Student()
# s.name = 'Michael'  # 动态给实例绑定一个属性
# print(s.name)
#
# # 还可以给实例绑定一个方法
# def set_age(self, age):
#     self.age = age
#
#
# from types import MethodType
#
# s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
# s.set_age(25)  # 调用实例方法
# print(s.age)  # 测试结果
#
# # 为了给所有实例都绑定方法，可以给class绑定方法
# def set_score(self, score):
#     self.score = score
#
#
# Student.set_score = set_score
#
# s.set_score(100)
# print(s.score)
#
# s2 = Student()
# s2.set_score(99)
# print(s2.score)

# # 使用__slots__
# # 但是，如果想要限制实例的属性怎么处理？比如，只允许对Student实例添加name和age属性
# # 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
# class Student(object):
#     __slots__ = ('name', 'age') # 用tuple定义预习绑定的属性名称
#
# s = Student() # 创建新的实例
# s.name = 'Michael' # 绑定属性‘name’
# s.age = 25 # 绑定属性 ‘age’
#
# # 由于‘score’没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误
# # 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类不起作用的

# 使用@property
# class Student(object):
#     def get_score(self):
#         return self._score
#
#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0` 100!')
#         self._score = value
#
#
# s = Student()
# s.set_score(60)  # ok!
# print(s.get_score())
# s.set_score(9999)

# 但是，上面的调用方法又略显复杂，没有直接用属性这么直接简单
# 有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量？
# 对于追求完美的Python程序员来说，这是必须要做到的！
# 还记得装饰起（decorator）可以给函数动态加上功能吗？
# 对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的；

# class Student(object):
#     @property
#     def score(self):
#         return self._score
#     @score.setter
#     def score(self,value):
#         if not isinstance(value,int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~100')
#         self._score = value
# # @property实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，只需要加上@property就可以了，
# # 此时，@property本身又创建了另一个装饰器@score.setter,负责把一个setter方法变成属性赋值，于是
# # 我们就拥有一个可控的属性操作
# s = Student()
# s.score = 60 # ok，实际转化为s.set_score(60)
# print(s.score) #ok ,实际转化为s.get_score()
# s.score = 9999

# 注意到这个神奇的@property,我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的
# 而是通过getter和setter方法来实现的
# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性
class Student(object):
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self,value):
        self._birth = value
    @property
    def age(self):
        return 2015 - self._birth

# 上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来

# 小结
# @property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查
# 这样，程序运行时就减少了出错的可能性

# 练习
# 请利用@property给一个screen对象加上width和height属性，以及一个只读属性resolution
# -*- coding: utf-8 _*_

# test:
# s = Screen()
# s.width = 1024
# s.height = 768
# print(s.resolution)
# assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution
class Screen(object):
    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be an integer!')
        if value < 0:
            raise ValueError('width must be >0!')
        self._width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('height must be an integer!')
        if value < 0:
            raise ValueError('height must be >0!')
        self._height = value

    @property
    def resolution(self):
        return self._width * self.height


s = Screen()
s.width = 1024
s.height = 768

print(s.width, s.height)
print(s.resolution)
