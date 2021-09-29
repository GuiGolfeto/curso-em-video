city = str(input('Qual sua cidade? '))
sant = 'santo' in city[:5].lower().strip()

if sant == True:
    print('Sua cidade tem Santo!')
else:
    print('Sua cidade não tem Santo :(')
