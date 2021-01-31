names = ['Fred', 'Wilma', 'Barney']


def long_name(name):
    return len(name) > 5


filter(long_name, names)
# returns a generator
# Out: <filter at 0x1fc6e443470>
print(list(filter(long_name, names)))  # cast to list
# Out: ['Barney']
