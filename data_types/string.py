a = 'amit'
b = "Manu"
c = "Hello world"

# used for multi line comments
""" 
 comment starts from here 
 TODO
"""


print(a[1]) # m , right indexing(start to end) start from 0 to n-1 and left indexing(end to start) start from -1 to -n, n is number of characters in string
print(a[-1]) # t
print(a == b)  # False

#escape sequences
print('hello \n world') # hello newline world
print('hello \t world') # hello 	 world

#Strings are immutable
#a[0] = 's' #TypeError: 'str' object does not support item assignment

# String concatenation
#a0 = a + 3 TypeError: must be str, not int
a1 = a + b
print(a1) # amitManu

print(a + " " + b)  # amit Manu

letter = 'z'
letter = letter * 10
print(letter) #zzzzzzzzzz


# String functions
print(len(a)) # 4 prints the length of string
print(a.capitalize())  # Amit
print(b.islower())  # False
print(b.isupper())  # False
print(b.isalnum())  # True
print(b.upper())  # MANU
print("123".isdigit())  # True
print(c.replace('o', "x"))  # Hellx wxrld

array = "pdf,excel,word,text,json".split(",")
print(array)  # ['pdf', 'excel', 'word', 'text', 'json']


# Format method of string -- String interpolation
print("Nice to meet you {}!! I am {}".format(a, b))  # Nice to meet you amit!! I am Manu
print("Nice to meet you {1}!! I am {0}".format(a, b))  # Nice to meet you Manu!! I am amit
print("Nice to meet you {a}!! I am {y}".format(a='Aryan', y='ish')) # Nice to meet you Aryan!! I am ish
print(f"Nice to meet you {a}!! I am {b}")  # Nice to meet you amit!! I am Manu

#Float formatting , float follows "{value:width.precision f}"
result = 100/77
print("result is {r}".format(r=result)) # 1.2987012987012987
print("result is {r:1.3f}".format(r=result)) # result is 1.299
result = 10000000000/77
print("result is {r:50.3f}".format(r=result)) # result is                                      129870129.870(width added whitespace)

num = "123456789"
print(num[2:])   # 3456789  _string_[begining:end:step_length]
print(num[:2])  # 12
print(num[2:5])  # 345
print(num[0::2])  # 13579
print(num[::-1])  # 987654321

x  = 'a' 'b'  # adjacent strings are concatenated
print(x)   # ab

# string join method

joinedstr = ','.join(['1','2','3','4'])  # concatenates the strings in list with delimiter ,
print(joinedstr)  # 1,2,3,4

# string partition

print("amit:manu".partition(':'))  # ('amit', ':', 'manu'), partition returns the tuple of before,current, after string

a, _, b = "amit:manu".partition(':')
print(a, b)  # amit manu