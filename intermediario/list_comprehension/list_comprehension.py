# Sem usar List comprehension
x = [1, 2, 3, 4, 5]
y = []

for i in x:
    y.append(i**2)

print(x)
print(y)

# List comprehension
a = [1, 2, 3, 4, 5]
b = [i**2 for i in a]

print("Usando list comprehension")
print(a)
print(b)

# Outro exemplo

print("Usando list comprehension - usando condição")
s = [1, 2, 3, 4, 5]
d = [i**2 for i in a]
f = [i for i in s if i % 2 == 1]
g = [i for i in d if i % 2 == 0]

print(s)
print(d)
print(f)
print(g)
