n = int(input("Digite um número natural: "))

x = n

soma = 0

while x !=0:
    soma = soma + x%10
    x = x//10

print(f"A soma dos dígitos de {n} é {soma}")
