from math import hypot
a = float(input('Informe o comprimento do cateto A: '))
b = float(input('Informe o comprimento do cateto B: '))
c = hypot(a, b)

print('A hipotenusa do cateto A de {} e do cateto B de {}, possui o valor de {:.2f}'.format(a, b, c))