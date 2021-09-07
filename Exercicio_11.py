# Pintando Parede
lar = float(input('Largura da parede em metros: '))
alt = float(input('Altura da parede em metros: '))
area = lar * alt
tin = area / 2
print(f'Sua parede tem a dimensão de {lar:.2f}x{alt:.2f} e sua área é de \033[1;32m{area}m²\033[m.')
print(f'Para pintar a parede, você irá precisar de \033[1;32m{tin:.2f}l\033[m de tinta.')

