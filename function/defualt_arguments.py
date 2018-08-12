import time


def get_time(args=time.ctime()):
    print(args)


get_time()
get_time()
get_time()
get_time()

'''
o/p
Sun Aug 12 20:06:50 2018
Sun Aug 12 20:06:50 2018
Sun Aug 12 20:06:50 2018
Sun Aug 12 20:06:50 2018
'''

# we see that time never changes because default arguments are initialised only once


def abc(a=[]):
    a.append('spam')
    print(a)


abc()  # ['spam']
abc()  # ['spam', 'spam'] because a is mutable object and gets initialised and call abc() again will add value in previous default value
abc(['a'])  # ['a', 'spam'] not using the default value
abc()  # ['spam', 'spam', 'spam']

# so always use immutable values as default values