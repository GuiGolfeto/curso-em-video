name = str(input('Digite seu nome completo: ')).strip()
sobre = 'silva' in name.lower()

if sobre == True:
    print('Seu nome tem Silva!')
else:
    print('Seu nome não tem Silva :(')
