cpf = int(input("Digite o número do seu CPF, somente os dígitos, sem pontos ou traços: "))

V1=0

for i in range(9):
    V1 = V1 + ((cpf // 10**(i+2)) % 10) * (i+2)

V1 = 11 - V1%11

if V1>=10:
    V1=0

V2=0

for i in range(10):
    V2 = V2 + ((cpf // 10**(i+1)) % 10) * (i+2)

V2 = 11 - V2%11

if V2>=10:
    V2=0

if cpf%100 == 10*V1 + V2:
    print("CPF válido!")
else:
    print("CPF inválido!")


