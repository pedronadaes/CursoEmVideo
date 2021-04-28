import pygame
pygame.init()
pygame.mixer.music.load("exemplo.mp3")
pygame.mixer.music.play()
pygame.event.wait()

#programa para tocar mp3
#colar arquivo no projeto, em load() identificar nome do arquivo