class Student:

    # static / class variable shared by all instances
    school = 'ABC High School'

    name = None
    age = None
    grade = None

    def print_all(self):
        print('School:', self.school)
        print('Name :', self.name)
        print('Age  :', self.age)
        print('Grade:', self.grade)
        print('-------------------')


if __name__ == '__main__':
    # create instance without using __init__ and set attributes afterwards
    student1 = Student()
    student1.name = 'Alice'
    student1.age = 20
    student1.grade = 'A'

    student1.print_all()

    student2 = Student()
    student2.name = 'Bob'
    student2.age = 22
    student2.grade = 'B'

    student2.print_all()

    student3 = Student()
    student3.name = 'Charlie'
    student3.age = 21
    student3.grade = 'A'

    student3.print_all()

    # show static/class variable is shared across instances
    print('--- Changing class variable Student.school ---')
    Student.school = 'New Horizon Academy'
    student3.age =25
    student1.print_all()
    student2.print_all()
    student3.print_all()