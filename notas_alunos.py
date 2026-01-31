'''Desafio — Notas dos Alunos
Crie um programa que:
Peça o nome de um aluno.
Peça três notas (de 0 a 10).
Calcule a média.
Mostre o nome do aluno, a média e a situação:
Média < 5 → Reprovado
5 ≤ Média < 7 → Recuperação
Média ≥ 7 → Aprovado '''

aluno1 = str(input('Digite seu nome: '))
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segeunda nota: '))
nota3 = float(input('Digite sua terceira nota: '))
media = (nota1 + nota2 + nota3) / 3 


if media < 5:
    print(f'Sua média é de {media:.2f}')
    print('Reprovado')
elif media < 7: 
    print(f'Sua média é de {media:.2f}')
    print(f'Recuperação')
else:
    print(f'Sua média foi de {media:.2f}')
    print('Aprovado')
