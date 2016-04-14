# print('hello word');
# print('the quick brown fox' ,'jumps over', 'the lazy dog');
# print('100+200=',100+200);
# #name=input();
# #print('hello',name);
# print('1024*786=',1024*786);
# #print absolute value of an integer:
# a=100
# if a>=0:
	# print(a)
# else:
	# print(-a)
	
# print('i\'m\ "OK\"!');

# x=10;
# x=x+10;
# print(x);
# a='abc';
# b=a;
# a='cdf';
# print(a+'分割'+b);

# print('小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出xx.x%，只保留小数点后1位：')

# s1 = 72

# s2 = 85

# r = (s2 - s1)/s2*100

# print('%.1f %%'% r)

# classmates=['Michael','Bol','Tracy']
#  print(len(classmates))
#  print(classmates[1]+'第一个')
#  print(classmates[-1]+'倒数第二个')
#  for s in classmates:
	# print(s)

# print('---追加一个到末尾--------------')
# classmates.append('lily')
# print(classmates)
# print('----追加一个到指定位置-----------')
# classmates.insert(1,'dengdeng')
# print(classmates)
# print('---删除末尾的元素--')
# classmates.pop()
# print(classmates)
# print('-------删除指定元素---------------')
# classmates.pop(1)
# print(classmates)
# print('----------替换某个元素----------------')
# classmates[1]='Sarah'
# print(classmates)

# ***************************#二维数组***************************
# s=['python','java',['asp','php'],'scheme']
# print(len(s))
# #另一种写法
# p=['asp','php']
# z=['python','java',p,'scheme']
# #要拿到php可以写p[1]或者z[2][1]
# print(z[2][1])

# L=[['Apple','Google','Microsoft'],['JAVA','Python','Ruby','PHP'],['Adam','Bart','Lisa']]
# print('打印Apple:'+L[0][0])
# print('打印Lisa:'+L[2][2])
# print('打印Python:'+L[1][1])

# print('my debug')

# age =20;
# if age>=18:
	# print("your age is",age)
	# print("adult")

# ageTwo=2	
# if ageTwo>=18:
	# print ("your age is",ageTwo)
	# print("adult")
# else:
	# print("your age is",ageTwo)
	# print("teenager")
	
# ageThree=3
# if 	ageThree>=18:
	# print("adult")
# elif ageThree >=6:
	# print("teenager")
# else:
	# print("kid")
	
# s=input('birth:')
# birth=int(s)
# if birth<2000:
	# print('00前')
# else:
	# print('00后')
	
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
# height=1.75
# weight=80.5-25
# bmi=weight/height
# print(weight/height)
# print('%.2f'%bmi)#保留2位小数
# if bmi<18.5:
	# print("过轻")
# elif bmi>18.5 and bmi<25:
	# print("正常")
# elif bmi>25 and bmi<28:
	# print("过重")
# elif bmi>28 and bmi<32:
	# print("肥胖")
# elif bmi>32:
	# print("严重肥胖")
	
#today 循环
# # for in
# names=['a','b','c','d','e']
# for name in names:
		# print(name);
#求和
# sum=0
# for x in [1,2,3,4,5,6,7,8,9,10]:
	# sum=sum+x;
	# print(sum);
#函数 range
#print(list(range(6)));
#计算0-100之和
# sum=0
# for x in range(101):
		# sum =sum+x;
		# print(sum);'
		
#计算100以内所有奇数之和，可以用while循环实现：		
		
# sum=0;
# n=99;
# while n>0:
	# sum=sum+n;
	# n=n-2;
	# print(sum);
	# print(n);
#请利用循环依次对list中的每个名字打印出Hello, xxx!：
 # L = ['Bart', 'Lisa', 'Adam']
 # for name in L:
		# # print("hello:"+name)
