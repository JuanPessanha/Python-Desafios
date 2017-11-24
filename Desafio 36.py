valor = float(input('Qual é o valor do imóvel desejado? R$'))
salaraio = float(input('Qual é o seu salário atual? R$'))
anos = int(input('Em quantos anos pretende pagar? '))
prestação = valor / anos / 12
meses = anos * 12

if prestação >= salaraio * 30 / 100:
    print('Empréstimo negado! A parcela de {:.2f} está acima dos 30% de seu salário.'.format(prestação))
elif anos == 0 or salaraio == 0 or anos == 0:
    print('Favor, preencher todos os camos de maneira correta, valores zerados não são permitidos.')
else:
    print('Epréstimo aprovado! Serão {} parcelas de R${:.2f} ao mês.'.format(meses, prestação))
print('{:.2f}'.format(prestação))
