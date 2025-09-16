# Faça um algoritmo que leia um número inteiro
# e mostre uma mensagem indicando se este número é par ou ímpar e se é positivo ou negativo.

num = int(input("Por favor digie um número: "))

if num % 2 == 0:
    print("O número é par.")
else:
    print("O  número é ímpar.")
    
if num >= 0:
    print("O número é pesutivo")
else:
    print("O número é neugativo.")