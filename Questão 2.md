
calculo = input("Digite a operação desejada (+, -, *, /): ")
a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))

if calculo == '+':
    resultado = a + b
elif calculo == '-':
    resultado = a - b
elif calculo == '*':
    resultado = a * b
elif calculo == '/':
    resultado = a / b

else:
    resultado = "Operação invalida!"

print("O resultado é:", resultado)
