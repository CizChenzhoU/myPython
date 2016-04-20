from Animal import Animal
# 从Animal模块继承Animal类


class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


dog = Dog()
dog.run()
dog.eat()
