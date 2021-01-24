# Faça um programa que receba duas notas digitadas pelo usuário.
# Se a nota for maior ou igual a seis, escreva aprovado,
# senão escreva reprovado.

nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))

nota = nota1 + nota2
resultado = nota / 2

if resultado >= 6:
    print(resultado, "Aprovado!")
else:
    print(resultado, "Reprovado!")
