import pygame
import time

pygame.init()

WIDTH, HEIGHT = 950, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Часы")

fon = pygame.transform.scale(pygame.image.load("7lab/fonsagat.png"), (WIDTH, HEIGHT))
minute_image = pygame.image.load("7lab/minute.png")
second_image = pygame.image.load("7lab/secund.png")

CENTER = (WIDTH // 2, HEIGHT // 2)

def rotate(image, angle, center):
    rotated = pygame.transform.rotate(image, angle)
    return rotated, rotated.get_rect(center=center)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = time.localtime()
    second_angle = -current_time.tm_sec * 6
    minute_angle = -current_time.tm_min * 6

    screen.blit(fon, (0, 0)) 

    rotated_minute, minute_rect = rotate(minute_image, minute_angle, CENTER)
    rotated_second, second_rect = rotate(second_image, second_angle, CENTER)

    screen.blit(rotated_minute, minute_rect.topleft)
    screen.blit(rotated_second, second_rect.topleft)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
