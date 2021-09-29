number = int(input('Escreva um numero inteiro: '))
print('-'*30)
print('Escolha uma das opções para converter o numero inserido:')
metodo = int(input(' 1 para binário \n 2 para octal \n 3 para hexadecimal \n '))

if metodo == 1:
    bina = bin(number)[2:]
    print(f'O numero {number} em binario é {bina}')

elif metodo == 2:
    octal = oct(number)[2:]
    print(f'O numero {number} em octal é {octal}')

elif metodo == 3:
    hexa = hex(number)[2:]
    print(f'O numero {number} em e hex fica {hexa}')
