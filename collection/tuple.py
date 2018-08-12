t = (1, 2, True, None, 'amit', True)

print(t)  # (1, 2, True, None, 'amit', True)

print(t[0])  # 1
print(len(t))  # 6

t = t + (3, 4)

print(t)  # (1, 2, True, None, 'amit', True, 3, 4) order is maintained

# t[0] = 5 'tuple' object does not support item assignment

t = t * 2  # multiplies the tuple with itself

print(t)  # (1, 2, True, None, 'amit', True, 3, 4, 1, 2, True, None, 'amit', True, 3, 4)

x = ((1, 2), (3, 4))
print(x[1][0])  # 3

k = (32,)  # single element tupple
print(k[0])  # 32

y = ()  # empty tuple
print(type(y))  # <class 'tuple'>

z = tuple([1, 2, 3, 4])  # creating tuple from list
print(z)  # (1, 2, 3, 4)

print(5 in z)  # False , in works like contains


# tuple unpacking

p = 1, 2, 3, 4  # brackets are omitted
print(p)  # (1, 2, 3, 4)


def minmax(list):
    return min(list), max(list)  # returns the tuple of min and max element from list


print(minmax([1, 2, 3, 4, 5]))  # (1, 5)

low, high = minmax([1, 2, 3, 4, 5])
print(low)  # 1
print(high)  # 5

(a, (b, c)) = (1, (2, 3))
print(b, c, a)  # 2 3 1

# swapping two numbers using tuple
a = 3
b = 4
a, b = b, a
print(a, b) # 4 3
