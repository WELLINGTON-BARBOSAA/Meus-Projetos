while True: 

    print('Seja bem vindo ao seu contador de palavra')
    palavra = input('Por favor, digite a palavra: ') 

    palavra_digitada = None

    try:
        palavra_digitada = (palavra).isalpha()
        
    except:
        palavra_digitada = False    

    if palavra_digitada is False:
        print('Voce não digitou palavras, tente novamente')
        continue

    print(f'A palavra digita foi : {palavra}')
    print(len(palavra)) 

    sair = input ('Deseja [s]air do contador: ').lower().startswith('s')
    if sair is True:
        break


