nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo (m/f): ")
estadoCivil = input("Digite seu estado civil: ")

tempoCasada = 0

if sexo == "f" and estadoCivil == "casada":
    tempoCasada = int(input("Digite o tempo de casada (anos): "))

print("\nDados do Usuario:")
print("Nome:", nome)
print("Sexo:", sexo)
print("Estado Civil:", estadoCivil)
if tempoCasada is not None:
    print("Tempo de casada (anos):", tempoCasada)
