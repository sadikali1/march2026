# Simple class example for beginners with two methods

class Person:

    """A basic Person class with two simple methods."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        """Return a greeting message."""
        return f'Hello, my name is {self.name}.'

    def have_birthday(self):
        """Increase the person's age by one year."""
        self.age += 1
        return f'Happy birthday! You are now {self.age} years old.'


# Create a Person object
person = Person('Alice', 14)
print(person.greet())
print('Current age:', person.age)

# Call the second method
birthday_message = person.have_birthday()
print(birthday_message)
print('New age:', person.age)

