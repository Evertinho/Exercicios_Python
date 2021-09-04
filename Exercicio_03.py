# Operações Aritméticas
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
s = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
print(f'A soma entre {n1} e {n2} é igual a \033[1;31m{s}\033[m!')
print(f'A subtração entre {n1} e {n2} é igual a \033[1;31m{su}\033[m!')
print(f'A multiplicação entre {n1} e {n2} é igual a \033[1;31m{m}\033[m!')
print(f'A divisão entre {n1} e {n2} é igual a \033[1;31m{d:.2f}\033[m!')
