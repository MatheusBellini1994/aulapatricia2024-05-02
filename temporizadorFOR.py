min = int(input("Digite o número de minutos: "))

print(f"{min}min 00s")

for i in range(min):
    for j in range(60):
        print(f"{min-1-i}min {59-j}s")
