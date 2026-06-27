class Student:

    student_count = 0  # Class variable to keep track of the number of students
    
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def greet(self):
        return f'Hello, my name is {self.name}.'
    
    def grade_info(self):
        return f'I am in grade {self.grade}.'
    
# Create a Student object
student = Student('Alice', 14, '9th')
print(student.greet())
print(student.grade_info())
