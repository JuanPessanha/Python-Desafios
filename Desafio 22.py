nome = input('Digite o seu nome completo: ').strip()
div_nome = nome.split()

print('Maiusculo: {}'.format(nome.upper()))
print('Minusculo: {}'.format(nome.lower()))
print('Total de letras: {}'.format(len(nome.replace(' ', ''))))
print('Total de letras do primeiro nome: {}'.format(len(div_nome[0])))
