from datetime import datetime

def ficha_cadastro():
    nome = input('Digite seu nome completo: ') 
    nome_mae = input('Nome da Mãe: ')
    nome_pai = input('Nome do pai: ')
       
    while True:
        try: 
            idade = int(input('Digite sua idade: '))
            if idade >= 1 and idade < 120:
                break
        except ValueError:
            print('Você não digitou um numero, tente novamente')
    
    moradia_local = endereco()
    telefone = tel()
    cartao_sus = sus()
    data = data_nasc()
    tipo_sangue = sangue()
    fum = fumante()
    aler = alergia()

    cadastro = {
        'nome_completo': nome,
        'data_nasc': data, 
        'anos': idade,
        'mae': nome_mae,
        'pai': nome_pai,
        'local': moradia_local,
        'numero_tel': telefone,
        'numero_sus': cartao_sus,
        'sanguineo': tipo_sangue,
        'fuma': fum,
        'alergico': aler 

    }

    return cadastro

def endereco():
    while True:
        moradia_paciente = input('Digite seu endereço completo: ').strip()
        if not moradia_paciente:
            print('Campo obrigatorio, tente novamente')
            continue
        return moradia_paciente

def tel():
    while True: 
        telefone = input('Digite seu numero de telefone : ')  
        if telefone.isdigit() and len(telefone) ==  11:
            return telefone
        else:
            print('Numero de telefone é invalido, tente novamente')
    
def sus():
    while True:
        cartao_sus = input('Digite o número do cartão do sus(contendo os 15 números): ')
    
        if cartao_sus.isdigit() and len(cartao_sus) == 15:
            return cartao_sus    
        else:
            print('Confira se o adicionou os 15 numeros corretos, tente novamente')
    
def data_nasc():
    while True:
        nasc = input('Digite a sua data de nascimento (DDMMAAAA): ')
        if not nasc.isdigit():
            print('Digite apenas numeros')
            continue

        if len(nasc) != 8:
            print('Digite a data no formato DD/MM/AAAA')
        try:
            data = datetime.strptime(nasc, "%d%m%Y")
            return data
            
        except ValueError:
            print('Data invalida')
            continue

def sangue():
    while True:
        tipo_sangue = input('Digite seu tipo sanguineo(A+, A-, B+, B-, AB+, AB-, O+ e O-): ').upper()
        if tipo_sangue not in ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']:
            print('Tipo sanguineo invalido, tente novamente')
            continue
        return tipo_sangue
    
def fumante():
    while True:
        usuario_fumante = input('Paciente é fumante ou não? (Não ou Sim): ').lower()
        if usuario_fumante not in ['sim', 'não', 'nao']:
            print('Você não digitou corretamente, tente novamente')
            continue
        return usuario_fumante    

def alergia():
    while True:
        usuario_alergico = input('Paciente é alergico a alguma médicação: ').upper()
        if usuario_alergico not in ['NÃO', 'SIM']:
            print('Você não digitou corretamente, tente novamente')
            continue
        return usuario_alergico

lista_pacientes = []

while True:
    print('MENU')
    print()
    print('Digite as opções a seguir: ')
    print('Digite 1, para adicionar paciente')
    print('Digite 2, para listar paciente')
    print('Digite 3, para remover algum paciente da lista')
    print('Digite 4, para sair da lista')
    print()



    try:
        usuario = int(input('Digite a opção desejada (de 1 a 4): '))
        
    except ValueError:
        print('Digite apenas numeros, tenta novamente')
        continue

    if usuario == 1:
        print('Você digitou -> 1 <- para adicionar paciente')
        paciente = ficha_cadastro()
        lista_pacientes.append(paciente)
        print('Paciente adicionado com sucesso')
    
    elif usuario == 2:
        if lista_pacientes == []:
            print('Sua lista se encontra vazia')
            continue
        print('Selecionou -> 2 <-, Lista de paciente: ')

        for i, paciente in enumerate(lista_pacientes, start=1):
            print(f"{i} - {paciente['nome_completo']}")


    elif usuario == 3:
        if lista_pacientes == []:
            print('Sua lista se encontra vazia')
            continue
        remover_paci = int(input('Digite o numero do paciente: '))
        
        if 1 <= remover_paci <= len(lista_pacientes):
            lista_pacientes.pop(remover_paci - 1)
            print('Paciente removido com sucesso')
        else:
            print('Número inválido')
        
        for i, paciente in enumerate(lista_pacientes, start=1):
           print(f"{i} - {paciente['nome_completo']}")
    
    elif usuario == 4:
        print('ENCENRRANDO O PROGRAMA DE PACIENTE')
        break