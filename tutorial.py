class Dog(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def speak(self):
        print('Hi I am ', self.name ,'and I am ', self.age , 'year old')

class Cat(Dog):
    def _init_(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color

    def speak(self):
        print('Hi I am ', self.name ,'and I am ', self.age , 'year old')


     

            