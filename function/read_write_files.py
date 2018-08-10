from binhex import openrsrc

student_list = []


def get_student_info():
    for student in student_list:
        student['name'] = student['name'].title()
    return student_list


def print_student_info():
    for student in get_student_info():
        print(student)


def add_student(name, id=221):
    student_list.append({
        'name': name,
        'id': id
    })


def save_data(student_list):
    try:
        f = open('student.txt','a')
        for student in student_list:
            f.write(student['name'] + " ")
            f.write(str(student['id']) + "\n")
        f.close()
    except Exception as error:
        print('error opening file')
        print (error)


def read_data():
    try:
        f = open('student.txt', 'r')
        for line in f.readlines():
            arr = line.split(" ")
            add_student(arr[0], arr[1])
    except Exception:
        print('error occured while reading from file')



"""
add_student("mark", 231)
add_student("jini")  # setting default value for argument
add_student("carl", 12)
add_student(id=32, name='max')  # calling function with named argument and have changed their order

print_student_info()
save_data(student_list)
"""

read_data()
print_student_info()




