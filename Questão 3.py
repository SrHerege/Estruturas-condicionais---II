kgMorango = float(input("Digite a quantidade de morangos (kg): ")) #usando aspas duplas por vicio de linguagem em C prof
kgMaca = float(input("Digite a quantidade de maçãs (kg): "))

if kgMorango <= 5:
    precoMorango = 2.50
else:
    precoMorango = 2.20

if kgMaca > 5:
    precoMaca = 1.80
else:
    precoMaca = 1.50

totalMorango = kgMorango * precoMorango
totalMaca = kgMaca * precoMaca

total = totalMorango + totalMaca

if kgMorango + kgMaca > 8 or total > 25.00:
    desconto = total * 0.10
else:
    desconto = 0.00

totalAPagar = total - desconto

# Exibe os resultados
print("\nQuantidade de morangos (Kg):", kgMorango)
print("Quantidade de maçãs (Kg):", kgMaca)
print("Total sem desconto: R$", format(total, '.2f'))
print("Desconto: R$", format(desconto, '.2f'))
print("Total a pagar: R$", format(totalAPagar, '.2f'))
