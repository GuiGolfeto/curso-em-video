from random import shuffle

grupo1 = str(input('Grupo 1: '))
grupo2 = str(input('Grupo 2: '))
grupo3 = str(input('Grupo 3: '))
grupo4 = str(input('Grupo 4: '))

todos = (f'{grupo1} {grupo2} {grupo3} {grupo4}'.split())
shuffle(todos)
print(f'A ordem da apresentação sera \n{todos}')
