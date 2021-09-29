from time import sleep
import random

# Definindo itens
itens = ('Pedra', 'Papel', 'Tesoura')

# jogada do computador
computador = random.randint(0, 2)

# apresentação de opções
print('''Opções:
0- Pedra
1- Papel
2- Tesoura ''')

# jogada do player
player = int(input('Qual sua jogada? '))

# Cadeciando
print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Po')
sleep(1)
# fim cadencia

# o que cada um jogou
print(f'O Computador jogou {itens[computador]}')
print(f'O Player jogou {itens[player]}')

# estruturas condicionais
if computador == 0:  # computador jogou pedra
    if player == 0:
        print('EMPATE')

    elif player == 1:
        print('Player Venceu!')

    elif player == 2:
        print('Computador Venceu!')

    else:
        print('Jogada Invalida...')

elif computador == 1:  # computador jogou papel
    if player == 0:
        print('Computador Venceu!')

    elif player == 1:
        print('EMPATE')

    elif player == 2:
        print('Player Venceu!')

    else:
        print('Jogada Invalida...')

elif computador == 2:  # computador jogou Tesoura
    if player == 0:
        print('Player Venceu!')

    elif player == 1:
        print('Computador Venceu!')

    elif player == 2:
        print('EMPATE')

    else:
        print('Jogada Invalida')
