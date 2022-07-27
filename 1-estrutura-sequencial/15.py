# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

hora = float(input("Informe quanto você ganha por hora: "))
mes = int(input("Horas trabalhadas no mês: "))

salario_bruto = hora * mes

IR = salario_bruto * 0.11
INSS = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
descontos = IR + INSS + sindicato
salario_liquido = salario_bruto - descontos

print(f"\nSalário bruto: {salario_bruto:.2f}")
print(f"Imposto de renda: R${IR:.2f}")
print(f"INSS: R${INSS:.2f}")
print(f"Sindicato: {sindicato:.2f}")
print(f"Salário líquido: R${salario_liquido:.2f}")