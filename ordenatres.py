a = input("Digite o primeiro número: ")

b = input("Digite o segundo número: ")

c = input("Digite o terceiro número: ")

temp=0

if a>b:
    temp=a
    a=b
    b=temp

if a>c:
    temp=a
    a=c
    c=temp

if b>c:
    temp=b
    b=c
    c=temp

print(f"O menor número é {a};")
print(f"O número intermediário é {b};")
print(f"E o maior número é {c};")
