import pygame, sys, random, time, copy
pygame.init()

# Параметры экрана 
SCREEN_SIZE = 500
SCALE = 15
FPS = 60
SPEED = 10
score, level = 0, 0
food_x, food_y = 10, 10

# Настройка тус
COLORS = {
    "background_top": (0, 0, 50),
    "background_bottom": (0, 0, 0),
    "snake_body": (255, 137, 0),
    "snake_head": (255, 247, 0),
    "food": (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)),
    "font": (255, 255, 255),
    "game_over": (255, 0, 0)
}

# Инициализация экрана
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Класс змейка
class Snake:
    def __init__(self):
        self.x, self.y = SCREEN_SIZE // 2, SCREEN_SIZE // 2
        self.direction = [SCALE, 0]
        self.body = [[self.x, self.y]]
        self.length = 1

    def move(self):
        self.body.insert(0, [self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1]])
        self.body = self.body[:self.length]

    def grow(self):
        self.length += 1

    def check_collision(self):
        return any(self.body[0] == segment for segment in self.body[1:])

    def render(self):
        for index, segment in enumerate(self.body):
            color = COLORS["snake_head"] if index == 0 else COLORS["snake_body"]
            pygame.draw.rect(screen, color, (*segment, SCALE, SCALE))

# Класс пойнт
class Food:
    def __init__(self):
        self.new_position()

    def new_position(self):
        global food_x, food_y
        food_x, food_y = random.randint(1, SCREEN_SIZE // SCALE - 1) * SCALE, random.randint(1, SCREEN_SIZE // SCALE - 1) * SCALE

    def render(self):
        pygame.draw.rect(screen, COLORS["food"], (food_x, food_y, SCALE, SCALE))

# Функции отображения
def render_gradient_background():
    for y in range(SCREEN_SIZE):
        color = tuple(COLORS["background_top"][i] + (COLORS["background_bottom"][i] - COLORS["background_top"][i]) * y // SCREEN_SIZE for i in range(3))
        pygame.draw.line(screen, color, (0, y), (SCREEN_SIZE, y))

def render_text(text, position, size, color):
    font = pygame.font.SysFont(None, size)
    screen.blit(font.render(text, True, color), position)

# Основной игровой цикл
def game_loop():
    global score, level, SPEED

    snake = Snake()
    food = Food()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != [0, SCALE]:
                    snake.direction = [0, -SCALE]
                elif event.key == pygame.K_DOWN and snake.direction != [0, -SCALE]:
                    snake.direction = [0, SCALE]
                elif event.key == pygame.K_LEFT and snake.direction != [SCALE, 0]:
                    snake.direction = [-SCALE, 0]
                elif event.key == pygame.K_RIGHT and snake.direction != [-SCALE, 0]:
                    snake.direction = [SCALE, 0]

        render_gradient_background()
        snake.move()
        snake.render()
        food.render()
        render_text(f"Score: {score}", (SCALE, SCALE), 20, COLORS["font"])
        render_text(f"Level: {level}", (SCALE * 7, SCALE), 20, COLORS["font"])

        if abs(snake.body[0][0] - food_x) < SCALE and abs(snake.body[0][1] - food_y) < SCALE:
            food.new_position()
            snake.grow()
            score += random.randint(1, 5)
            if score % 10 == 0:
                level += 1
                SPEED += 1

        if snake.check_collision() or any(coord < 0 or coord >= SCREEN_SIZE for coord in snake.body[0]):
            render_text("Game Over!", (SCREEN_SIZE // 4, SCREEN_SIZE // 3), 50, COLORS["game_over"])
            pygame.display.update()
            time.sleep(3)
            return

        pygame.display.update()
        clock.tick(SPEED)

# Запуск игры
game_loop()
