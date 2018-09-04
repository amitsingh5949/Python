from pprint import pprint as pp

student = {
    'name': 'amit',
    'age': 28,
    'college': 'utd'
}

print(student)  # {'name': 'amit', 'age': 28, 'college': 'utd'}
# print(student[0]) key error
# print(student('address')) key error
print(student['name'])  # amit
print(student.get('name','unknown'))  # amit
print(student.get('address','unknown'))  # unknown

print(student.keys())  # dict_keys(['name', 'age', 'college'])

values = student.values();
print(values)  # dict_values(['amit', 28, 'utd'])
for val in values:
    print(val)

student['name']  = 'henry'  # updates the values
items  = student.items()  # map.entry return the tuple of (key, value)
for item in items:
    print(item[0], item[1])

del student['name']  # deletes key-value pair
print(student)

student['address'] = 'HAl second stage'  # if key is not present then it gets added
print(student)  # {'age': 28, 'college': 'utd', 'address': 'HAl second stage'}

# dictionary copy

d = dict([('name','amit'), ('age', 28)])
print(d)  # {'name': 'amit', 'age': 28}

e = d.copy()
print(e)  # {'name': 'amit', 'age': 28}
print(e is d)  # False
print(e == d)  # True

f = dict(e)
print(f)   # {'name': 'amit', 'age': 28}
f['age'] = 29
print(f)  # {'name': 'amit', 'age': 29}

#f.update(e) updating contensts of f with e
print(f)  # {'name': 'amit', 'age': 28}

h = {'addess' : 'hal II stage'}
f.update(h)
print(f)  # {'name': 'amit', 'age': 29, 'addess': 'hal II stage'}

pp(f)  # idk.. how to use pp