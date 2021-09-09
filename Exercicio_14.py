# Conversor de Temperatura
cel = float(input('Digite a temperatura em ºC: '))
far = (cel * 9 / 5) + 32
kel = cel + 273.15
print(f'A temperatura de {cel:.1f}ºC corresponde a {far:.2f}ºF e a {kel:.2f}K!')
