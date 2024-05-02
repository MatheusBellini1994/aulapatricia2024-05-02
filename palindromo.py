palavra = input("Escreva uma palavra: ")

len = len(palavra)

reverso = ""

for letra in palavra:
    reverso = letra + reverso

if reverso==palavra:
    print(f'A palavra "{palavra}" é um palíndromo!')
else:
    print(f'A palavra "{palavra}" não é um palíndromo.')


