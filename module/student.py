class Student:

    school_name = 'utd'  # class attribute similar to static variables

    def __init__(self, name, id=332):   # parametrised constructor
        self.name = name   # this will create instance attribute name and id and also tie it to self
        self.id = id

    def get_student(self):
            return self.name + ' ' + str(self.id) + ' ' + self.school_name

    def __str__(self):  # toString() method
        return 'student instance with name ' + self.name