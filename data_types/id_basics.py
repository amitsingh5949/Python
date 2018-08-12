a = 10
print(id(a))  # 10943296

b = a
print(id(a))  # 10943296

# we see both id's are same, id() is similiar to hasCode()

x = 10

print(id(x))  # 10943296, we see that x also has the sme id as object 10 is already in pool so no new objects will be created