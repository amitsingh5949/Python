class Student:

    school_name = 'utd'  # class attribute similar to static variables

    def __init__(self, name, id=332):   # parametrised constructor
        self.name = name   # this will create instance attribute name and id and also tie it to self
        self.id = id

    def print_student(self):
            print(self.name, self.id, self.school_name)

    def __str__(self):  # toString() method
        return 'student instance with name ' + self.name


mark = Student('mark')
print(mark)  # student instance with name mark
mark.print_student()  # mark 332 utd
print(mark.id)  # 332
print(mark.school_name)  # utd
print(Student.school_name)  # utd as static variables can be accessed bu class names