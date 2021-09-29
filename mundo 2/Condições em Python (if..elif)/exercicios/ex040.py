n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
media = (n1 + n2) / 2

if media <= 5:
    print(f'Sua média foi {media}, portanto está Reprovado')

elif media > 5 and media < 6.9:
    print(f'Sua média foi {media}, portanto está de Recuperação')

elif media >= 7:
    print(f'Parabéns, sua média foi {media} e você foi Aprovado')
