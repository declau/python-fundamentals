a = {1, 2, 2, 3, 4}
b = {3, 3, 4, 4, 5}

# Intersection
print(a.intersection(b))

# Union
print(a.union(b))

# Difference
print(a.difference(b))
print(b.difference(a))


# Symmetric Difference
# returns a new set with elements present in either a or b but not in both
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

# Testing membership
print(1 in a)
print(6 in a)

# Length
print(len(a))
print(len(b))
