print('-'*30)
print('CALCULADORA DE PACE')
print('-'*30)

def media (tempo, km):
     return tempo / km

while True: 
    try:
        time = float(input('Digite o tempo: '))
        distancia = float(input('Digite a distancia percorrida: '))
        pace = media(time, distancia)
        print(f'Seu pace é de {pace:.2f} min/km')
        break

    except Exception:
        print('Voce não digitou numeros')