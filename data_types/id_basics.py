a = 10
print(id(a))  # 10943296

b = a
print(id(a))  # 10943296

# we see both id's are same, id() is similar to hasCode()

x = 10

print(id(x))  # 10943296, we can see that x also has the same id as object 10 is already present in pool so no new object will be created