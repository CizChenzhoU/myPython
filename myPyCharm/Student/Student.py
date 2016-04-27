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
#
# from enum import Enum
#
# Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#
# for name, member in Month.__members__.items():
#     print(name, '==>', member, ',', member.value)

# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
# from enum import Enum,unique
#
# @unique
# class WeekDay(Enum):
#     Sun = 0 # Sun的value被设定为0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6
# @unique装饰器可以帮助我们检查保证没有重复值
# 访问这些枚举可以有若干中方法
# day1 = WeekDay.Mon
# print(day1)
# print(WeekDay.Mon.value)

# 可见，既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量
# 小结
# Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较

# *************************使用元类****************************
# type
# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的
# 比方说我们要定义一个Hello的class，就写一个hello.py模块
# class Hello(object):
#     def hello(self,name='world'):
#         print('Hello,%s.' % name)

# 当Python解释器载入hello模块时，就会依次指向该模块的所以语句，执行结果就是动态创建
# 出一个Hello的class对象，测试如下：
#from hello import Hello
# h = Hello()
# h.hello() # Hello ,world
# print(type(Hello))
# type()函数可以查看一个类型或变量的类型，Hello是一个class
# 它的类型就是type,而h是一个实例，它的类型就是class Hello

# 我们说class的定义是运行时动态创建的，而创建class的方法就是使用type()函数
# type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如
# 我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)..的类型

# 要创建一个class对象，type()函数依次传人3个参数
# 1.class的名称 2.继承的父类集合，注意Python支持多重继承，如果只要一个父类，别忘了tuple的单元素写法
# 3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上

# 通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法
# 然后调用type()函数创建出class

# 正常情况下，我们都用class Xxx.. 来定义类，但是，type()函数也允许我们动态创建出类来，也就是说
# 动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同，要在静态语言运行期创建类，必须构造源代码字符串
# 再调用编译器，或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂。

# metaclass
# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass
# metaclass,直译为元类，简单的解释就是
# 当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例
# 但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass,然后创建类
# 连接起来就是，先定义metaclass,就可以创建类，最后创建实例
# 所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的实例
# metaclass是Python面向对象里最难理解的，也是最难使用的魔术代码。正常情况下，你不会碰到需要使用metaclass
# 的情况

# 先看一个简单的例子，这个metaclass可以给我们自定义的Mylist增加一个add方法
# 定义ListMetaclass,按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass

# # metaclass是类的模版，所以必须是从‘type’类型派生
# class ListMetaclass(type):
#     def __new__(cls,name,bases,attrs):
#         attrs['add'] = lambda self ,value :self.append(value)
#         return type.__new__(cls,name,bases,attrs)
#
# # 有了ListMetaclass,我们在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass:
# class MyList(list,metaclass=ListMetaclass):
#     pass
#
# # 当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，
# #  要通过ListMetaclass.__new__()来创建，在此，我们可以修改类的定义，比如，加上新的方法，
# # 然后，返回修改后的定义
# # __new__()方法接收到的参数依次是：
# # 1.当准备创建的类的对象；
# # 2.类的名字
# # 3.类继承的父类集合；
# # 4.类的方法集合。
# # 测试一下MyList是否可以调用add()方法
# L =MyList()
# L.add(1)
# print(L)
# 动态修改有什么意义？直接在MyList定义中写上add()方法不是更简单吗？
# 正常情况下，确实应该直接写，通过metaclass修改纯属变态。
# 但是，总会遇到通过metaclass修改类定义的，ORM就是一个典型的例子。
# ORM全称“Object Relational Mapping”,即对象-关系映射，就是把关系数据库的
# 一行映射为一个对象，也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句
# 要编写一个ORM框架，所以的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。
# 让我们来尝试编写一个ORM框架
# 编写底层模块的第一步，就是先把调用的接口写出来。比如，使用这如果使用这个ORM框架
# 想定义一个User类来操作对应的数据库表User,我们期待他写出这样的代码

# *******************错误处理**********************
# 高级语言通常设置了一套try...except.....finally....的错误处理机制，Python也不例外
# try:
#     print('try....')
#     r = 10 / 0
#     print('result:',r)
# except ZeroDivisionError as e:
#     print('except',e)
# finally:
#     print('finally....')
# print('END')

