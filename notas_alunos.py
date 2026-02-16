'''Desafio — Notas dos Alunos
Crie um programa que:
Peça o nome de um aluno.
Peça 2 notas (de 0 a 10).
Calcule a média.
Mostre o nome do aluno, a média e a situação:
Média < 5 → Reprovado
5 ≤ Média < 7 → Recuperação
Média ≥ 7 → Aprovado '''

def linha():
    print('BEM VINDO A SUA CALCULADORA DE MEDIA')
    print ('-' *50)

def encerramento():
    print('CALCULADORA ENCERRADA')
    print('-' * 50)

def media (x,y):
    return (x + y) / 2 

linha()
while True:
    try:
        aluno = input('Digite seu nome: ')
        nota1 = float(input('Digite sua primeira nota: '))
        nota2 = float(input('Digite sua segunda nota: '))
        
        res_media = media(nota1, nota2)
        
        
        print(f'{aluno}, você com a média de {res_media:.2f}')
        if res_media < 5 :
            print(f'REPROVADO, com média de {res_media:.2f}')    
        elif res_media < 7:
            print(f'RECUPERAÇÃO, com média de {res_media}')
        else:
            print(f'APROVADO, com a média de: {res_media}')
        
        continuar = input('Deseja continuar calculando media? (sim/nao): ').lower()
        if continuar != 's':
            encerramento()
            break

    except ValueError:
        print('Você digitou errado, tente novamente')


    