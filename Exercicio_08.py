# Conversor de Medidas
me = int(input('Uma distância em metros: '))
km = me / 1000
hm = me / 100
dam = me / 10
dm = me * 10
cm = me * 100
mm = me * 1000
print(f'A medida de {me}m é equivalente a:')
print(f'{km:.3f}km')
print(f'{hm:.2f}hm')
print(f'{dam:.1f}dam')
print(f'{dm:.0f}dm')
print(f'{cm:.0f}cm')
print(f'{mm:.0f}mm')
