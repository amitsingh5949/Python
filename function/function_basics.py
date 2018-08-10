student_list = []


def get_student_info():
    # student_list_title = []
    for student in student_list:
        student['name'] = student['name'].title()
    # student_list_title.append(student)
    return student_list


def print_student_info():
    for student in get_student_info():
        print(student)


def add_student(name, id=221):
    student_list.append({
        'name': name,
        'id': id
    })


add_student("mark", 231)
add_student("jini")  # setting default value for argument
add_student("carl", 12)
add_student(id=32, name='max')  # calling function with named argument and have changed their order

print_student_info()
