from math import sin, cos, tan,radians

angulo = float(input('Digite um angulo: '))
new = radians(angulo)
sen = sin(new)
coss = cos(new)
tann = tan(new)

print(f'O seno desse angulo é {sen :.2f}, o coseno {coss :.2f} e a tangente é {tann :.2f}')
