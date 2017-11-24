vel = float(input('Escreva a sua velocidade atual: '))
if vel > 80:
    exc = (vel - 80)
    print('Você esta {:.1f}KM/h acima da velocidada max permitida e será multado em R${:.2f}'.format(exc, exc * 7))

print('Pode prosseguir, você está dentro do limite de velocidade!')
