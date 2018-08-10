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
items  = student.items()  # map.entry
for item in items:
    print(item)

del student['name']  # deletes key-value pair
print(student)

