# 1. Faça um algoritmo que leia dois números e apresente-os em ordem crescente. Use estrutura de desvio condicional simples.

num1 = int(input("Por favor, digite o primeiro número: ")) 
num2 = int(input("Por favor, digite o segundo número: "))

if  num1 >= num2:
    print(f"{num2}  {num1}")
else:
    print(f"{num1}  {num2} ")