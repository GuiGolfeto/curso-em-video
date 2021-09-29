km = float(input('Qual velocidade do seu carro? '))
media = float(80)

if km > 80:
    multa = (km - 80) * 7.00
    print(f'Você esta a cima da velocidade permitida que é {media}')
    print(f'Como você estava a {km}Km/h, o valor da multa ira ser R${multa}')
else:
    print('Parabéns, Você esta no limite de velocidade')
