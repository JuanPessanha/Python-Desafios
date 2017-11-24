sal = float(input('Informe o salário atual do funcionário: '))
rea = float(input('Informe o valor da porcentagem do reajuste '))
aum = (sal * rea)/100

print('O valor do reajuste para o funcionário será de R${:.2f}'.format(aum))
print('O novo salário do funcionário com reajuste será de: R${:.2f}'.format(sal + aum))