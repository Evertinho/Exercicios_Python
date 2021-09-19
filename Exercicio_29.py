# Radar Eletrônico
velocidade = int(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h.')
    multa = (velocidade - 80) * 7
    print(f'Você deve pagar uma multa de \033[1;31mR${multa:.2f}\033[m!')
print('Tenha um bom dia! Dirija com segurança!')
