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
