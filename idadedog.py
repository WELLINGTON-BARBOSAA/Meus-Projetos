# Calculadora da idade humana em cachorro

# Requisitos: porte do cachorro - Pequeno, medio e grande
# Peso 
# idade
# Tabelas de peso
#   P               MEDIO               GRANDE              GIGANTE                                 
#  <= 9.07 ---- 9.52 kg - 22.7 kg ---- 23.1 - 40.8 kg ---- > 40.8kg

'''Ela deverá:
1. Receber o peso do cachorro. OK
2. Receber a idade do cachorro. OK
3. Identificar o porte utilizando sua função classificar_cachorro() OK.
4. Consultar o dicionário idades.
5. Retornar a idade humana equivalente.'''

def calcular_idade_humana (peso, idade):   
    
    classi = classificar_cachorro(peso)

    resultado = idades[classi][idade]
    
    return resultado

def classificar_cachorro(peso):

    if peso <= 9.07:
        return 'pequeno'

    elif 9.08 <= peso <= 22.7:
        return 'medio'

    elif 23 <= peso <= 40.8:
        return 'grande'

    else:
        return'gigante'


idadePequeno = {
    1: 15,
    2: 24,
    3: 28,
    4: 32,
    5: 36,
    6: 40,
    7: 44,
    8: 48,
    9: 52,
    10: 56,
    11: 60,
    12: 64,
    13: 68,
    14: 72, 
    15: 76,
    16: 80,
    17: 84,
    18: 88,
    19: 92,
    20: 96 
}

idadeMedio = {
    1: 15,
    2: 24,
    3: 28,
    4: 33,
    5: 37,
    6: 42,
    7: 47,
    8: 51,
    9: 56,
    10: 60,
    11: 65,
    12: 69,
    13: 74,
    14: 78,
    15: 83,
    16: 87,
    17: 92,
    18: 96,
    19: 101,
    20: 105
}

idadeGrande = {
    1: 15,
    2: 24,
    3: 30,
    4: 35,
    5: 40,
    6: 45,
    7: 50,
    8: 55,
    9: 61,
    10: 66,
    11: 72,
    12: 77,
    13: 82,
    14: 88,
    15: 93,
    16: 99,
    17: 104,
    18: 109,
    19: 115,
    20: 120
}

idadeGigante = {
    1: 15,
    2: 24,
    3: 32,
    4: 37,
    5: 42,
    6: 49,
    7: 56,
    8: 64,
    9: 71,
    10: 78,
    11: 86,
    12: 93,
    13: 101,
    14: 108,
    15: 115,
    16: 123
}

idades = {
    'pequeno': idadePequeno,
    'medio': idadeMedio,
    'grande': idadeGrande,
    'gigante': idadeGigante
}

peso_digitado = float(input('Digite o peso do cachorro: '))
idade_digitada = int(input('Digite a idade do seu cachorro: '))

resultado = calcular_idade_humana(peso_digitado, idade_digitada)

print(f'A idade humana equivalente  é {resultado} anos')

