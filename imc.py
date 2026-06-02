def imc():
    peso = float(input('Digite seu peso: '))
    altura = float(input('Digite sua altura: '))     
    resultado = peso / (altura * altura)
    return resultado

conta = imc()

print(f'Seu imc é de: {conta:.2f}')
if conta <= 18.5:
   print('Abaixo do peso')
    
elif conta <= 24.9:
   print('Normal')

elif conta <= 29.9:
   print('Sobrepeso')

elif conta <= 34.9:
   print('Obesidade I')

elif conta <= 39.9:
   print('Obesidade II')

else:
   print('Obesidade GRAVE')
