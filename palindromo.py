palavra = input("Escreva uma palavra: ")

len = len(palavra)

reverso = ""

for i in range(len):
    reverso = reverso + palavra[len-1-i]

if reverso==palavra:
    print(f'A palavra "{palavra}" é um palíndromo!')
else:
    print(f'A palavra "{palavra}" não é um palíndromo.')


