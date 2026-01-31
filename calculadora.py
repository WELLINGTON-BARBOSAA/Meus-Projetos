while True:

    numero1 = input('Digite um numero: ' )
    numero2 = input('Digite outro numero: ' )
    operador = input('Digite operador desejado (/*-+): ' )

    numeros_valid = None


    try:
        num1_float = float(numero1)
        num2_float = float(numero2)
        numeros_valid = True

    except:
        numeros_valid = False
   
    if numeros_valid is False:
        print('Numeros digitado invalido, tente novamente')
        continue
    
    operador_validos = '/*-+'

    if operador not in operador_validos:
        print('operador digitado invalido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    if operador == '+':
        print(num1_float+num2_float)

    elif operador == '-':
        print(num1_float-num2_float)
    
    elif operador == '*':
        print(num1_float*num2_float)
    
    elif operador == '/':
        print(num1_float/num2_float)
            
    else:
         print('Algo deu errado')       

    sair = input ('Deseja [s]air: ').lower().startswith('s')
    if sair is True:
        break