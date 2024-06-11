# define Animal class as super class
class Animal():
    def __init__(self):
        print("Animal created")
    def eat(self):
        print("Animal eating")
# define Dog class as sub class of Animal Class
class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog created")
    def speak(self):
        print("Woof!")
# define Cat class as sub class of Animal Class
class Cat(Animal):
    def __init__(self):
        super().__init__()
        print("Cat created")
    def speak(self):
        print("Meoww!")
# instance of Dog class inherited from Animal class
d = Dog()
d.eat()
d.speak()
# instance of Cat class inherited from Animal class
c = Cat()
c.eat()
c.speak()
