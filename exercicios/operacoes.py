# Escreva um programa que receba dois números e um sinal,
# e faça a operação matemática definida pelo sinal.

numero1 = float(input("Digite o primeiro número:"))
sinal = input("Qual operação desejada?:")
numero2 = float(input("Digite o segundo número:"))

if sinal == "+":
    op = numero1 + numero2

elif sinal == "-":
    op = numero1 - numero2

elif sinal == "/":
    op = numero1 + numero2

elif sinal == "*":
    op = numero1 * numero2

else:
    print("Sinal inválido.")

print("operação selecionada foi: " + sinal + "\n" + "Resultado: " + str(op))
