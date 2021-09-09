# Calculando Descontos
pre1 = float(input('Digite o preço do produto: R$'))
des = pre1 * 0.05
pre2 = pre1 - des
print(f'Valor Inicial: R${pre1:.2f}')
print(f'Desconto de 5%: R${des:.2f}')
print(f'Valor Final: R${pre2:.2f}')
