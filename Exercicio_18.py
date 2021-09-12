# Seno, Cosseno e Tangente
from math import sin, cos, tan, radians
ang = float(input('Digite o valor do ângulo: '))
seno = sin(radians(ang))
cose = cos(radians(ang))
tang = tan(radians(ang))
print(f'O SENO de {ang:.1f} é igual a {seno:.3f}.')
print(f'O COSSENO de {ang:.1f} é igual a {cose:.3f}.')
print(f'A TANGENTE de {ang:.1f} é igual a {tang:.3f}.')
