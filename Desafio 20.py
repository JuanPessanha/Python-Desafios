from random import shuffle
al1 = input('Primeiro Aluno: ')
al2 = input('Segundo Aluno: ')
al3 = input('Terceiro Aluno: ')
al4 = input('Quarto Aluno: ')
lista = [al1, al2, al3, al4]
#neste caso o shuffle embarlhou a ordem dos valores no próprio array da variável, e ao chamá-la mais abaixo no print os valores vem embaralhados
shuffle(lista)
print('A ordem será: {}'.format(lista))