# 当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行
# 而是直接跳转至错误处理代码，即except语句，执行完except后，如果有finally语句块，则执行finally语句块
# 至此，执行完毕。

# 上面的代码在计算10 / 0时会产生一个除法运算错误：
# 输出
# try...
# except: division by zero
# finally...
# END
# 从上面输出可以看到，当错误发生时，后续语句print('result:',r)不会被执行
# except由于捕获到ZeroDivisionError,因此被执行。最后，finally语句被执行。然后程序继续按照流程往下走
# 如果把除数 0 改成 2，则执行结果如下
# try...
# result: 5
# finally...
# END
# 由于没有错误发生，所以except语句块不会被执行，但是finally如果有，则一定会被执行（可以没有finally语句）
# 错误应该有很多种类，如果发生了不同种类的错误，应该由不同的except语句块处理。
# try:
#     print('try....')
#     r = 10 /int('a')
#     print('result:',r)
# except ValueError as e:
#     print('ValueError:',e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:',e)
# finally:
#     print('finally...')
# print('END')

# int()函数可能会抛出ValueError,所以我们用一个except捕获ValueError,用另一个except捕获ZeroDivisionError
# 此外，如果没有错误发生，可以在except语句后面加上一个else，当没有错误发生执行else语句
# try:
#     print('try...')
#     r = 10 / int('2')
#     print('result:',r)
# except ValueError as e:
#     print('ValueError:',e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:',e)
# else:
#     print('no error!')
# finally:
#     print('finally...')
# print('END')

# Python的错误其实也是class，所有的错误类型都继承自BaseException,所以在使用except时
# 需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。

# *******************文件读写**********************
# Python内置了读写文件的函数，用法和C是兼容的
# 读写文件前，我们先了解一下，在磁盘上读写文件的功能都是由操作系统提供的，现代操作系统不允许普通程序直接
# 操作磁盘，所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），然后，通过操作系统提供
# 的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）

# # 读文件
# # 要读取文件的模式打开一个文件对象，使用Python内置的open()函数，传人文件名和标示符：
# f = open('E:\myPython\myNotepad++\gitIsFree.txt', 'r')
# # 读取文件
# f.read()
# # 关闭文件
# f.close()

# 由于文件读写是都有可能产生IOError，一旦出错，后面的f.close()就不会调用。所以，为了保证无论是否出错都能正确地
# 关闭文件，我们可以使用try .....finally来实现
# try:
#     f = open('E:\myPython\myNotepad++\gitIsFree.txt', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()
# 但是每次都这么写实在太繁琐，所以，Python引人了with语句来自动帮我们调用close（）方法
# with open('E:\myPython\myNotepad++\gitIsFree.txt', 'r') as f:
#     print(f.read())
# 限制每次读取字节大小，防止内存溢出
# with open('E:\myPython\myNotepad++\gitIsFree.txt', 'r') as f:
#     print(f.read(20))
# # 每次读取一行
# with open('E:\myPython\myNotepad++\gitIsFree.txt', 'r') as f:
#     print(f.readline())
# # 读取所有内容并返回list
# with open('E:\myPython\myNotepad++\gitIsFree.txt', 'r') as f:
#    for f1 in f.readlines():
#        print(f1.strip()) # 把末尾的‘\n’删掉
# 如果文件很小，read()一次性读取最方便
# 如果不确定文件大小，反复调用read（size）比较保险
# 如果配置文件，调用readlines()最方便

# file-like Object
# 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object
# 除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承
# 只要写个read()方法就行。

# StringIO就是在内存中创建的file-like Object,常用作临时缓冲。

# 二进制文件
# 前面讲的默认都是读取文本文件，并且是UTF-8编码的文件，要读取二进制文件，比如图片、视频等等，用'rb'
# 打开文件即可
# f = open('/Users/michael/test.jpg', 'rb')
# f.read()
# 输出 b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00...' # 十六进制表示的字节
# 字符编码
# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件
# with open('E:\myPython\myNotepad++\gitIsFree.txt', 'r', encoding='UTF-8') as f:
#     print(f.read())

