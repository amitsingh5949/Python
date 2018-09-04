s = 'my name is amit singh'.split(' ')

list1 = [len(word) for  word in s]
print(list1)  # [2, 4, 2, 4, 5]

set1 = {len(word) for word in s}
print(set1)  # {2, 4, 5}


def less_5(x):
    if x < 5:
        return True
    else:
        return False


set2 = {len(word) for word in s if less_5(len(word))}  # filter predicate
print(set2)  # {2, 4}

