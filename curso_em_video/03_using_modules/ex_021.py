# Write a Python program that opens and plays audio from an MP3 file.
import pygame

pygame.init()
pygame.mixer.music.load("ex_021_playing_audio.mp3")
pygame.event.wait()
