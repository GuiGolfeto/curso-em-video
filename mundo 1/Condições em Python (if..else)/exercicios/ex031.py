km = float(input('Qual a distancia da viagem? Km'))

if km <= 200:
    valor = km * 0.50
    print(f'O valor para {km}Km é de {valor}')
if km > 200:
    pas = km * 0.45
    print(f'O valor para {km}km é de {pas}')
