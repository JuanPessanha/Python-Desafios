num = input('Digite um número de 0 a 9999: ')
div_num = num.replace('', ' ').split()
comp_num = len(div_num)
if comp_num > 4:
    print('O número {}, possui mais do que 4 digitos, favor inserir um número válido!!!'.format(num))
elif 1 == comp_num:
    print('Unidade: {}'.format(div_num[0]))
elif 2 == comp_num:
    print('Unidade: {}'.format(div_num[1]))
    print('Dezena: {}'.format(div_num[0]))
elif 3 == comp_num:
    print('Unidade: {}'.format(div_num[2]))
    print('Dezena: {}'.format(div_num[1]))
    print('Centena: {}'.format(div_num[0]))
else:
    print('Unidade: {}'.format(div_num[3]))
    print('Dezena: {}'.format(div_num[2]))
    print('Centena: {}'.format(div_num[1]))
    print('Milhar: {}'.format(div_num[0]))


'''
Forma analoga
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
'''
