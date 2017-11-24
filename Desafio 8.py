n1 = float(input('Digite o valor em metros: '))
km = n1/1000
hm = n1/100
dam = n1/10
dm = n1*10
cm = n1*100
mm = n1*1000

print('Você digitou {} metros \nValor em centímetros: {} \nValor em milímetros: {} \nValor em decímetros: {} \nValor em decâmetros: {} \nValor em hectometros: {} \nValor em quilometros: {}'.format(n1, cm, mm, dm, dam, hm, km))