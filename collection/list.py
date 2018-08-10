student_names = ['amit', 'namit', 'aryan']
print(student_names)  # ['amit', 'namit', 'aryan']

print(student_names[0])  # amit
print(student_names[1])  # namit
print(student_names[-1])  # aryan , accessing list backwards index starts from -1 as there is o such thing as -0

# student_names[3] = 'sirsa'  # can't do this
student_names.append('sirsa')
print(student_names)  # ['amit', 'namit', 'aryan', 'sirsa']

if "amit" in student_names:
    print("amit")  # amit

print(len(student_names))  # 4
del(student_names[0])
print(len(student_names))  # 3
# del(student_names["aryan"])  list indices must be integers or slices, not str


student_names.append('mark')
student_names.append('alice')
student_names.append('rob')
student_names.append('jon')
student_names.append('jini')
student_names.append('kevin')
student_names.append('max')
student_names.append('carl')

print(student_names)  # ['namit', 'aryan', 'sirsa', 'mark', 'alice', 'rob', 'jon', 'jini', 'kevin', 'max', 'carl']

# list slicing , works same as string slicing

print(student_names[1:])  # ['aryan', 'sirsa', 'mark', 'alice', 'rob', 'jon', 'jini', 'kevin', 'max', 'carl']
print(student_names[1:-1:2])  # ['aryan', 'mark', 'rob', 'jini', 'max']



