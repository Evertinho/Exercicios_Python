#Catetos e Hipotenusa
from math import hypot
co = float(input('Comprimento do cateto oposto em cm: '))
ca = float(input('Comprimento do cateto adjacente em cm: '))
hip = hypot(co, ca)
print(f'A hipotenusa é igual a \033[1;32m{hip:.2f}\033[m.')
