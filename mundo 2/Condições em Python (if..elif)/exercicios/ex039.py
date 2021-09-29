import datetime
nasc = int(input('Ano em que nasceu: '))
today = datetime.date.today()
idade = today.year - nasc

alist = str(input('ja se alistou? (s/n)'))

if idade < 18:
    print('Você ainda não precisa de alistar')

elif idade == 18 and alist == 'n':
    print('Ja chegou a hora de se alistar')

elif idade >= 18 and alist == 's':
    print('Parabens, você ja se alistou')

elif idade >= 18 and today != '2021-05-07' and alist == 'n':
    prazo = int(today.day - 9)
    prazo1 = int(today.month - 5)
    print(f'você esta atrazado {prazo1} messes e {prazo} dias')

