frase = 'Curso em Video Python'
fatiamento = frase[9:13]
analise1 = len(frase)
analise2 = frase.count('o')
analise3 = frase.find('deo')
analise4 = 'Curso' in frase
trans1 = frase.replace('Python', 'C#')
trans2 = frase.upper()
trans3 = frase.lower()
trans4 = frase.capitalize()
trans5 = frase.title()
oooo = frase.split()
oooo = "-".join(frase)

print(f'fatiamento: {fatiamento}')
print(f'comprimento: {analise1} / Quantas vezes aparece a letra o {analise2} / onde encontrou deo {analise3}'
      f' / existe a palavra curso? {analise4}')
print(f"""Era {frase} e ficou {trans1}
Era {frase} e ficou {trans2}
Era {frase} e ficou {trans3}
Era {frase} e ficou {trans4}
Era {frase} e ficou {trans5}""")

print(oooo)


