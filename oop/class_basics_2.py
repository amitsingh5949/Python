
class Test:
    def print(self):
        print('hello world')
        print(self)

obj = Test()
print(obj)   # <__main__.Test object at 0x7fd2e88cc208>
obj.print()

"""
o/p
<__main__.Test object at 0x7f6b077df1d0>
hello world
<__main__.Test object at 0x7f6b077df1d0>

we can see obj and self are same , self can be thought as this
"""