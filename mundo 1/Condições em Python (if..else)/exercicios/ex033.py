n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
n3 = float(input('Digite o terceiro numero: '))

# Vizualizando o maior numero
maior = n1

if (n2 > maior):
    maior = n2
if (n3 > maior):
    maior = n3

print(f'Entre os numeros escolhidos, o maior deles é {maior}')

# Vizulizando o menor numero
menor = n1

if (n2 < menor):
    menor = n2
if (n3 < menor):
    menor = n3

print(f'Entre os numeros escolhidos, o menor deles é {menor}')
