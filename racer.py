import pygame, sys, random, time
from pygame.locals import *

# Инициализация Pygame
pygame.init()

# Параметры экрана
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 600
FPS = 60
SPEED = 3
SCORE, COINS = 0, 0

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Шрифты
font = pygame.font.SysFont("Verdana", 20)
game_over_text = font.render("Game Over", True, BLACK)

# Экран и фон
background = pygame.image.load("zhol.png")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer")

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect(center=(160, 520))
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
        if keys[K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(5, 0)
        if keys[K_UP] and self.rect.top > 0:
            self.rect.move_ip(0, -5)
        if keys[K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.move_ip(0, 5)

# Класс врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("redcar.png")
        self.rect = self.image.get_rect(center=(random.randint(40, SCREEN_WIDTH - 40), 0))
    
    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Класс монет
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(center=(random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_HEIGHT - 40)))
    
    def reset_position(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_HEIGHT - 40))

    def move(self):
        pass  # Coin қозғалмайды, бірақ move() бар

# Создание объектов
player = Player()
enemy = Enemy()
coin = Coin()

# Группы спрайтов
enemies = pygame.sprite.Group(enemy)
coins = pygame.sprite.Group(coin)
all_sprites = pygame.sprite.Group(player, enemy, coin)

# Основной цикл игры
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    # Проверка столкновений с врагом
    if pygame.sprite.spritecollideany(player, enemies):
        screen.fill(RED)
        screen.blit(game_over_text, (130, 250))
        pygame.display.update()
        time.sleep(2)
        running = False
    
    # Проверка сбора монеты
    if pygame.sprite.spritecollideany(player, coins):
        COINS += random.randint(1, 3)
        coin.reset_position()
        if COINS % 10 == 0:
            SPEED += 1
    
    # Прокрутка фона
    screen.blit(background, (0, 0))
    
    # Отображение очков
    screen.blit(font.render(f"Score: {SCORE}", True, BLACK), (10, 10))
    screen.blit(font.render(f"Coins: {COINS}", True, BLACK), (SCREEN_WIDTH - 100, 10))
    
    for sprite in all_sprites:
        if isinstance(sprite, (Player, Enemy)):  # Тек Player и Enemy қозғалсын
            sprite.move()
        screen.blit(sprite.image, sprite.rect)
    
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
