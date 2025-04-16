import pygame  # Pygame кітапханасын импорттаймыз
import time  # Уақытпен жұмыс істеу үшін time модулін қосамыз

# Pygame-ті инициализациялау
pygame.init()

# Экран өлшемдерін анықтау
WIDTH, HEIGHT = 950, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Ойын терезесін жасау
pygame.display.set_caption("Часы")  # Терезеге атау беру

# Фон және сағат тілі суреттерін жүктеу
fon = pygame.transform.scale(pygame.image.load("7lab/fonsagat.png"), (WIDTH, HEIGHT))  # Фонды масштабтау
minute_image = pygame.image.load("7lab/minute.png")  # Минут тілін жүктеу
second_image = pygame.image.load("7lab/secund.png")  # Секунд тілін жүктеу

# Сағаттың орталық нүктесі
CENTER = (WIDTH // 2, HEIGHT // 2)

# Кескінді бұру функциясы
def rotate(image, angle, center):
    rotated = pygame.transform.rotate(image, angle)  # Кескінді бұру
    return rotated, rotated.get_rect(center=center)  # Жаңа айналған кескін мен оның координаталарын қайтару

clock = pygame.time.Clock()  # Pygame сағат объектісін жасау
running = True  # Ойын циклінің жұмысын басқару үшін айнымалы

# Ойын циклі
while running:
    for event in pygame.event.get():  # Барлық оқиғаларды өңдеу
        if event.type == pygame.QUIT:  # Егер "жабу" батырмасы басылса
            running = False  # Циклды тоқтату

    # Ағымдағы уақытты алу
    current_time = time.localtime()
    second_angle = -current_time.tm_sec * 15  #унд тілі 6 градусқа өзгереді әр секунд сайын
    minute_angle = -current_time.tm_min * 6# Минут тілі 6 градусқа өзгереді әр минут сайын

    screen.blit(fon, (0, 0))  # Фон суретін экранға шығару

    # Минут және секунд тіліне бұруды қолдану
    rotated_minute, minute_rect = rotate(minute_image, minute_angle, CENTER)
    rotated_second, second_rect = rotate(second_image, second_angle, CENTER)

    # Айналған сағат тілі суреттерін экранға шығару
    screen.blit(rotated_minute, minute_rect.topleft)
    screen.blit(rotated_second, second_rect.topleft)

    pygame.display.flip()  # Экранды жаңарту
    clock.tick(30)  # Кадр жылдамдығын 30 FPS етіп орнату

pygame.quit()  # Pygame-ті жабу