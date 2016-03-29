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
height=1.75
weight=80.5-25
bmi=weight/height
print(weight/height)
print('%.2f'%bmi)#保留2位小数
if bmi<18.5:
	print("过轻")
elif bmi>18.5 and bmi<25:
	print("正常")
elif bmi>25 and bmi<28:
	print("过重")
elif bmi>28 and bmi<32:
	print("肥胖")
elif bmi>32:
	print("严重肥胖")
	


