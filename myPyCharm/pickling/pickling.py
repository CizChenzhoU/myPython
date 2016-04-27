# 序列化
# 变量从内存中变为可存储或传输的过程称之为序列化，在Python中Pickling
# 在其他语言中也被称之为serialization，marshalling，flattening等等
# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling

# 把一个对象序列化并写入文件：
# import pickle
#
# d = dict(name='Bob', age=20, score=88)
# pickle.dumps(d)

# pickle.dumps()方法吧任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
# 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object
# f = open('E:/myPython/myPyCharm/pickling/pickling.txt', 'wb')
# pickle.dump(d, f)
# f.close()
#
# # 看看写入的dump.txt文件，一堆乱七八糟的内容，这些都是Python保存的对象内部信息
# # 当我们要吧对象从磁盘读到内存时，可以先把内容读到一个bytes,然后用pickle.loads()方法反序列化出对象
# # 也可以直接用pickle.load()方法从一个file-like Object直接反序列化出对象
# f = open('E:/myPython/myPyCharm/pickling/pickling.txt', 'rb')
# d = pickle.load(f)
# f.close()
# print(d)

# JSON
# 如果我们要在不同的语言之间传递对象，就必须把对象序列化为标准格式
# 比如xml,但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串
# 可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式
# 并且比XML更快，而且可以直接在Web页面中读取，非常方便。

# JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：
# import json
# d = dict(name='Bob', age=20, score=88)
# print(json.dumps(d))

# JSON标准规定JSON编码是UTF-8
# Python的dict对象可以直接序列化为JSON的{},不过，很多时候，我们更喜欢用class表示对象，然后再序列化
# import json
#
#
# class Student(object):
#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score
#
# def student2dict(std):
#     return {
#         'name': std.name,
#         'age': std.age,
#         'score': std.score
#     }
#
# s = Student('Bob', 20, 88)
# print(json.dumps(s, default=student2dict))
#
# # 如果我们要把JSON反序列化为一个student对象实例，loads()方法首先转换出一个dict对象
# # 然后，我们传入的object_hook函数负责把dict转化为Student实例
# def dict2student(d):
#     return Student(d['name'], d['age'], ['score'])
#
# # 运行
# json_str = '{"age":20,"score":88,"name":"Bob"}'
# print(json.loads(json_str,object_hook=dict2student)) # 打印出的是反序列化的Student实例对象

# 小结
# Python语言特定的序列化模块是pickle，但如果要把序列化搞的更通用、更符合Web标准，就可以使用json模块
# json模块的dumps()和loads()函数是定义得非常好的接口的典范。当我们使用时，只需要传入一个必须的参数
# 但是，当默认的序列化或反序列机制不满足我们的要求时，我们又可以传入更多的参数来定制序列化或反序列化的规则
# 既做到了接口简单易用，又做到了充分的扩展性和灵活性。






