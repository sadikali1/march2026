class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            raise ValueError('Age cannot be negative')

    def describe(self):
        return f"{self.__name} is {self.__age} years old."

if __name__ == '__main__':
    person = Person('Alice', 30)
    print(person.describe())

    person.set_name('Bob')
    person.set_age(35)
    print(person.describe())
