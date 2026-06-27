# Simple Car class with name, color, and a method to show details

class Car:
    
    def __init__(self, name1, color1):
        self.name = name1
        self.color = color1

    def show_details(self):
        return f'Car name: {self.name}, Color: {self.color}'


car1 = Car('Toyota', 'Red')
car2 = Car('Hundai Creta', 'White')
car3 = Car('Honda City', 'Black')

print(car1.show_details())
print(car2.show_details())
print(car3.show_details())


# local variabe 
# class variable, instance variable