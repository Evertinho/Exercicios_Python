# Aluguel de Carro
dia = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
pre = (dia * 60) + (km * 0.15)
print(f'O total a pagar é de R${pre:.2f}!')
