""" Dada a seguinte lista:

lista = [1,2,3,4,5,6,7,8,9,10]
lista2 = []


Modifique o código a seguir para que lista2 possua apenas números pares. """

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [i for i in lista if i % 2 == 0]

print(lista2)
