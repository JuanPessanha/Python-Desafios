sal = float(input('Digite o salário do funcionário: '))
sal1 = (sal * 10 / 100)
sal2 = (sal * 15 / 100)

if sal > 1250:
    print('Neste caso o aumento será de 10%, o novo salário será: RS{:.2f}'.format(sal + sal1))
else:
    print('Neste caso o aumento será de 15%, o novo salário será: R${:.2f}'.format(sal + sal2))
