# Conversor de Moedas
real = float(input('Quantos reais você tem? R$'))
dolar = real / 5.22
euro = real / 6.38
libra = real / 7.43
franco = real / 5.81
print(f'Com R${real:.2f} você consegue comprar: ')
print('-' * 35)
print(f'US${dolar:.2f}')
print(f'€{euro:.2f}')
print(f'£{libra:.2f}')
print(f'Fr{franco:.2f}')
