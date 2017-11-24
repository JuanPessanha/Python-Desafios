trip = float(input('Digite a distância em KM da viagem: '))
if trip <= 200:
    print('O preço da sua viagem será de: R${:.2f}'.format(trip * 0.50))
else:
    print('O preço da sua viagem que terá taxa extra será: R${:.2f}'.format(trip * 0.45))
