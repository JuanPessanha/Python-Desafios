sal = float(input('Digite o salário atual do funcionário: R$'))
aum = float(input('Digite a porcentagem do reajuste do salário: '))
v_aum = (sal * aum) / 100

print('O reajuste será de R${:.2f} para o funcionário'.format(v_aum))
print('O novo salário do funcionário já com reajuste será de R${:.2f}'.format(sal + v_aum))
