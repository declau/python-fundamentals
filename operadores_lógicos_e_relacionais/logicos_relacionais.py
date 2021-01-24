# -*- coding: utf-8 -*-

x = 2
y = 3
separacao = "--------------------------"
x = y

print("Relacionais")
print(x)
print(x == y)
print(separacao)
x = 2
print(x == y)
print(x < y)
print(x <= y)
print(x > y)
print(x >= y)
print(x != y)

print(separacao)
print("Lógicos")
soma = x + y
z = 2
print(x == y and x == soma)
print(x == y or x == z)