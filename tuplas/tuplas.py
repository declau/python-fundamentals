# Tuple: ordered, immutable, allows duplicate elements

minha_tupla = ("Denis", 38, "Brasil")
# minha_tupla = ("Denis",) # Definir um unico elemento em uma Tupla
# minha_tupla = "Denis", 38, "Brasil" # Parenteses são opcionais

print(minha_tupla)

minha_tupla2 = tuple(["Denis", 38, "Brasil"])
# Verificando se um elemento pertence a Tupla
if "Denis" in minha_tupla2:
    print("Yes")
else:
    print("No")

# Percorrer os elementos em uma Tupla
for i in minha_tupla2:
    print(i)

# passando o index da Tupla
item = minha_tupla2[2]
print(item)
