pr = float(input('Digite o preço do produto: R$'))
desc = float(input('Digite a porcentagem de desconto oferecido '))
v_desc = (pr * desc)/100

print('O valor do desconto é: R${}'.format(v_desc))
print('O preço do produto com desconto é: R${:.2f}'.format(pr - v_desc))