#dict
# d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# print(d['Michael'])	
# #  add dict
# d["Lily"]=1
# print(d['Lily'])
# # 判断key是否存在
# print('Lily' in d)
# print('Lisa' in d)	
# #通过get判断key是否存在
# print(d.get('Lily'));
# print(d.get('Lisa'));
# #没有会返回None ,也可指定返回参数例如
# print(d.get('Lisa'),-1)
# #删除一个key
# d.pop('Lily')
# print(d);
#求绝对值的函数abs
#abs(100)
#求最大值
#print(max(1,2,3,4,5,6));
#数据类型转换
# print(int('123'))
# print(str(456))
# print(bool(1))
# print(bool(''))
#请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
# n1 = 255
# n2 = 1000
# print(hex(n1))
# print(hex(n2))


#***************************定义函数***************************
# def my_abs(x):
    # if x>=0:
        # return x
    # else:
        # return -x

# print(my_abs(1))
# print(my_abs(-2))
#只允许整数和浮点数
# def my_abs(x):
    # if not isinstance(x,(int,float)):
        # raise TypeError('bad operand type数据类型错误')
    # if x >= 0:
        # return x
    # else:
        # return -x

# print(my_abs('a'))
# print(my_abs(-2))
#返回多个参数
# import math

# def move(x,y,step,angle=0):
    # nx=x+step*math.cos(angle)
    # ny=y-step*math.sin(angle)
    # return nx,ny
# x,y=move(100,100,60,math.pi/6)
# print(x,y)
#请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程ax2 + bx + c = 0
#b*b-4*a*c; // 计算根的判别式
# import math
# def quadratic(a,b,c):
    # if a==0:
        # print('1')
        # return -c/b
    # elif b*b - 4*a*c<0:# 无实数解
        # print('2')
        # return None
    # elif b*b - 4*a*c==0:#有二个相等的实数解
        # print('3')
        # return -b/(2*a)
    # else:
        # print('4')
        # return (-b - math.sqrt(b*b - 4*a*c))/(2*a),(-b + math.sqrt(b*b - 4*a*c))/(2*a)#有二个不相等的实数解

# a=float(input('input a:'))
# b=float(input('input b:'))
# c=float(input('input c:'))

# print(quadratic(a,b,c))


#***************************函数的参数***************************
#一个计算x2的函数：

# def power(x):
    # return x * x

# x=int(input('input x:'))
# print(power(x))
#如果我们要计算x3怎么办？可以再定义一个power3函数，但是如果要计算x4、x5……怎么办？
# def power(x, n):
    # s = 1
    # while n > 0:
        # n = n - 1
        # s = s * x
        # print(s,'and',x)
    # return s
# x=int(input('input x:'))
# n=int(input('input n:'))
# print(power(x,n))
#默认参数
# def power(x,n=2):
    # s=1
    # while n > 0:
        # n = n-1
        # s = s * x
        # print(n,'me')
    # return s
# x = int(input('input x:'))
#n = int(input('input n:'))
# print(power(x,1))
#可变参数
#以数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。
#参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来，这样，函数可以定义如下：
# def calc(numbers):
    # sum = 0
    # for n in numbers:
        # sum = sum + n * n
        # print(sum,'n is',n)
    # return sum
# a = int(input('input a'))
# b = int(input('input b'))
# c = int(input('input c'))
# print(calc([a,b,c,4]))
#定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
#在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：
# def calc(*numbers):
    # sum=0
    # for n in numbers:
        # sum=sum+n*n
    # return sum
#print(calc(1,2,3,4,5))
#如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做：
# number=[1,2,3,4]
# print(calc(number[0],number[1],number[2],number[3]));
#也可以这样写
#*number表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见
# print(calc(*number))
#关键字参数
# def person(name,age,**kw):
   # print('name',name,'age',age,kw);

# person('lily','12');
# person('lisa',12,city='beijing')
#关键字参数有什么用？它可以扩展函数的功能。
# extra = {'city':'beijing','job':'Engineer'}
# person('lisa',12,job=extra['job'])
#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
# person('lisa',12,**extra)
#命名关键字参数
#对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。
# def persion(name,age,**kw):
    # if 'city' in kw:
        # #有city参数
        # pass
    # if 'job' in kw:
        # #有job参数
        # pass
    # print('name',name,'age',age,kw)
