# Jogo da adivinhação 1
from random import randint
from time import sleep
computador = randint(0, 5)  # Faz o computador escolher aleatoriamente entre 0 e 5
print('_=_' * 19)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar....')
print('_=_' * 19)
jogador = int(input('Em que número eu pensei? '))  # Jogador tenta adivinhar o número
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! Você acertou e venceu!')
else:
    print(f'Que pena, eu pensei no número {computador} e não no número {jogador}!')
