class Student:

    school_name = 'utd'  # class attribute similar to static variables

    def __init__(self, name, id=332):   # parametrised constructor
        self.name = name   # this will create instance attribute name and id and also tie it to self
        self.id = id

    def get_student(self):
            return self.name + ' ' + str(self.id) + ' ' + self.school_name

    def __str__(self):  # toString() method
        return 'student instance with name ' + self.name


class HighSchoolStudent(Student):  # extending Student class

    school_name = 'asu'

    def get_student(self):  # overriding get_student() method from parent class
        studnet_info = super().get_student()  # super calls the parent method.
        return studnet_info.title() + '-HS'



student = HighSchoolStudent('james', 28)
print(student.get_student())  # James 28 Asu-HS