# extra = {'city':'beijing','job':'Engineer'}
# #但是调用者仍可以传入不受限制的关键字参数：
# persion('lisa',12,city='beijing',addr='chaoyang',zipCode='12345')
#如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
# def persion(name,age,*,city,job):
 # print(name,age,city,job)
# #命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：
# persion('lisa',12,city='beijing',job='Engineer')
#命名关键字参数可以有缺省值，从而简化调用
# def persion(name,age,*,city='chengdu',job):
    # print(name,age,city,job)
# persion('lisa',12,job='Engineer')
# persion('lisa',12,city='beijing',job='Engineer')

#参数组合
#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用，
#除了可变参数无法和命名关键字参数混合。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数/命名关键字参数和关键字参数。
# def f1(a, b, c=0, *args, **kw):
    # print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

# def f2(a, b, c=0, *, d, **kw):
    # print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

# f1(1,2,*(1,2,3),**{'name':'lisa','age':12})
# args = (1, 2, 3)
# kw = {'d': 99, 'x': '#','name':'lisa','age':12}
# f2(*args,**kw)
# 小结

# Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

# 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

# 要注意定义可变参数和关键字参数的语法：

# *args是可变参数，args接收的是一个tuple；

# **kw是关键字参数，kw接收的是一个dict。

# 以及调用函数时如何传入可变参数和关键字参数的语法：

# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

# 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

# 定义命名的关键字参数不要忘了写分隔符*，否则定义的将是位置参数。


#***************************递归参数***************************
# 在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。

# 举个例子，我们来计算阶乘n! = 1 x 2 x 3 x ... x n，用函数fact(n)表示，可以看出：

# fact(n) = n! = 1 x 2 x 3 x ... x (n-1) x n = (n-1)! x n = fact(n-1) x n

# 所以，fact(n)可以表示为n x fact(n-1)，只有n=1时需要特殊处理。

# 于是，fact(n)用递归的方式写出来就是：
# def fact(n):
    # if n == 1:
        # return 1
    # return n*fact(n-1)

# print(fact(100))
# ===> fact(5)
# ===> 5 * fact(4)
# ===> 5 * (4 * fact(3))
# ===> 5 * (4 * (3 * fact(2)))
# ===> 5 * (4 * (3 * (2 * fact(1))))
# ===> 5 * (4 * (3 * (2 * 1)))
# ===> 5 * (4 * (3 * 2))
# ===> 5 * (4 * 6)
# ===> 5 * 24
# ===> 120
# 解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。

# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，
# 使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

# 上面的fact(n)函数由于return n * fact(n - 1)引入了乘法表达式，所以就不是尾递归了。要改成尾递归方式，需要多一点代码，主要是要把每一步的乘积传入到递归函数中：
# def fact_iter(num,product):
    # if num == 1:
        # return product
    # return fact_iter(num - 1,num * product)

# def fact(n):
    # return fact_iter(n,1)
# print(fact(1000))
#大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。
# 汉诺塔的移动可以用递归函数非常简单地实现。

# 请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法.
# 汉诺塔思想笔记
# 认识汉诺塔的目标：把A柱子上的N个盘子移动到C柱子
# 递归的思想就是把这个目标分解成三个子目标
# 子目标1：将前n-1个盘子从a移动到b上
# 子目标2：将最底下的最后一个盘子从a移动到c上
# 子目标3：将b上的n-1个盘子移动到c上
# 然后每个子目标又是一次独立的汉诺塔游戏，也就可以继续分解目标直到N为1
# def move(n,a,b,c):
    # if n==1:
        # print(a,'---->',c)
    # else:
        # move(n-1, a, c, b)# 子目标1 A移动到B
        # move(1,a,b,c)#子目标2  A移动到C
        # move(n-1, b, a, c)# 子目标3 B移动到C
