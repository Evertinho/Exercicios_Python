# Ano Bissexto
from datetime import date
ano = int(input('Que ano você quer analisar? Coloque 0 para analisar o ano atual:  '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'\033[1;32mO ano {ano} é BISSEXTO.\033[m')
else:
    print(f'\033[1;31mO ano {ano} NÃO é BISSEXTO.\033[m')
