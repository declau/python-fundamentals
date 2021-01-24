""" Em Python, dicionários são arrays associativos, ou seja, 
    um determinado valor passa a ser vinculado a uma chave.
 """
dicionario_sites = {"Dunha": "dunha.com", "Google": "google.com"}

# imprimindo a chave do dicionário
print(dicionario_sites["Dunha"])

# navegando pelo dicionário
# for dict in dicionario_sites:
#     print(dict)


# navegando pelo dicionário imprimindo chave valor
# for dict in dicionario_sites:
#     print(dict+": "+dicionario_sites[dict])

#  items()
# vai converter p dicionáreio em uma tupla que é um conjunto de dados imutável
# for i in dicionario_sites.items():
#     print(i)

# values()
# vai retornar somente os valores
for i in dicionario_sites.values():
    print(i)