# n = input('enter the number:')
# move(int(n), 'A', 'B', 'C')
#***************************高级特性***************************
# L=[]
# n=1
# while n<=99:
    # L.append(n)
    # n=n+2

# print(L);
#***************************切片***************************
# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#如何用切片取前三
#print(L[0:3])
#取倒数 倒数第一个元素的索引是-1。
# print(L[-1:])
# print(L[-2:-1])
#切片操作十分有用。我们先创建一个0-99的数列：
# L = list(range(100))
# #print(L)
# print(L[0:10])
# print(L[-10:])
# #前10个数，每两个取一个：
# print(L[:10:2])
# #所有数每5个取一个
# print(L[::5])
# #什么都不写就复制一个list
# print(L[:])
#在很多编程语言中，针对字符串提供了很多各种截取函数（例如，substring），其实目的就是对字符串切片。Python没有针对字符串的截取函数，只需要切片一个操作就可以完成，非常简单。
#***************************迭代***************************
# d={"a":1,"b":2,"c":3}
# for key in d:
	# print(key)
# for key in 'ABCD':
	# print(key)
#判断是否可以迭代
# from collections import Iterable
# print(isinstance('abc',Iterable))
# print(isinstance(123,Iterable))
# #如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
# for i,value in enumerate(['a','b','c','d']):
		# print(i,value)
# #上面的for循环里，同时引用了两个变量，在Python里是很常见的，比如下面的代码：
# for x,y in [(1,2),(3,4),(5,6)]:
	# print(x,y)
#***************************列表生成式***************************
#列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
#(list(range(1,11)))
#如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
# L=[]
# for x in range(0,11):
	# L.append(x*x)

# print(L)
#循环太繁琐，如果用列表的话一句代码
# print([x*x for x in range(1,11)])
# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
# print([x*x for x in range(1,11) if x%2 ==0])
#还可以使用两层循环，可以生成全排列：
# print([m+n for m in "ABC" for n in 'XYZ'])
# import os # 导入os模块，模块的概念后面讲到  [d for d in os.listdir('.')] 
# print(d for d in os.listdir('.'))
# 循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
# d={"a":"1","b":"2","c":"3","d":"4"}
# for key,value in d.items():
	# print(key,value)
#列表生成式也可以使用两个变量来生成list：
# print([key+'='+value for key,value in d.items()])
#把列表中的字符串变为小写
# L = ['Hello', 'World', 'IBM', 'Apple']
# print([s.lower() for s in L])
# 练习

# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
# L = ['Hello', 'World', 18, 'Apple', None]
# print([s.lower() for s in L if isinstance(s,str) == True])
#***************************生成器***************************
# g = (x * x for x in range(10))
# for b in g:
	# print(b)
# generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。

# 比如，著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：

# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

# def fib(max):
	# n,a,b=0,0,1
	# while n<max:
		# print(b)
		# a,b=b,a+b
		# n=n+1
	# return 'done'
# fib(6);

# 仔细观察，可以看出，fib函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。

# 也就是说，上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了：
# def fib(max):
	# n,a,b=0,0,1
	# while n<max:
		# yield(b)
		# a,b=b,a+b
		# n=n+1
	# return 'done'
# for b in fib(6):
	# print(b)
# 练习

# 杨辉三角定义如下：

          # 1
        # 1   1
      # 1   2   1
    # 1   3   3   1
  # 1   4   6   4   1
# 1   5   10  10  5   1

# N = [1]
# def fib(N):
	# while True:
		# yield(N)
		# N.append(0)
		# N = [N[i-1] + N[i] for i in range(len(N))]
# for x in fib(N):
	# print(x)
	
#第二种写法
# NUM = 6

# def printLine(lineList):
    # lineList = [str(tmpNum) for tmpNum in lineList]
    # print("%s%s" % (" " * (NUM - len(lineList)), " ".join(lineList)))

