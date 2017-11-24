pr = float(input('Informe o preço do produto: '))
desc = float(input('Informe a porcentagem de desconto que será ofericida: '))
v_desc = (pr * desc)/100

print('O preço do produto com desconto será: R${:.2f}'.format(pr - v_desc))