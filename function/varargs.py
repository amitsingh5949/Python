
def passing_varargs(name, *args):
    print(name)  # mark
    print(args)  # ('suja', 2, None, True)  , takes varargs as tuple


passing_varargs('mark', 'suja', 2 , None, True)


def passing_kvarargs(name, **kargs):
    print(name)
    print(kargs)  # {'description': 'loves python, not so much', 'feedback': None, 'days_passed': 3} , takes kvarargs as dictionary
    print(kargs['description'], kargs['feedback'])


passing_kvarargs('mark', description='loves python, not so much', feedback=None, days_passed = 3)
