dist = float(input('Quantos KM foram percorridos com o veículo? '))
dias = int(input('Quantos dias o carro foi alugado? '))
aluguel = (dist * 0.15) + (dias * 60)

print('Durante o aluguel, o carro percorreu {}KM, durante {} dias. Totalizando o valor de R${:.2f}'.format(dist, dias, aluguel))