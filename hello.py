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

# #二维数组
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


#定义函数
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


#函数的参数
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



