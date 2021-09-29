produto = float(input('Digite o valor do produto: '))
desc = float(input('Digite o valor do desconto em %: '))
final = produto - (desc * produto / 100)

print ('O produto com {}% de desconto fica por {} reais'.format(desc, final))
