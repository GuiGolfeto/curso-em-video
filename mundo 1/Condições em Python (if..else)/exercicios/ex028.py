import random
from time import sleep

print('-'*28)
print(' '*4, 'Jogo do adivinha')
print('-'*28)

esc = int(input('Qual numero entre 0 a 5 você acha que vai sair? ')) #resposta que o jogador acha
print('Processando...')
sleep(2)

number = random.randint(0, 5) # numero que a maquina vai pensar

if esc == number:
    print(f'O numero que caiu foi {number}')
    print('Parabéns, você ganhou!')
else:
    print(f'O numero que caiu foi {number}')
    print('Que pena você perdeu :(')

