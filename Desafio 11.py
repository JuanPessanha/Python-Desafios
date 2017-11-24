alt = float(input('Qual é a altura da parede? '))
lar = float(input('Qual é a largura da parede? '))
area = alt*lar

print('A área da parede é {:.1f}M², e a quantidade de tinta que será necessára é {:.1f}L.'.format(area, area/2))