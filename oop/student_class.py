student_list = []


class Student:

    def __init__(self, name, id=332):   # parametrised constructor
        student_list.append({
            'name': name,
            'id': id
        })

    def print_student_list(self):
        for student in student_list:
            print(student)

    def __str__(self):  # toString() method
        return 'student instance'


student1 = Student('mark')
student2 = Student('carl', 13)
print(student2)
student2.print_student_list()

"""
o/p:
student instance
{'name': 'mark', 'id': 332}
{'name': 'carl', 'id': 13}
"""