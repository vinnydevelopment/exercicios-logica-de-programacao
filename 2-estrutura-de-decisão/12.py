# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#         Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00  
#         (-) INSS ( 10%)                 : R$  110,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00


#Entrada
hora = float(input("Informe o valor da sua hora de trabalho: "))
mes = int(input("Informe quantas horas você trabalha por mês: "))
#Processamento
salario_bruto = hora * mes

if salario_bruto <= 900:
	percentual = 0
elif salario_bruto <= 1500:
	percentual = 5
elif salario_bruto <= 2500:
	percentual = 10
else:
	percentual = 20

IR = (salario_bruto * (percentual / 100))
INSS = salario_bruto * 0.10
FGTS = salario_bruto * 0.11
total_descontos = IR + INSS
salario_liquido = (salario_bruto - total_descontos)
#Saída
print(f"\tSalário Bruto({hora} * {mes}): R${salario_bruto:.2f}")
print(f"\t(-)IR({percentual}%): R${IR:.2f}")
print(f"\t(-)INSS(5%): R${INSS:.2f}")
print(f"\tFGTS(11%): R${FGTS:.2f}")
print(f"\tTotal de descontos: R${total_descontos:.2f}")
print(f"\tSalário Líquido: R${salario_liquido:.2f}")


