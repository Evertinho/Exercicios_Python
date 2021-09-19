# Par ou Ímpar?
num = int(input('Digite um número inteiro: '))
resto = num % 2
if resto == 0:
    print(f'O número {num} é PAR.')
else:
    print(f'O número {num} é ÍMPAR.')
