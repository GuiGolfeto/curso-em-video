reta1 = float(input('Digite o comprimento 1: '))
reta2 = float(input('Digite o comprimento 2: '))
reta3 = float(input('Digite o comprimento 3: '))

if reta1 < (reta2 + reta3) and reta2 < (reta3 + reta1) and reta3 < (reta1 + reta2):
    print('Daria pra fazer um triangulo')
else:
    print('não da pra fazer um triangulo')
