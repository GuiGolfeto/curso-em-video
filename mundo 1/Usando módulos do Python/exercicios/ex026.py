frase = str(input('Digite uma frase: '))
qtd = frase.lower().count('a')
onde = (frase.lower().find('a')) + 1
final = (frase.lower().rfind('a')) + 1

print(f'Sua frase aparece a letra "a" {qtd} vezes')
print(f'O "a" primeiro aparece na posição de numero {onde}')
print(f'O ultimo "a" aparece na posição de numero {final}')
