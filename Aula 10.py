n1 = float(input('Digite a sua nota do 1º Bimestre: '))
n2 = float(input('Digite a sua nota do 2º Bimestre: '))
n3 = float(input('Digite a sua nota do 3º Bimestre: '))
n4 = float(input('Digite a sua nota do 4º Bimestre: '))
media = (n1 + n2 + n3 + n4) / 4

if media >= 7:
    print('\nSua média de notas é: {:.2f}; Parabéns você foi aprovado!'.format(media))
else:
    print('\nSua média de notas é: {:.2f}; Infelizmente você não passou.'.format(media))
