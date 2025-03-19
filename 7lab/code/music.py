import pygame
import os

pygame.init()

# музыкага жол
music_folder = r"C:/Users/uzakb/Desktop/PP2_all_labs/7lab/music"
allmusic = os.listdir(music_folder)

playlist = [os.path.join(music_folder, song) for song in allmusic if song.endswith(".mp3")]

if not playlist:
    raise FileNotFoundError("error , add m3 fail")

# Экран 
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Lana Del Rey")
clock = pygame.time.Clock()

# Фон сурет
background = pygame.image.load(os.path.join(music_folder, "background.png") ,)

# Кнопка
playb = pygame.image.load(os.path.join(music_folder, "play.png"))
pausb = pygame.image.load(os.path.join(music_folder, "pause.png"))
nextb = pygame.image.load(os.path.join(music_folder, "next.png"))
prevb = pygame.image.load(os.path.join(music_folder, "back.png"))

# музыка косылуы
index = 0
aplay = False
pygame.mixer.music.load(playlist[index])
pygame.mixer.music.play()
aplay = True

# Кнопкалардың координатасы (x, y, width, height)
play_rect = pygame.Rect(370, 590, 70, 70)
next_rect = pygame.Rect(460, 587, 70, 70)
prev_rect = pygame.Rect(273, 585, 75, 75)

# Ойын цикл
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()
        
        elif event.type == pygame.KEYDOWN:  # Пернетақтадан басу
            if event.key == pygame.K_SPACE:  # Тоқтату/Ойнату
                if aplay:
                    aplay = False
                    pygame.mixer.music.pause()
                else:
                    aplay = True
                    pygame.mixer.music.unpause()
            if event.key == pygame.K_RIGHT:  # келесы музыка
                index = (index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
            if event.key == pygame.K_LEFT:  # ⏮ Алдыңғы музыкасы
                index = (index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
        
        elif event.type == pygame.MOUSEBUTTONDOWN:  # мышкамен баскару
            if play_rect.collidepoint(event.pos):  # Play/Pause кнопка
                if aplay:
                    aplay = False
                    pygame.mixer.music.pause()
                else:
                    aplay = True
                    pygame.mixer.music.unpause()
            if next_rect.collidepoint(event.pos):  #  Next кнопкасы
                index = (index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
            if prev_rect.collidepoint(event.pos):  #  Previous кнопкасы
                index = (index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()

    # Музыка атын шығару
    font2 = pygame.font.SysFont(None, 20)
    text2 = font2.render(os.path.basename(playlist[index]), True, (150, 20, 50))

    # Экранды жанарту
    screen.blit(background, (268, 300))
    screen.blit(text2, (268, 520))
    screen.blit(pygame.transform.scale(playb if not aplay else pausb, (70, 70)), (370, 590))
    screen.blit(pygame.transform.scale(nextb, (70, 70)), (460, 587))
    screen.blit(pygame.transform.scale(prevb, (75, 75)), (273, 585))

    pygame.display.update()
    clock.tick(24)
