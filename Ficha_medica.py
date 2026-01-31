while True: 

    print('Ficha médica')

    print('Preencha todos os dados a seguir')

    nome = input('Digite seu nome completo: ')
    data_nascimento = input('Digite sua data de nascimento:  ')
    endereço = input('Digite seu endereço: ')
    cartão_sus = input('Digite seu cartão do SUS: ')
    nume_tel = input('Numero para contato: ')
    nome_mãe = input('Nome da mãe: ')
    nome_pai = input('Nome do pai: ')
    tipo_sanguineo = input('Tipo sanguineo: ')
    fumante = input('Fumante: ')
    alergia_med = input ('Possui alergia a medicamento: ')


    if nome.replace(' ', '').isalpha():
        print('Voce digitado corretamente')
    else:
        print('Digite apenas letras (nome)')


    if  data_nascimento.replace('/', '').isnumeric():
        print('Data de nascimento digitada corretamente')
    else:
        print('Digite apenas numeros(data_nasc)')


    if endereço.isalpha() and endereço.isnumeric:
        print('Nome ou numero incorreto (endereço)')
    else:
        print('Endereço digitado corretamente')


    if len(cartão_sus) < 14 or len(cartão_sus) >16  :
        print('Numeros a mais ou a menos (numero SUS)')
    else:
        print('Numero do sus correto')


    if len (nume_tel) < 8 or len(nume_tel) > 10:   
        print('Numeros a mais ou a menos (Telefone)')
    else:
        print('Numero de telefone esta correto')


    if nome_mãe.replace(' ', '').isalpha() and nome_pai.replace(' ', '').isalpha():
        print('Digitado corretamente')
    else:
        print('Voce digitou algo de errado, olha novamente (Pais)')


    if len(tipo_sanguineo) > 3 :
        print('Tipo Sanguineo incorreto (Tipo de sangue)')
    else:
        print('Tipo sanguineo cadastrado')


    if fumante.lower() in ['Sim', 'sim', 'nao', 'Não', 'não']:
        print('Informação valida')
    else:
        print('Responda apenas (Sim ou Não)')

    if alergia_med.lower() in ['Sim', 'sim', 'Não', 'não', 'nao']:
        print('Informação valida')
    else:
        print('Responda (Sim ou Não)')

    print('Cadastro realizado com sucesso')

    sair = input('Deseja [s]air: ').lower().startswith('s')
    if sair is True:
        break
