from random import choice

name1 = str(input('Digite o nome do aluno 1: '))
name2 = str(input('Digite o nome do aluno 2: '))
name3 = str(input('Digite o nome do aluno 3: '))
name4 = str(input('Digite o nome do aluno 4: '))

result = choice([name1, name2, name3, name4])

print(f'O sorteado para apagar a lousa é {result}')
