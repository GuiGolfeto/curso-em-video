alt = float(input('Digite a altura em metros: '))
lar = float(input('Digite a largura em metros: '))
area = alt * lar
tinta = area / 2

print ('a area do local é de {:.2f} metros quadrados, portanto é necessario de {:.2f} litros de tinta'.format(area, tinta))