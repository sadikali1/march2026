class Flyer:
    def fly(self):
        return f"{self.name} is flying."

class Swimmer:
    def swim(self):
        return f"{self.name} is swimming."

class Duck(Flyer, Swimmer):
    def __init__(self, name):
        self.name = name

    def quack(self):
        return f"{self.name} says quack!"

if __name__ == '__main__':
    daffy = Duck('Daffy')
    print(daffy.quack())
    print(daffy.fly())
    print(daffy.swim())
