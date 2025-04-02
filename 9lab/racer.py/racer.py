import pygame, sys
from pygame.locals import *
import random, time

# Инициализация
pygame.init()

# фпс
FPS = 60
FramePerSec = pygame.time.Clock()

# тустердын ргб коды
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400  # Экранные ены
SCREEN_HEIGHT = 600  # Экраннын биыктыгы
SPEED = 3  # жылдамдык
SCORE = 0  # упай сасны
COINS = 0  # монета саны

# Шрифттер
font = pygame.font.SysFont("Verdana", 20)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("zhol.png")  # Фон суреты

# ак экран жасау
screen = pygame.display.set_mode((400, 600))  # размер экран
screen.fill(WHITE)  # ак тусты экран
pygame.display.set_caption("Racer")  # игранын аты

# карсы машина класы
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("redcar.png")  # карсы машина суреты
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # карсылас колыкты экран жогаргы жагынан кездейсок шыгару

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)  # карсы машина жылдамдыгы
        if (self.rect.top > 600):
            SCORE += 1  # ар карсы машина откен сайын упай косу
            self.rect.top = 0  # карсы машинаны жогары болыкке шыгару
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # кездейсок орынга орналастыру

# Монета (Coin) класы
c1, c2, c3, c4, c5 = False, False, False, False, False  # Монеталар ушын шарттар

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")  # Монетаның суреты
        self.image = pygame.transform.scale(self.image, (40, 40))  # Монета размеры
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_HEIGHT - 40))  # Монетаны кездейсок орынга орналастыру

    def move(self):
        global COINS
        global SPEED
        if self.rect.bottom < SCREEN_HEIGHT // 3:
            COINS += 3  # Монетаны жогары болыктен жинаганда берылетын упай
        elif self.rect.bottom < SCREEN_HEIGHT // 1.5:
            COINS += 2  # Монетаны ортангы болыктен жинаганда берылетын упай
        else:
            COINS += 1  # Төменгы болыктен монета жинаган кезде монетанын кобейуы
        global c1, c2, c3, c4, c5
        if not c1 and COINS >= 10:
            SPEED += 1  # Жылдамдыкты арттыру
            c1 = True
        if not c2 and COINS >= 20:
            SPEED += 1  # Жылдамдыкты арттыру
            c2 = True
        if not c3 and COINS >= 30:
            SPEED += 1  # Жылдамдыкты арттыру
            c3 = True
        if not c4 and COINS >= 40:
            SPEED += 1  # Жылдамдыкты арттыру
            c4 = True
        if not c5 and COINS >= 50:
            SPEED += 1  # Жылдамдык арттыру
            c5 = True
        self.rect.top = random.randint(40, SCREEN_WIDTH - 40)  # Монетаны кездейсок орнату
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_HEIGHT - 40))  # Монетаны кайта орналастыру

# Ойыншы класы
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")  # Ойыншы машинанын суреты
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)  # Ойыншынын алгашкы орны

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:  # Солга бурылу
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:  # Онға бурылу
                self.rect.move_ip(5, 0)
        if self.rect.top > 0:
            if pressed_keys[K_UP]:  # Жогары жылжу
                self.rect.move_ip(0, -5)
        if self.rect.bottom < SCREEN_HEIGHT:
            if pressed_keys[K_DOWN]:  # астына жылжу
                self.rect.move_ip(0, 5)

# Спрайттарды орнату
P1 = Player()  # Ойыншы
E1 = Enemy()  # Қарсылас
C1 = Coin()  # Монета

# Спрайттар тобы
enemies = pygame.sprite.Group()
enemies.add(E1)
coinss = pygame.sprite.Group()
coinss.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# карсы машина косылуы
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)  # скорость арттыру

# Ойыннын аякталу жкраны
def game_over_screen():
    screen.fill(RED)
    screen.blit(game_over, (30, 250))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    return True
                elif event.key == K_ESCAPE:
                    return False

# авария 
def handle_crash():
    time.sleep(2)

background_y = 0  # Фоннын алгашкы орны

# ойыннын циклы
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.1  # Жылдамдык артып отырады
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if pygame.sprite.spritecollideany(P1, enemies):  # машинанын авария болуы
        continue_game = handle_crash()
        if not continue_game:
            pygame.quit()
            sys.exit()

    background_y = (background_y + SPEED) % background.get_height()  # Фон козгалысы
    screen.blit(background, (0, background_y))  # Фонды орнату
    screen.blit(background, (0, background_y - background.get_height()))

    scores = font_small.render(str(SCORE), True, BLACK)  # очко корсету
    screen.blit(scores, (10, 10))

    coins = font_small.render(str(COINS), True, BLACK)  # Монеталарды корсету
    screen.blit(coins, (370, 10))

    # Барлык спрайттарды экранга шыгару
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        if entity == C1:
            if pygame.sprite.spritecollideany(P1, coinss):  # Ойыншы монета жинаса
                entity.move()
        else:
            entity.move()

    for enemy in enemies:  # екыншы машина козга

        enemy.move()

    for coin in coinss:  # Монеталардың қозғалысы
        coin.rect.y += SPEED
        if coin.rect.top > SCREEN_HEIGHT:
            coin.rect.y = -coin.rect.height
            coin.rect.x = random.randint(40, SCREEN_WIDTH - 40)  # Монетаның жаңа орны

    pygame.display.update()  # Экранды жаңарту
    FramePerSec.tick(FPS)  # FPS реттеу
