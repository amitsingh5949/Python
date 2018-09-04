set1 = {34, 12, 93, 45, 3 , 4, 0, 1}
print(set1)  # {0, 1, 34, 3, 4, 12, 45, 93}

#print(set1[0])  3 'set' object does not support indexing

set2 = set(set1)
set2.add(46)
print(set2)  # {0, 1, 34, 3, 4, 12, 45, 46, 93}

print(46 in set2)  # True

# empty set
set3 = {}
print(type(set3))  # <class 'dict'> creats dictionary not set

set3 = set()
print(type(set3))  # <class 'set'>

set4 = set([2, 2, 2])
print(set4)  # {2} duplicates are discarded

# update

set4.update(set2)
print(set4)  # {0, 1, 2, 34, 3, 4, 12, 45, 46, 93}

set5 = set4.copy()
print(set5)  # {0, 1, 2, 34, 3, 4, 12, 45, 46, 93}
print(set5 is set4)  # False
print(set5 == set4)  # True

# delete and remove
set5.remove(34)
#set5.remove(34)  # KeyError: 34

set5.discard(12)  # deletes if key is present or not
set5.discard(12)

# set has other useful methods:
# union(), intersection(), difference(), symmetric_difference(), issubset(), issuperset(), isdisjoint()