# 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError,因为在文本中可能夹杂了一些非法编码的字符
# 遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。
# 最简单的方式是直接忽略
# with open('E:\myPython\myNotepad++\gitIsFree.txt', 'r', encoding='gbk', errors='ignore') as f:
#     print(f.read())

# 写文件
# with open('E:\myPython\myNotepad++\gitIsFree.txt', 'w',encoding='UTF-8',errors='ignore') as f:
#     f.write('Hello, world!')
#     f.write('中国')

# *************************StringIO和BytesIO******************************
# StringIO顾名思义就是在内存中读写str
# from io import StringIO
# f = StringIO()
# f.write('hello')
# f.write(' ')
# f.write('world!')
# print(f.getvalue())
# 读取IO
# f = StringIO('Hello!\nHi!\nGoodbye!')
# while True:
#     s = f.readline()
#     if s =='':
#         break
#     print(s.strip())
# BytesIO
# StringIO操作只能是str,如果要操作二进制数据，就需要使用BytesIO
# BytesIO实现了在内存中读写bytes
# 我们创建一个BytestIO,然后写入一些bytes:
# from io import BytesIO
# f = BytesIO()
# f.write('中文'.encode('utf-8'))
# print(f.getvalue())
# 注意，写入的不是str,而是经过UTF-8编码的bytes
# 和StringIO类似，可以用一个bytes初始化BytesIO,然后，像文件一样读取。
# from io import BytesIO
# f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
# f.read()

# **************************操作文件和目录*********************************
# Python内置的os模块也可以直接调用操作系统提供的接口函数
import os

# print(os.name)  # 输出nt 注：posix,说明系统是Linux、Unix或者是nt,就是Window系统

# 获取详细的系统信息
# os.uname() 注意uname()函数在Window上不提供，也就是说，os模块的某些函数是跟操作系统相关的。

# 环境变量
# 查看环境变量
# os.environ
# 获取某个环境变量的值
# print(os.environ.get('PATH'))
# print(os.environ.get('x', 'default'))

# 操作文件和目录
# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中
# 这一点要注意一下。查看、创建和删除目录可以这么调用

# 查看当前目录的绝对路径：
# print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来。
#print(os.path.join('E:\myPython\myPyCharm\Student', 'testdir'))
# 然后创建一个目录
#os.mkdir('E:\myPython\myPyCharm\Student/testdir')
# 然后删除一个目录
# os.rmdir('E:\myPython\myPyCharm\Student/testdir')
# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数
# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数

# # os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
# print(os.path.splitext('E:/myPython/myPyCharm/Student/test.txt'))
# # 文件重命名
# # os.rename('E:/myPython/myPyCharm/Student/test.txt', 'E:/myPython/myPyCharm/Student/text.py')
# # 删除文件
# os.remove('E:/myPython/myPyCharm/Student/text.py')

# 最后看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码：
# print([x for x in os.listdir('.') if os.path.isdir(x)])
# 要列出所有的.py文件，也只需一行代码：
# print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

# 小结
# Python的os模块封装了操作系统的目录和文件操作。要注意这些函数有的在os模块中，有的在os.path模块中

# 练习
# 利用os模块编写一个能实现dir -1的输出程序
# 编写一个程序，能在当前目录已经当前目录的所以子目录下查找文件名包含指定字符串的文件，并打印出相对路径。

# str:查找的字符串
# path:路径，默认为当前路径
# the_path:相对路径
# def what_file(str, path='.', the_path='\\'):
#     for p in os.listdir(path):
#         # 当前文件的全路径
#         current_file = os.path.join(path, p)
#         # 是否存在str字符串
#         if str in p and os.path.isfile(current_file):
#             print(p, os.path.join(the_path, p))  # 输出相对路径
#         # 当前路径是否一个文件夹
#         if os.path.isdir(current_file):
#             # 是文件夹递归，并将相对路径加上p
#             what_file(str, current_file, os.path.join(the_path, p))
#
# # 调用
# what_file("py", "E:/myPython/myPyCharm")


