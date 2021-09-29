n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))
met = int(input('Qual metodo quer usar? \n soma: 1 \n subtração: 2 \n divisão: 3 \n multiplicação: 4 \n'))

if met == 1:
    soma = float(n1 + n2)
    print(f'A soma ente {n1} e {n2} é igual a {soma}')

if met == 2:
    subs = float(n1 - n2)
    print(f'A subtração entre {n1} e {n2} é igual a {subs}')

if met == 3:
    div = float(n1 / n2)
    print(f'A divisão entre {n1} e {n2} é igual a {div}')

if met == 4:
    mult = float(n1 * n2)
    print(f'A multiplicação entre {n1} e {n2} é igual a {mult}')
