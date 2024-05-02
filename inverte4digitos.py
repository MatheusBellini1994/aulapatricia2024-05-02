n = int(input("Digite um número de 4 dígitos: "))

x = n

a = x%10

x = x//10

b = x%10

x = x//10

c = x%10

x = x//10

d = x%10

x = x//10

print(f"O inverso de {n} é {a}{b}{c}{d}.")
