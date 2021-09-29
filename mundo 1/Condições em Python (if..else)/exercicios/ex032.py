year = int(input('Digite qualquer ano: '))

if (year % 4 == 0 and year % 100!=0) or (year % 400 == 0):
    print(f'O ano {year} é Bissexto')
else:
    print(f'O ano {year} não é Bissexto')
