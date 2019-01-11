student_names = ['amit', 'namit', 'aryan']
print(student_names)  # ['amit', 'namit', 'aryan']

print(student_names[0])  # amit
print(student_names[1])  # namit
print(student_names[-1])  # aryan , accessing list backwards index starts from -1 as there is no such thing as -0

# student_names[3] = 'sirsa'  # can't do this
student_names.append('sirsa') # inserts element at the last
print(student_names)  # ['amit', 'namit', 'aryan', 'sirsa']

if "amit" in student_names:
    print("amit")  # amit

print(len(student_names))  # 4


# delete and remove
del(student_names[0])
print(len(student_names))  # 3
# del(student_names["aryan"])  list indices must be integers or slices, not str

print(student_names.remove('aryan'))  # return None but removes the element
print(student_names) #['namit', 'sirsa']

popped_item = student_names.pop()
print(popped_item ) # sirsa
student_names.append('sirsa')
popped_item = student_names.pop(0)
print(popped_item ) # namit

student_names.insert(0,'namit')
student_names.append('mark')
student_names.append('alice')
student_names.append('rob')
student_names.append('jon')
student_names.append('jini')
student_names.append('kevin')
student_names.append('max')
student_names.append('carl')
student_names.insert(2, 'maria')  # insert method
print(student_names)  # ['namit', 'sirsa', 'maria', 'mark', 'alice', 'rob', 'jon', 'jini', 'kevin', 'max', 'carl']


# list slicing , works same as string slicing
print(student_names[1:])  # ['sirsa', 'maria', 'mark', 'alice', 'rob', 'jon', 'jini', 'kevin', 'max', 'carl']
print(student_names[1:-1:2])  # ['sirsa', 'mark', 'rob', 'jini', 'max']


# copies one list to other -  keep in mind copies are shallow
# Method 1 : copying by slicing
student_names_copy  = student_names[:]
print(student_names_copy)  # ['namit', 'sirsa', 'maria', 'mark', 'alice', 'rob', 'jon', 'jini', 'kevin', 'max', 'carl']
print(student_names is student_names_copy)  # False

print(student_names == student_names_copy)  # True since contents are same

# method 2 calling copy method
copy2 = student_names.copy()  # ['namit', 'aryan', 'sirsa', 'mark', 'alice', 'rob', 'jon', 'jini', 'kevin', 'max', 'carl']
print(copy2) #['namit', 'sirsa', 'maria', 'mark', 'alice', 'rob', 'jon', 'jini', 'kevin', 'max', 'carl']

# method 3 - calling list constructor
copy3 = list(student_names)
print(copy3)  # ['namit', 'sirsa', 'maria', 'mark', 'alice', 'rob', 'jon', 'jini', 'kevin', 'max', 'carl']

#update list
student_names[0] = 'Hanu' # unlike strings we can update the elements in list
print(student_names) #['Hanu', 'sirsa', 'maria', 'mark', 'alice', 'rob', 'jon', 'jini', 'kevin', 'max', 'carl']




shallow = [[1, 2]] * 3
print(shallow)  # [[1, 2], [1, 2], [1, 2]]
print(len(shallow))  # 3

shallow[1].append(3)
print(shallow)  # [[1, 2, 3], [1, 2, 3], [1, 2, 3]] since all inner list were pointing to same list due to shallow copying
print(len(shallow))  # 3

list1 = {False, 'amit', 1, None, True, 2}
print(list1)  # {False, 1, 2, 'amit', None} not printing last True..idk


# list constructor
a = list('amit')  # coverts string to list of characters
print(a)  # ['a', 'm', 'i', 't']

# list search

s = "1 2 3 4 5 6".split(' ')
print(s.index('3'))  # 2
# print(s.index('7'))  ValueError: '7' is not in list


# adding two list

a = [1, 2, 3 ] + [3, 4, 5]
print(a)  # [1, 2, 3, 3, 4, 5]
a += [6, 7, 8]
print(a)  # [1, 2, 3, 3, 4, 5, 6, 7, 8]
a.extend([9, 0])  # [1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 0]

print(a)

# reverse and sort functions are in place and return None

a.reverse()
print(a)  # [0, 9, 8, 7, 6, 5, 4, 3, 3, 2, 1]

a.sort()
print(a)  # [0, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9]

a.sort(reverse=True)
print(a)  # [9, 8, 7, 6, 5, 4, 3, 3, 2, 1, 0]

# reversed and sorted not in place

b = [4, 5, 1 ,2, 8, 0, 6]

c = sorted(b)
print(b)  # [4, 5, 1, 2, 8, 0, 6]
print(c)  # [0, 1, 2, 4, 5, 6, 8]

c = reversed(b)
print(b)   # [4, 5, 1, 2, 8, 0, 6]
print(c)  # <list_reverseiterator object at 0x7f5a62a50860> , return iteratable reversed list
print(list(c))  # [6, 0, 8, 2, 1, 5, 4]

pp = [1, 2, 3, 1, 1, 1, 1]
print(pp.count(1))  # 5






