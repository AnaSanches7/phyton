import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('como tudo deve ser.mp3')

pygame.mixer.music.play()

input()

pygame.event.wait()
