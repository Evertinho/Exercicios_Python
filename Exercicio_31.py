# Cálculo de Preço por Distância
distancia = float(input('Qual a distância da viagem em Km? '))
if distancia <= 200:
    print(f'Com a distância de {distancia}Km o preço da passagem será de \033[1;32mR${distancia * 0.50:.2f}\033[m.')
else:
    print(f'Com a distância de {distancia}Km o preço da passagem será de \033[1;32mR${distancia * 0.45:.2f}\033[m.')
