city = input('Digite o nome da sua cidade: ').strip().lower()
if 'santo' in city[:5]:
    print('Existe')
else:
    print('Sua cidade não é santificada')