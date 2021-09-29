number = int(input('Digite um numero entre 0 e 9999: '))
uni = number // 1 % 10
dez = number // 10 % 10
cen = number // 100 % 10
mil = number // 1000 % 10

print(f'Unidade: {uni}')
print(f'Dezena: {dez}')
print(f'Centena: {cen}')
print(f'Milhar: {mil}')