# for i in range(NUM): #获得一个['1','2','3'.....]
    # if i < 2:
        # yhList = [1] * (i + 1)#解析num每个值，取得小于2的两个值（0，1），分别以[1],[1][1]格式输出
    # else:
       # yhList[1:-1] = [(tmpNum + yhList[j]) for j, tmpNum in enumerate(yhList[1:])] #enumerate 函数用于遍历序列中的元素以及它们的下标：yhList[1:-1]:不要第一个和最后一个.。每列错位相加例如第一个位加第二位、第二位加第三位
    # printLine(yhList)

#第三种写法
# def ytran(max):
	# n=0
	# a=[1]
	# while n<max:
			# print(a)
			# b=a+[0]
			# c=[0]+a
			# a=[b[i]+c[i] for i in range(len(b))]
			# n+=1
# ytran(6)

#第四种写法
# def rectangle(m):
	# n, b = 0, [1]
	# while n < m:
		# yield(b)
		# b = [1] + [b[i] + b[i + 1] for i in range(len(b) - 1)] + [1]
		# n += 1

#第五种写法
# for x in rectangle(10):
	# print(x)
# def triangles():
    # L = [1]
    # while True:
        # yield(L)
        # i = 1
        # T = L[:]
        # while i < len(L):
            # L[i] = T[i] + T[i-1]
            # i += 1
        # L.append(1)
# for i in triangles():
	# print(i)
	
#***************************迭代器***************************
#可以使用isinstance()判断一个对象是否是Iterable对象
# from collections import Iterable
# print(isinstance([],Iterable)) #True
# print(isinstance({},Iterable)) #True
# print(isinstance('cba',Iterable)) #True
# print(isinstance((x for x in range(10)),Iterable)) #True
# print(isinstance(100,Iterable)) #False
#而生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，
#直到最后抛出StopIteration错误表示无法继续返回下一个值了。
#可以被next()函数调用并不断返回下一个值得对象称为迭代器：Iterator
#可以使用isinstance()判断一个对象是否是Iterator对象
# from collections import Iterator
# print(isinstance((x for x in range(10)),Iterator))#True
# print(isinstance([],Iterator))#Flase
# print(isinstance({},Iterator))#Flase
# print(isinstance('abc',Iterator))#Flase
#生成器都是Iterator对象，但list、dict、str虽然是Iterable,确不是Iterator
#把list、dict、str等Iterable变成Iterator可以使用iter()函数
# print(isinstance(iter([]),Iterator))#True
# print(isinstance(iter('cba'),Iterator))#True
#***************************函数式编程***************************
#***************************高阶函数***************************
#1+到100
# print(sum(range(1,100)))
#求绝对值的函数abs
#print(abs(-10))
#传入函数
#既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收
#另一个函数作为参数，这种函数就称之为高阶函数
#例子：一个简单的高阶函数：
# def add(x,y,f):
	# return f(x)+f(y)
# print(add(-5,6,abs))
#当我们调用add(-5,6,abs)时，参数x,y和f分别接收-5，6和abs,
#根据函数定义，可以推导计算过程
#x=-5
#y=6
#f=abs
#f(x)+f(y)=abs(-5)+abs(6)=11
#编写高阶函数，就是让函数的参数能够接收别的参数
#map/reduce
# def f(x):
	# return x*x
# r=map(f,[1,2,3,4,5,6,7,8,9])
# print(r);
# print(list(r))
# mqp()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator(迭代器)
#Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list
#你可能回想，不需要map函数，写一个循环，也可以计算出结果：
# L=[]
# def f(x):
	# return x*x
# for n in [1,2,3,4,5,6,7,8,9]:
	# L.append(f(n))
# print(L)
#这样写也可以，但是你很难一眼明白“把f(x)作用在list的每一个元素并把结果生成一个新的list”
#而map作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的f(x)=x2
#还可以计算任意复制的函数，例如，把list所有数字转为字符串：
# print(list(map(str,[1,2,3,4,5,6,7,8,9])))
#reduce的用法
#reduce把一个函数作用在一个序列[x1,x2,x3,....]上，这个函数必须接收两个参数。
#求和
# from functools import reduce
# def add(x,y):
	# return x+y
# print(reduce(add,[1,3,5,7,9]))

