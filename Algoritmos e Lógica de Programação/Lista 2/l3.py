#3. Faça um algoritmo que calcule a média aritmética das 3 notas de um aluno e mostre,
# além do valor da média, uma mensagem de "Aprovado", caso a média seja igual ou superior a 6, ou a mensagem "Reprovado", caso contrário.

n1 = float(input("Declare a primeira nota: "))
n2 = float(input("Declare a segunda nota: "))
n3 = float(input("Declare a terceira nota: "))

media = (n1+n2+n3)/3
print(f"Sua média é: {media}")

if media > 6:
    print("Você foi aprovado babygirl.")
else:
    print("Você foi reprovado babygirl.")
