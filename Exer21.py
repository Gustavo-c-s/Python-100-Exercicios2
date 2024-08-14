import pygame
print('*Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.*')

pygame.mixer.init()

pygame.mixer.music.load("./audio.wav")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    continue