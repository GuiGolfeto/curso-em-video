peso = float(input('Diga seu peso em kg: '))
altura = float(input('Diga sua altura em metros: '))
imc = peso / (altura * altura)

print(f'{imc :.2f}')
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 >= imc < 25 :
    print('Peso ideal')
elif 25 > imc < 30:
    print('Sobrepeso')
elif 30 > imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('obesidade morbida')