#将序列[1,3,5,7,9]变换成整数，reduce就可以派上用场
# from functools import reduce
# def fn(x,y):
	# return x*10+y

# print(reduce(fn,[1,3,5,7,8]))
# 把str转换为int的函数：
# from functools import reduce
# def fn(x,y):
	# return x*10+y

# def char2num(s):
	# return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]#dict[key]

# print(reduce(fn,map(char2num,'13579')))

# 练习

# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

# def normalize(name):
	# return name.capitalize() #首字母大写
# L1 =['admin','LISA','barT']  
# L2 =list(map(normalize,L1)) 
# print(L2)
#Python提供的sum()函数可以接受一个list并求和，
#请编写一个prod()函数，可以接受一个list并利用reduce()求积：
# from functools import reduce
# def times(x,y):
	# return x*y
# print(reduce(times,[3,5,7,9]))

#另一种写法
# from functools import reduce
# def prod(L):
	# return reduce(lambda x,y:x*y,L)
# print('3*5*7*9=',prod([3,5,7,9]))

#***************************Python内建的filter()函数用于过滤序列***************************
#在一个list中，删除偶数，只保留奇数。
# def is_odd(n):
	# return n%2==1
# print(list(filter(is_odd,[1,2,4,5,6,9,10,15])))
#把一个序列中的空字符串删掉
# def not_empty(s):
	# return s and s.strip()#strip去除前后空格

#print(list(filter(not_empty,['A','','B',None,'C',''])))

#用filter求素数
#计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单
#首先，列出从2开始的所有自然数，构造一个序列
#2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
#取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉
#3, #4, 5, #6, 7, #8, 9, #10, 11, #12, 13, #14, 15, #16, 17, #18, 19, #20, ...
#取新序列的第一个数3，它一定是素数，然后用3把序列的倍数筛掉:
#5, #6, 7, #8, #9, #10, 11,#12, 13, #14, #15, #16, 17, #18, 19, #20, ...
#取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
#7, #8, #9, #10, 11, #12, 13, #14, #15, #16, 17, #18, 19, #20, ...
#不断筛选下去，就可以得到所有的素数
#用python来实现这个算法，可以先构造一个从3开始的奇数序列
# def _odd_iter():
	# n=1
	# while True:
		# n=n+2
		# yield n
# #注意这是一个生成器，并且是一个无限序列
# #然后定义一个筛选函数
# def _not_divisibie(n):
	# return lambda x:x%n>0
# #最后，定义一个生成器，不断返回下一个素数
# def primes():
	# yield 2
	# it=_odd_iter()#初始序列
	# while True:
		# n=next(it)#返回序列的第一个数
		# yield n
		# it=filter(_not_divisibie(n),it)#构造新序列
# #这个生成器先返回第一素数2，然后利用filter()不断产生筛选后的新的序列。
# #由于primes（）也是一个无限序列，所以调用时需要设置一个退出循环的条件

# #打印1000以内的素数
# for n in primes():
	# if n<1000:
		# print(n)
	# else:
		# break

# primes()
# 练习

# 回数是指从左向右读和从右向左读都是一样的数，
# 例如12321，909。请利用filter()滤掉非回数：
# def is_palindrome(n):
	# s=str(n)
	# if len(s)==1:
		# return True
	# else:
		# lst=[c for c in s]
		# new_lst=[]
		# for x in range(len(lst)):
			# new_lst.append(lst[len(lst)-x-1])
		# if(''.join(new_lst))==s:
			# return True
		# else:
			# return False

# output=filter(is_palindrome,range(1,1000))
# print(list(output))

#另一种解法
# def is_palindrome(n):
	# return str(n)==str(n)[::-1]#切片[::-1]是将列表或字符倒过来

# output =filter(is_palindrome,range(1,1000))
# print(list(output))

#***************************sorted***************************

# print(sorted([36,5,-12,9,-21]))
#此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，
#例如按绝对值进行排序

# print(sorted([36,5,-12,9,-21],key=abs))

