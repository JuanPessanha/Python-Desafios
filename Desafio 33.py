n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n2 < n1 < n3:
    print('\nO maior número é {}, e o menor número é {}.'.format(n3, n2))
elif n3 < n1 < n2:
    print('\nO maior número é {}, e o menor número é {}.'.format(n2, n3))
elif n1 < n2 < n3:
    print('\nO maior número é {}, e o menor número é {}.'.format(n3, n1))
elif n3 < n2 < n1:
    print('\nO maior número é {}, e o menor número é {}.'.format(n1, n3))
elif n1 < n3 < n2:
    print('\nO maior número é {}, e o menor número é {}.'.format(n2, n1))
else:
    print('\nO maior número é {}, e o menor número é {}.'.format(n1, n2))


#Realizado com while
'''while (n1 < n2, n3):
    if n2 > n3:
        print('O maior número é {}, e o menor número é {}.'.format(n2, n1))
    else:
        print('O maior número é {}, e o menor número é {}.'.format(n3, n1))
    break

while (n2 < n1, n3):
    if n1 > n3:
        print('O maior número é {}, e o menor número é {}.'.format(n1, n2))
    else:
        print('O maior número é {}, e o menor número é {}.'.format(n3, n2))
    break

while (n3 < n1, n2):
    if n1 > n2:
        print('O maior número é {}, e o menor número é {}.'.format(n1, n3))
    else:
        print('O maior número é {}, e o menor número é {}.'.format(n2, n3))
    break'''

