a = 5
b = 0

c = True
d = False

str1 = "123"
str2 = ""

x = None

arr1 = ['amit', 'manu']
arr2 = []

if a == 5:
    print('a is ' + str(a))  # a is 5
else:
    print('a is not ' + str(a))

if a != 5:
    print('a is not ' + str(a))
else:
    print('a is  ' + str(a))  # a is 5

if a:
    print('a is ' + str(a))  # a is 5
else:
    print('a is not ' + str(a))

if str1:
    print(str1)  # 123

if str2:
    print(str2)  # prints nothing

if arr1:
    print(arr1)  # ['amit', 'manu']

if arr2:
    print(arr2)  # prints nothing


if x:
    print(x)  # prints nothing

if not x:
    print(x)  # None

if x or a:
    print('x or a  ' + str(a))   # x or a  5

if x and a:
    print('x or a  ' + str(a))  # prints nothing

str3 = "bigger" if a > b else "samller"  # ternary condition
print(str3)  # bigger
