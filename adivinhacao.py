import random

n = random.randint(1,100)

print("Adivinhe um número de 1 a 100!")

x = 0

while x!=n:
    x= int(input("Qual você acha que é o número? "))
    if x==n:
        print("Parabéns! Você é um grande adivinhador de números!")
    elif n<x:
        print("O número é menor que isso.")
    else:
        print("O número é maior que isso.")
