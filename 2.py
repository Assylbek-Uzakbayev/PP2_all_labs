
import pygame
def play_music(music_file):
    pygame.mixer.init()
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
play_music('your_music_file.mp3')