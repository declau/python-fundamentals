""" FUNCTION: callable that determines the condition or 
None then use the identity function for filtering (positional- only)

ITERABLE: iterable that will be filtered (positional-only)
 """
names = ["Fred", "Wilma", "Barney"]


def long_name(name):
    return len(name) > 5


filter(long_name, names)
# returns a generator
# Out: <filter at 0x1fc6e443470>
print(list(filter(long_name, names)))  # cast to list
# Out: ['Barney']

print([name for name in names if len(name) > 5])  # equivalent list comprehension
# Out: ['Barney']