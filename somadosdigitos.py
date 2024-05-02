n = int(input("Digite um número natural: "))

soma = 0

while n !=0:
    soma = soma + n%10
    n = n//10

print(f"A soma dos dígitos é {soma}")
