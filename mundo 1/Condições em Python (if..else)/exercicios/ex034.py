salario = float(input('Digite seu salario: R$'))

if salario >= 1250:
    new = salario + (salario * 10 / 100)
    print(f'Já que seu salario é de R${salario}, então seu aumento é de 10%')
    print(f'Seu novo salario é de R${new}')
if salario < 1250:
    new = salario + (salario * 15 / 100)
    print(f'Já que seu salario é de R${salario}, então seu aumento é de 15%')
    print(f'Seu novo salario é de R${new}')
