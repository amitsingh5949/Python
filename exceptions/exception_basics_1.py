student = {
    'name': 'amit',
    'age': 28,
    'college': 'utd'
}

try:
    student['address']
except KeyError:
    print('key not found')


try:
    name = 'amit' + 3
except TypeError as error:
    print('error occurred')
    print(error)
except Exception:
    print('unknown error')

print('after catching exception')