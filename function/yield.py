student_list = []


def read_data():
    try:
        f = open('student.txt', 'r')
        for line in read_lines_using_yield(f):
            arr = line.split(" ")
            student_list.append({'name': arr[0], 'id': arr[1]})
    except Exception:
        print('error occured while reading from file')


def read_lines_using_yield(f):
    for line in f:
        yield line


read_data()
print(student_list)
