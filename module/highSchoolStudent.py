from module.student import Student


class HighSchoolStudent(Student):  # extending Student class

    school_name = 'asu'

    def get_student(self):  # overriding get_student() method from parent class
        student_info = super().get_student()  # super calls the parent method.
        return student_info.title() + '-HS'