from random import randint

loop = 1

while loop != 0:
    num = randint(0, 100)
    option = input('Para converter {} para binário digite 1, 2 para octal ou 3 para hexadecimal: '.format(str(num)))

    if option == '1':
        binario = str(bin(num))
        print(binario[2:])

    elif option == '2':
        octa = str(oct(num))
        print(octa[2:])

    elif option == '3':
        hexa = str(hex(num))
        print(hexa[2:])

    else:
        print('Digite apenas 1, 2 ou 3!')

