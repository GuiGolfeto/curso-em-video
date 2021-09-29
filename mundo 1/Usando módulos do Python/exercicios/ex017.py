from math import hypot

op = float(input('Digite o valor do Cateto oposto: '))
ad = float(input('Digite o valor do Cateto adjacente: '))
hip = hypot(op, ad)

print(f'O valor da hipotenusa é {hip :.2f}')