# #字符排列
# print(sorted(['bob','about','Zoo','Credit']))
# #默认情况下，对字符串排序。按照ASCII的大小比较，由于‘Z’<'a'，结果大小字母Z就会排在小写字母a前面
# #如果需要排序忽略大小写，按字母应该怎么处理呢？
# #再传入一个参数
# print(sorted(['bob','about','Zoo','Credit'],key=str.lower))# lower() 方法转换字符串中所有大写字符为小写。
# #要进行反向排序，不必改动key函数，可以传入第三个参数recerse=True:
# print(sorted(['bob','about','Zoo','Credit'],key=str.lower,reverse=True))

# 练习

# 假设我们用一组tuple表示学生名字和成绩：

# # L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# # 请用sorted()对上述列表分别按名字排序：
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# def by_name(t):
	# return t[0].lower()

# print(sorted(L,key=by_name))

# #再按成绩从高到低排序：
# def by_int(t):
	# return t[1]
# print(sorted(L,key=by_int,reverse=True))

#***************************返回函数***************************
#高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
#实现一个可变参数的求和
# def calc_sum(*args):
	# ax=0
	# for n in args:
		# ax=ax+n
	# return ax
#但是，如何不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？
# #可以不返回求和的结果，而是返回求和的函数
# def lazy_sum(*args):
	# def sum():
		# ax=0
		# for n in args:
			# ax=ax+n
		# return ax
	# return sum
# #当我们调用lazy_sum，返回的并不是求和结果，而是求和函数
# f=lazy_sum(1,3,5,7,9)
# #print(f)
# #调用函数f时，才是真正计算求和的结果
# #例如
# print(f())
#在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数
#sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时
#相关参数和变量都保存在返回的函数中，这种称为‘闭包（Closure）’的程序结构拥有极大的威力。

#注意，注意，注意，当我们调用lazy_sum()时，每次调用都会返回
# #一个新的函数，即时传入新的参数
# #例子
# f1=lazy_sum(1,3,5,7,9)
# f2=lazy_sum(1,3,5,7,9)
# print(f1==f2)#等于Flase因为每次都返回的是一个新的函数

# #注意到返回的函数在其定义内部引用了局部变量args,所以，
# #当一个函数返回了一个函数后，其内部的局部变量还被新函数引用

# #另一个需要注意的问题是，返回的函数并没有立即执行，而是直到调用了f()
# #才执行，例子
# def count():
	# fs=[]
	# for i in range(1,4):
		# def f():
			# return i*i
		# fs.append(f)
	# return fs
# f1,f2,f3=count()
# #以上每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了
# #你可能认为返回结果是1，4，9。但实际结果是
# print(f1(),f2(),f3())#全部是9
#原因在于返回的函数引用了变量i,但它并非立刻执行。
#等到三个函数都返回时，它们引用的变量i已经变成了3，所以结果都等于9
#返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化
#如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，
#无论该循环变量后续如何更改，已绑定到函数参数的值不变：
# def count():
	# def f(j):
		# def g():
			# return j*j
		# return g
	# fs=[]
	# for i in range(1,4):
		# fs.append(f(i)) #f(i)立刻被执行，因此i的当前值被传入f()
	# return fs

# f1,f2,f3=count()
# print(f1(),f2(),f3())

#小结
#一个函数可以返回一个计算结果，也可以返回一个函数
#返回一个函数，牢记改函数并未执行，返回函数中不要引用任何可能会发生变化的变量

#***************************匿名函数***************************
# f=list(map(lambda x:x*x,[1,2,3,4,5,6,7,8,9]))#关键字lambda表示匿名函数，冒号前面的x表示函数参数。
# print(f)
#lambda x:x*x  实际上就是：
# def f(x):
	# return x*x
#这样写的好处就是，后者多定义了一个（污染环境）函数
#尤其是如果这个函数只会用一次的话。
#而且第一写法更易读，因为那个映射到列表上的函数具体是要做什么，
#非常一目了然。如果你仔细观察自己的代码，会发现这种场景其实很常见：
#你在某处就真的只需要一个能做一件事情的函数而已，连它叫什么名字都无关紧要。
#Lambda 表达式就可以用来做这件事。

