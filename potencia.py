x = float(input("Digite a base da potência: "))

y = int(input("Digite um expoente inteiro e não-negativo: "))

potencia = 1

for i in range(y):
    potencia = potencia*x

print(f"{x}^{y} = {potencia}")
