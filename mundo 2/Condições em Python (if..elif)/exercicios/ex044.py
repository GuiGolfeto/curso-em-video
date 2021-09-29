produto = float(input('Digite o valor do produto: R$'))
print('Digite o metoro de pagamento:')
print('-'*25)

#metodos de pagamento
pagamento = int(input("""1- Dinheiro/Cheque
2- 1x Cartão
3- 2x Cartão
4- 3x ou mais
"""))

if pagamento == 1:
    valor = produto - (produto * 10 /100)
    print(f'O Valor a ser pago é R${valor}')

elif pagamento == 2:
    valor = produto - (produto * 5 / 100)
    print(f'O Valor a ser pago é R${valor}')

elif pagamento == 3:
    valor = produto / 2
    print(f'O Valor das parcelas sera R${valor}')

elif pagamento == 4:
    mes = int(input('Por quantos meses quer pagar? '))
    valor = produto - (produto * 0.15 * mes)
    print(f'Em {mes}x fica por R${valor}')
