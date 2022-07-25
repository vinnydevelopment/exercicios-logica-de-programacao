#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

hora = float(input("Informe quanto você ganha por hora: "))
mes = int(input("Informe a quantidade de horas trabalhadas no mês: "))

total = hora * mes

print(f"O seu salário é R${total:.2f}")