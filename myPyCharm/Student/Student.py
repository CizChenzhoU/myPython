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

# 使用__slots__
# 但是，如果想要限制实例的属性怎么处理？比如，只允许对Student实例添加name和age属性
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义预习绑定的属性名称

s = Student() # 创建新的实例
s.name = 'Michael' # 绑定属性‘name’
s.age = 25 # 绑定属性 ‘age’

# 由于‘score’没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类不起作用的
