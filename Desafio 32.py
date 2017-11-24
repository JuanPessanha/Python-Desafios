ano = int(input('Digite um ano para saber se ele é bissexto: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 00:
    print('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {} não é Bissexto'.format(ano))
