from Animal import *


class Cat(Animal):
    def run(self):
        print('Cat is running...')

    def eat(self):
        print("Eating fish")


# cat = Cat()
# cat.run()
# cat.eat()
def run_twice(Animal):
    Animal.run()
    Animal.run()


run_twice(Cat())
run_twice(Animal())

# 静态语言VS动态语言
# 对于静态语言来说，如果需要传人Animal类型，则传入对象必须是Animal类型或者它的子类，否则，讲无法调用run()方法
# 对于动态语言来说，则不一定需要传人Animal类型。我们只需要保证传入的对象有一个run()方法就可以了；

# 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”
# 那它就可以被看做是鸭子。
# python的“file-like object”就是一种鸭子类型。对真正的文件对象，它有一个read()方法，返回其内容
# 但是，许多对象，只要有read()方法，都被视为“file-like object”
# 许多函数接收的参数就是“file-like object”你不一定要传人真正的文件对象，完全可以传人仁和实现了read()方法的对象

# 小结
# 继承可以把父类的所有功能都直接那过来，这样就不必重零做起，子类只需要新增自己特有方法
# 也可以把父类不适合的方法覆盖重写。
# 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。 喵！！！






