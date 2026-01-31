''' Faça um Programa que pergunte quanto você ganha por hora e o número de horas 
trabalhadas no mês.Calcule e mostre o total do seu salário no referido mês, 
sabendo-se que são descontados 11% para o Imposto de Renda, 
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

    A -  salário bruto. - OK 
    B -  quanto pagou ao INSS. (Criar uma formula)
    C - quanto pagou ao sindicato(Se tiver).
    D - o salário líquido. (Criar uma formula)
    E - calcule os descontos e o salário líquido, conforme a tabela abaixo: '''

salario_mes  = float(input('Seu salario mensal: '))
salario_dia = salario_mes / 30 
salario_hora = float (input('Digite hora trabalhada no dia: '))
print(f'Seu dia trabalhado é {salario_dia}')
print(f'Sua hora trabalhada é de {salario_dia/salario_hora}')
print(f'Sua hora tralhada é de {salario_hora}')
print(f'Seu salario bruto é de {salario_mes}')


aliquota1 = (7.5 / 100) * salario_mes
aliquota2 = (9 / 100) * salario_mes - 22.77
aliquota3 = (12 / 100) * salario_mes - 106.59
aliquota4 = (14 / 100) * salario_mes - 190.40


if salario_mes >= 1518: 
    print(f'Seu salário liquido é de: R$ {salario_mes - aliquota1}')

elif salario_mes >= 1518 and  salario_mes <= 2793:
    print(f'Seu salário liquido é de: R$ {salario_mes - aliquota2}')

elif salario_mes >= 2793 and salario_mes <= 4190:
    print(f'Seu salário liquido é de: R$ {salario_mes - aliquota3}')

elif salario_mes >= 4190 and salario_mes <= 8157: 
    print(f'Seu salário liquido é de: R$ {salario_mes - aliquota4}')

else:
    print('Algo deu errado')