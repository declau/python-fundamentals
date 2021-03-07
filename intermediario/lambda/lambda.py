from functools import reduce

add10 = lambda x: x + 10
print(add10(5))

mult = lambda x, y: x * y
print(mult(2, 5))


# sorted
points2D = [(1, 2), (15, 1), (5, -15), (10, 4)]

points2D_soterd = sorted(points2D, key=lambda x: x[1])
points2D_soterd_pĺus = sorted(points2D, key=lambda x: x[0] + x[1])

print(points2D)
print(points2D_soterd)
print(points2D_soterd_pĺus)

# map
# map(sunf, seq)

a = [1, 2, 3, 4, 5]
b = map(lambda x: x * 2, a)
print(list(b))

c = [x * 3 for x in a]  # list comprehension
print(list(c))

# filter
# filter(func, seq)

d = [1, 2, 3, 4, 5, 6]
e = filter(lambda x: x % 2 == 0, d)

print(list(e))

e = [x for x in d if x % 2 == 0]  # list comprehension
print(list(e))


# reduce
# reduce(func, seq)
f = [1, 2, 3, 4]
product_f = reduce(lambda x, y: x * y, f)
print(product_f)

# output 24