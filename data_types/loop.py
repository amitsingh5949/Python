student_names = ['amit', 'namit', 'aryan']
student_names.append('mark')
student_names.append('alice')
student_names.append('rob')
student_names.append('jon')
student_names.append('jini')
student_names.append('kevin')
student_names.append('max')
student_names.append('carl')

# like for-each loop
for name in student_names:
    print(name)  # print names all student in new line

# for loop with range
for x in range(10):
    print(x)  # print numbers from 0 to 9

# range() actually returns a list, takes 3 argument  range(begin, end, increment)
print(range(5) == [0, 1, 2, 3, 4])  # though statement is logically true but it prints false
print(range(1, 5) == [1, 2, 3, 4])  # though statement is logically true but it prints false
print(range(1, 5, 2) == [1, 3])  # though statement is logically true but it prints false

# we can use break and continue smiliar to other languages
for x in range(10):
    if x==5:
        break;
    print(x)




