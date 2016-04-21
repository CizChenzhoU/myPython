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
# class Student(object):
#     @property
#     def birth(self):
#         return self._birth
#     @birth.setter
#     def birth(self,value):
#         self._birth = value
#     @property
#     def age(self):
#         return 2015 - self._birth

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
# class Screen(object):
#     @property
#     def width(self):
#         return self._width
#
#     @property
#     def height(self):
#         return self._height
#
#     @width.setter
#     def width(self, value):
#         if not isinstance(value, int):
#             raise ValueError('width must be an integer!')
#         if value < 0:
#             raise ValueError('width must be >0!')
#         self._width = value
#
#     @height.setter
#     def height(self, value):
#         if not isinstance(value, int):
#             raise ValueError('height must be an integer!')
#         if value < 0:
#             raise ValueError('height must be >0!')
#         self._height = value
#
#     @property
#     def resolution(self):
#         return self._width * self.height
#
#
# s = Screen()
# s.width = 1024
# s.height = 768
#
# print(s.width, s.height)
# print(s.resolution)

# *********************定制类**************************
# class Student(object):
#     def __init__(self,name):
#         self.name = name
#
# print(Student('Michael'))

# 输出<__main__.Student object at 0x000001C0B107E320>
# 怎样才能打印得好看呢？只需要定义好__str__()方法，返回一个好看的字符串就可以了
# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return 'Student object(name : %s)' % self.name


# print(Student('Michael'))

# 输出Student object(name : Michael)

# # 但是细心的朋友会发现直接敲变量不用print,打印出来的实例还是不好看
# s = Student('Michael')
# s
#
# # 这是因为直接显示变量调用的不是__str__(),而是__repr__(),两者的区别是__str__()返回用户看到的字符串
# # 而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调式服务的。
# # 解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法
#
# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return 'Student object (name = %s)' % self.name
#
#     __repr__ = __str__


# __iter__
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
# 该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法
# 拿到下一个值，直到遇到StopIteration错误时退出循环
# 我们以斐波那契数列为例，写一个Fib类，可以作用于循环：
# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1  # 初始化两个计数器a,b
#
#     def __iter__(self):
#         return self  # 实例本身就是迭代对象，故返回自己
#
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b  # 计算下一个值
#         if self.a > 100000:  # 退出循环的条件
#             raise StopIteration()
#         return self.a  # 返回下一个值
#
# # 现在，试试把Fib实例作用于for循环
# for n in Fib():
#     print(n)

# __getitem__
# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把他当成list来使用还是不行，比如，取第5个元素
# 要表现得想list那样按照下标取出元素，需要实现__getitem__()方法:
# class Fib(object):
#     def __getitem__(self, n):
#         a, b = 1, 1
#         for x in range(n):
#             a, b = b, a + b
#         return a
#
# # 现在，就可以按下标访问数列的任意一项了：
# f = Fib()
# print(f[0])
# print(f[1])
# print(f[2])
# print(f[3])

# 但是list有个神奇的切片方法：
# print(list(range(100))[5:10])

# 对于Fib报错。原因是__getitem__()传人的参数可能是一个int,也可能是一个切片对象slice，所以要做判断
# class Fib(object):
#     def __getitem__(self, item):
#         if isinstance(item, int):  # item是索引
#             a, b = 1, 1
#             for x in range(item):
#                 a, b = b, a + b
#             return a
#         if isinstance(item, slice):  # item是切片
#             start = item.start
#             stop = item.stop
#             if start is None:
#                 start = 0
#             a, b = 1, 1
#             L = []
#             for x in range(stop):
#                 if x >= start:
#                     L.append(a)
#                 a, b = b, a + b
#             return L
#
#
# f = Fib()
# print(f[0:5])
# print(f[:10])


# __getattr__
# 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错，比如定义Student类

# class Student(object):
#     def __init__(self):
#         self.name = 'Michael'
#
# # 调用name属性，没问题，但是，调用不存在的score属性，就有问题了
# s = Student()
# print(s.name)
# print(s.score)
# 错误信息很清楚告诉我们，没有找到score这个attribute
# 要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，那就是写一个
# __getattr__()方法，动态返回一个属性。修改如下
# class Student(object):
#     def __init__(self):
#         self.name = 'Michael'
#
#     def __getattr__(self, attr):
#         if attr == 'score':
#             return 99
#
#
# # 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self,'score')来尝试获得属性
# # 这样，我们就有机会返回score的值
#
# s = Student()
# print(s.name)
# print(s.score)
#
# # 返回函数也可以这样写
#
# class Students(object):
#     def __getattr__(self, attr):
#         if attr == 'age':
#             return lambda: 25
#
# # 只是调用方式要变为：
# s1 =Students()
# print(s1.age())

# 注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name,不会在__getattr__中查找
# 此时，注意到任意调用如s.abc都会返回None,这是因为我们定义的__getattr__默认返回就是None.
# 要让class值响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误：
# class Student1(object):
#     def __getattr__(self, attr):
#         if attr == 'age':
#             return lambda: 25
#         raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

# 这时间上可以把一个类的所以属性和方法调用全部动态化处理了，不需要任何特殊手段
# 这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况作调用
# 举个例子：
#
# 现在很多网站都搞REST API，比如新浪微博、豆瓣啥的，调用API的URL类似：
#
# http://api.server/user/friends
# http://api.server/user/timeline/list
# 如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。
#
# 利用完全动态的__getattr__，我们可以写出一个链式调用：
#
# class Chain(object):
#     def __init__(self,path=''):
#         self._path = path
#     def __getattr__(self, path):
#         return Chain('%s/%s'%(self._path,path))
#     def __str__(self):
#         return self._path
#
#     __repr__ = __str__
#
# print(Chain().status.user.timeline.list) # 输出：/status/user/timeline/list
#
# # 这样，无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且，不随API的增加而改变！
# # 还有些REST API会把参数放到URL中，比如GitHub的API: GET /users/:user/repos
# # 调用时，需要把：users替换为实际用户名。如果我们能写出这样的链式调用：
# print(Chain().users('michael').repos)

# __call__
# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用
# 能不能直接在实例本身上调用呢？在Python中是肯定的
# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。

# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __call__(self):
#         print('My name is %s.' % self.name)
#
#
# s = Student('Micheal')
# s()
# __call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样
# 所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没什么根本的区别
# 如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的
# 这样一来，我们就模糊了对象和函数的界限。
# 那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，
# 能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例：
# print(callable(s))
# print(callable(max))
# print(callable([1, 2, 3]))
# print(callable(None))
# print(callable('str'))

# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象

