# Tocando um MP3
import pygame
pygame.init()
# O arquivo MP3 deve estar na mesma pasta que esse código
# Insira o nome do arquivo MP3 no local designado por Música.mp3
pygame.mixer.music.load('Música.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input()
