set1 = {34, 12, 93, 45, 3 , 4, 0, 1}

iterator = iter(set1)

try:
    while(True):
        print(next(iterator))  # prints all elements of set
except StopIteration:
    pass
