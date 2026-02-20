def media (tempo, km):
     return tempo / km

def linha_abertura():
    print('-' * 30)
    print('Seja bem vindo a sua calculadora de paces')
    print('-' * 30)

def linha_fechamento():
    print('-' *30)
    print('Calculadora de pace encerrada')
    print('-' *30)

linha_abertura()

while True: 
    try:
        time = float(input('Digite o tempo em minutos: '))
        distancia = float(input('Digite a distancia percorrida: '))
        pace = media(time, distancia)
        print(f'Seu pace é de {pace:.2f} min/km')
        linha_fechamento()
        break

    except Exception:
        print('Voce não digitou numeros')