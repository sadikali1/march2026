class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

    def run(self):
        return f"{self.name} is running."

    def eat(self):
        return f"{self.name} is eating."

class Dog(Animal):
    def bark(self):
        return f"{self.name} says Woof!"

class Puppy(Dog):
    def bark(self):
        return f"{self.name} says yip yip!"

class Cat(Animal):
    def meow(self):
        return f"{self.name} says Meow!"


dog = Dog('My Dog')
print(dog.bark())
print(dog.run())
print(dog.eat())

puppy = Puppy('Tiny Puppy')
print(puppy.bark())
print(puppy.run())
print(puppy.eat())

cat = Cat('My Cat')
print(cat.meow())
print(cat.run())
print(cat.eat())
