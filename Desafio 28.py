import random
num = random.randint(0, 5)
print('Estou pensando em um número entre 0 e 5.... Pronto! Você consegue adivinhar o número que eu pensei?')
usr = int(input('\nTente advinhar o número entre 0 e 5 que eu o SEU COMPUTADOR pensei: '))

if usr >= 6:
    print('\nVocê prestou atenção no que eu falei? É um número de 0 a 5, tenta de novo!')
elif usr == num:
    print('\nNós dois estamos em sintonia, você descobriu o número {}.'.format(num))
else:
    print('\nERROU, eu pensei no número {}! Tenta de novo meu parceiro'.format(num))
