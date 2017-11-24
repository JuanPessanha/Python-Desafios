import math
a = float(input('Digite um ângulo para saber seu Seno, Coseno e Tangente: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))

print('O ângulo {:.2f}º possuí: \nO seno de {:.2f}º \nO coseno de {:.2f}º \nA tangente de {:.2f}º'.format(a, s, c, t))