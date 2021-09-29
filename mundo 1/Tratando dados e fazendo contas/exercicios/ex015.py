aluguel = float(input('Quantos dias alugados? '))
kms = float(input('Quantos KM foram rodados? '))
preço = (aluguel * 60) + (kms * 0.15)

print(f'O preço a ser pago é de {preço}')
