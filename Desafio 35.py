a = float(input('Digite a medida do lado A: '))
b = float(input('Digite a medida do lado B: '))
c = float(input('Digite a medida do lado C: '))

if (a - b) < c < (a + b):
    print('Verdadezinha')
else:
    print('Mentirinha')
