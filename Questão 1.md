produto = input("Digite o produto: ")
quantidade = int(input("Digite a quantidade do produto: "))
precoUnitario = float(input("Digite o preço unitario do produto: "))

total = quantidade * precoUnitario

if quantidade <= 5:
    descontoPercentual = 0.02
elif quantidade <= 10:
    descontoPercentual = 0.03
else:
    descontoPercentual = 0.05

desconto = total * descontoPercentual

totalAPagar = total - desconto

print("\nDescrição do produto:", produto)
print("Quantidade adquirida:", quantidade)
print("Preço unitario: R$", format(precoUnitario, '.2f'))
print("Total: R$", format(total, '.2f'))
print("Desconto: R$", format(desconto, '.2f'))
print("Total a pagar: R$", format(totalAPagar, '.2f'))