#匿名函数有个限制，就是只能有一个表达式，不用写retrun,返回值就是该表达式的结果

#小结
#python对函数的支持有限，只有一些简单的情况下可以使用匿名函数

#***************************装饰器***************************
#由于函数也是一个对象，而函数对象可以被赋值给变量，所以，通过变量也能调用该函数
# def now():
	# print('2016-4-13')
# f=now
# f()
# #函数有一个__name__属性，可以拿到函数的名字
# print(now.__name__)
# print(f.__name__)
#现在，假设我们要增强now()函数的功能，比如，在调用前后自动打印日志，但是又不希望修改now()函数的定义
#这种在代码运行期间动态增加功能的方式，称之为‘装饰器’（Decorator）
#本质上，Decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的Decorator
#可以如下定义：
# def log(func):
	# def wrapper(*args,**kw):
		# print('call %s()'% func.__name__)
		# return func(*args,**kw)
	# return wrapper
# #观察上面的log,因为它是一个Decorator,所以接受一个函数作为参数，并返回一个函数
# #我们要借助Python的@语法，把decorator置于函数的定义处
# @log
# def now():
	# print('2016-4-13')
# #调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志
# now()
#把@log放到now()函数的定义处，相当于执行了语句：
#now=log(now)
#由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，
#只是现在同名的now变量指向了，新的函数，于是调用now()将执行新函数，即在
#log()函数中返回的wrapper()函数

#wrapper()函数的参数定义是（*args,**kw）,因此，wrapper（）函数可以接受任意参数的调用
#在wrapper（）函数内，首先打印日志，再紧接着调用原始函数。

#如果decorator本身需要传入参数，那就需要编写
#一个返回decorator的高阶函数，写出来会更复杂
# #比如定义log文本
# def log(text):
	# def decorator(func):
		# def wrapper(*args,**kw):
			# print('%s %s():'%(text,func.__name__))
			# return func(*args,**kw)
		# return wrapper
	# return decorator

# #这个三层嵌套的Decorator用法如下：
# @log('execute我是参数')
# def now():
	# print('2016-4-13')

# now()

# #和两层相比，3层嵌套的效果是这样的：
# #now=log('execute')(now)

# #以上两种decorator的定义都没有问题，但还差最后一步。因为我们讲了函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，
# #它们的__name__已经从原来的'now'变成了'wrapper'：
# print(now.__name__)#返回wrapper

#因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。

#不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：
# import functools

# def log(func):
    # @functools.wraps(func)
    # def wrapper(*args, **kw):
        # print('call %s():' % func.__name__)
        # return func(*args, **kw)
    # return wrapper
#或者针对带参数的decorator：

# import functools

# def log(text):
    # def decorator(func):
        # @functools.wraps(func)
        # def wrapper(*args, **kw):
            # print('%s %s():' % (text, func.__name__))
            # return func(*args, **kw)
        # return wrapper
    # return decorator

# @log('execute我是参数')
# def now():
	# print('2016-4-13')
# now()
# print(now.__name__)

#***************************偏函数***************************
#Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）

# #int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换
# int('12345')#输出12345
# #但int()函数还提供额外的base参数，默认值为10.如果传入base参数，就可以做N进制的转换
# int('123456',base=8)#按8进制转换，输出5349
# int('12345',16)#按16进制转换，输出74565
# #假设需要大量的二进制转换，每次都传入int(x,base=2)非常麻烦，
# #于是我们可以定义一个int2()函数，默认把base=2传进去：
# def int2(x,base=2):
	# return int(x,base)
# int2('1000000')#输出64
# int2('1010101')#输出85
# functools.partial就是帮助我们创建一个偏函数的，
# 不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
import functools
int2=functools.partial(int,base=2)
print(int2('1000000'))#输出64
print(int2('1010101'))#输出85