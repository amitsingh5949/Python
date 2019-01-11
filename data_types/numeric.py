#!/usr/bin/python3 python3.6    
a = 2
b = 2345677890076554432222244466778899999766334545677787899898898877676556544543343223222435454566567767788788989897676554443
print(a+b) #2345677890076554432222244466778899999766334545677787899898898877676556544543343223222435454566567767788788989897676554445

pi = 3.147
print(a+pi) # 5.147

#type() function
print(type(a)) # <class 'int'>
print(type(pi)) # <class 'float'>

#Type casting
print(int(pi)) # 3
print(float(a)) # 2.0
print(int(pi) + float(a)) # 5.0

#Power operator
print(2 ** 3) # 8
print( 2 + 10 * 10 + 2) # 104 it performs the association automatically
print( 0.1 + 0.2 - 0.3)  # 5.551115123125783e-17 https://docs.python.org/2/tutorial/floatingpoint.html
