class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def print_all(self):
        print('Name :', self.name)
        print('Age  :', self.age)
        print('Grade:', self.grade)
        print('-------------------')


# create instances using __init__
student1 = Student('Alice', 20, 'A')
student1.print_all()

student2 = Student('Bob', 22, 'B')
student2.print_all()

student3 = Student('Charlie', 21, 'A')
student3.print_all()