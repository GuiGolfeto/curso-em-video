import datetime
ano = int(input('Digite o ano em que nasceu: '))
today = datetime.date.today()
idade = today.year - ano

if idade <= 9:
    print(f'Você tem {idade} anos, então sua categoria é Mirim')
elif 9 < idade <= 14:
    print(f'Você tem {idade} anos, então sua categoria é Infantil')
elif 14 < idade <= 19:
    print(f'Você tem {idade} anos, então sua categoria é Junior')
elif idade == 20 and idade == 19:
    print(f'Você tem {idade} anos, então sua categoria é Senio')
elif idade > 20:
    print(f'Você tem {idade} anos, então sua categoria é MASTER')
