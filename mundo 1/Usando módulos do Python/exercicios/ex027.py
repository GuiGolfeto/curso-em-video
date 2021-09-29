name = str(input('Digite seu nome completo: ')).strip()
lista = name.split()

print(f'Nome completo: {name}')
print(f'Primeiro nome: {lista[0]}')
print(f'Ultimo nome: {lista[-1]}')
