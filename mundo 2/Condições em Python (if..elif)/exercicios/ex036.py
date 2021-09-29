home = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual seu salario? R$'))
anos = int(input('Em quantos anos vai pagar? '))

parcela = home / (anos * 12)

if parcela >= salario * 30 / 100:
    print(f'O valor de cada parcela é de R${parcela :.2f}, sendo assim você não pode comprar a casa')

elif parcela < salario * 30 / 100:
    print(f'O valor de cada parcela é de R${parcela :.2f}, sendo assim você esta apto a comprar a casa')
