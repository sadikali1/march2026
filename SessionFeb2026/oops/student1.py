# Student class without constructor
# Assigning values directly to object attributes

class Student:
    """A simple Student class without constructor."""

    def __init__(self, name, email, phone, rollnumber):
        self.name = name
        self.email = email
        self.phone = phone
        self.rollnumber = rollnumber

    def print_details(self):
        """Print student details."""
        print(f'Name: {self.name}')
        print(f'Email: {self.email}')
        print(f'Phone: {self.phone}')
        print(f'Roll Number: {self.rollnumber}')


# Create a student object
student = Student('Alice', 'alice@example.com', '9876543210', 101)

# Call print_details method
student.print_details()

# Create second student object
student2 = Student('Bob', 'bob@example.com', '9876543211', 102)

print()
student2.print_details()

# Create third student object
student3 = Student('Charlie', 'charlie@example.com', '9876543212', 103)

print()
student3.print_details()

