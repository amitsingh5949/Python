a = 'amit'
b = "Manu"
c = "Hello world"  # used for multi line comments

""" 
 comment starts from here 
 TODO
"""

print(a + " " + b)  # amit Manu

print(a == b)  # False

# String functions
print(a.capitalize())  # Amit
print(b.islower())  # False
print(b.isupper())  # False
print(b.isalnum())  # True
print(b.upper())  # MANU

print("123".isdigit())  # True

print(c.replace('o', "x"))  # Hellx wxrld

array = "pdf,excel,word,text,json".split(",")
print(array)  # ['pdf', 'excel', 'word', 'text', 'json']

# Format method of string

print("Nice to meet you {0}!! I am {1}".format(a, b))  # Nice to meet you amit!! I am Manu

print(f"Nice to meet you {a}!! I am {b}")  # Nice to meet you amit!! I am Manu

num = "123456789"
print(num[2:])   # 3456789  _string_[begining:end:length]
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