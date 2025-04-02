import pygame  
import sys  # системамен байланысуы
import copy  
import random 
import time  

pygame.init()  

# Ойыннын настройкасы
scale = 15 
score = 0  
level = 0  
SPEED = 10  
food_x = 10  # доптын кординатасы
food_y = 10  

# Ойын экраны
display = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake Game")  
clock = pygame.time.Clock()  # Ойын уакытын баскару ушын

# тустерды орнату ргб 
background_top = (0, 0, 50)  # Фон жогары болыгы
background_bottom = (0, 0, 0)  
snake_colour = (255, 137, 0)  
food_colour = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))  # Тағамның түсі (кездейсоқ)
snake_head = (255, 247, 0)  
font_colour = (255, 255, 255)  
defeat_colour = (255, 0, 0)  

# Змейка класы
class Snake:
    def __init__(self, x_start, y_start):
        self.x = x_start  # Змейканың бастапкы x координатасы
        self.y = y_start  # Змейканың бастапкы y координатасы
        self.w = 15  # Змейканың ены
        self.h = 15  # Змейканың биыктыгы
        self.x_dir = 1  
        self.y_dir = 0  # жогары томен козгалыс багыты
        self.history = [[self.x, self.y]]  
        self.length = 1  # Змейканың узындыгы

    # Змейка бастапкы калыпка келтыру класы
    def reset(self):
        self.x = 500 / 2 - scale  # Змейканы экраннын ортасына орналастыру
        self.y = 500 / 2 - scale  
        self.w = 15  # Ены
        self.h = 15  
        self.x_dir = 1 
        self.y_dir = 0  
        self.history = [[self.x, self.y]]  # змейка туралы отчет кайта калыпына келтыру
        self.length = 1 

    # Змейканы экрнага шыгару
    def show(self):
        for i in range(self.length):
            if not i == 0:
                pygame.draw.rect(display, snake_colour, (self.history[i][0], self.history[i][1], self.w, self.h))
            else:
                pygame.draw.rect(display, snake_head, (self.history[i][0], self.history[i][1], self.w, self.h))

    # Змейканын допты жегенын тексеру
    def check_eaten(self):
        if abs(self.history[0][0] - food_x) < scale and abs(self.history[0][1] - food_y) < scale:
            return True

    # новый уровеньга откенын ттексеру
    def check_level(self):
        global level
        if self.length % 5 == 0:
            return True

    # змейка узындыгы
    def grow(self):
        self.length += 1
        self.history.append(self.history[self.length - 2])

    # оз озыне соктыгысысн тексеру
    def death(self):
        i = self.length - 1
        while i > 0:
            if abs(self.history[0][0] - self.history[i][0]) < self.w and abs(self.history[0][1] - self.history[i][1]) < self.h and self.length > 2:
                return True
            i -= 1

    # Змейканы кординатасын жанарту
    def update(self):
        i = self.length - 1
        while i > 0:
            self.history[i] = copy.deepcopy(self.history[i - 1])
            i -= 1
        self.history[0][0] += self.x_dir * scale
        self.history[0][1] += self.y_dir * scale

# тамактын клсасы
class Food:
    # Тамактын орнын аныктау
    def new_location(self):
        global food_x, food_y
        food_x = random.randrange(1, int(500 / scale) - 1) * scale
        food_y = random.randrange(1, int(500 / scale) - 1) * scale

    # тамакты экранга шыгару
    def show(self):
        pygame.draw.rect(display, food_colour, (food_x, food_y, scale, scale))

# Ойыншы упайын корсету функциясы
def show_score():
    font = pygame.font.SysFont(None, 20)
    text = font.render("Score: " + str(score), True, font_colour)
    display.blit(text, (scale, scale))

# игранын уровеньын корсету
def show_level():
    font = pygame.font.SysFont(None, 20)
    text = font.render("Level: " + str(level), True, font_colour)
    display.blit(text, (90 - scale, scale))

# игранын циклы
def gameLoop():
    global score
    global level
    global SPEED

    snake = Snake(500 / 2, 500 / 2)  # змейка обьектысы
    food = Food()  # Тамак обьекты
    food.new_location()  # Тамактын бастапкы орны

    while True:  # Ойыннын негызгы циклы
        for event in pygame.event.get():  # Оқиғаларды өңде
            if event.type == pygame.QUIT:  # егер терезены жапса
                pygame.quit()  # Pygameды токтату
                sys.exit()  # аяктау 
            if event.type == pygame.KEYDOWN:  # кнопка басу
                if event.key == pygame.K_q:  # Егер Q басылса
                    pygame.quit()  # Pygame токтату
                    sys.exit()  # Бағдарламаны аяктау
                if snake.y_dir == 0:  # Егер змейка колдене козгалса
                    if event.key == pygame.K_UP:  # Егер Жогары кнопка
                        snake.x_dir = 0  
                        snake.y_dir = -1  # y жогары
                    if event.key == pygame.K_DOWN:  # Егер томенгы кнопка басылсса
                        snake.x_dir = 0  # x токтау
                        snake.y_dir = 1  # y томенге

                if snake.x_dir == 0:  # Егер змейка тік бағытта қозғалса
                    if event.key == pygame.K_LEFT:  # Егер Солға пернесі басылса
                        snake.x_dir = -1  # x бойынша қозғалысты солға бағыттаймыз
                        snake.y_dir = 0  # y бойынша қозғалысты тоқтатамыз
                    if event.key == pygame.K_RIGHT:  # Егер Оңға пернесі басылса
                        snake.x_dir = 1  # x бойынша қозғалысты оңға бағыттаймыз
                        snake.y_dir = 0  # y бойынша қозғалысты тоқтатамыз

        # Экранның фонын градиентпен бояу
        for y in range(500):
            color = (
                background_top[0] + (background_bottom[0] - background_top[0]) * y / 500,
                background_top[1] + (background_bottom[1] - background_top[1]) * y / 500,
                background_top[2] + (background_bottom[2] - background_top[2]) * y / 500
            )
            pygame.draw.line(display, color, (0, y), (500, y))

        snake.show()  # Змейканы корсету
        snake.update()  # Змейканын орнын ауыстыру
        food.show()  # Тагамды экранга шыгру
        show_score()  
        show_level()  

        if snake.check_eaten():  # Егер тамак жесе
            food.new_location() 
            score += random.randint(1, 5)  # упайды рандомно улгайту
            snake.grow()  # Змейканы улгайту

        if snake.check_level():  # егер жана денгейге жетсе
            food.new_location()  # Тагамнын жана орны
            level += 1  # левел арттыру
            SPEED += 1  # Жылдамдык арттыру
            snake.grow()  # Змейканы улгайту

        if snake.death():  # егер согтыгысп калсаа
            score = 0  # 
            level = 0  # басынан басту
            font = pygame.font.SysFont(None, 100)  # Шрифт орнату
            text = font.render("Game Over!", True, defeat_colour) 
            display.blit(text, (50, 200))  # Мәтынды экрнага шыгру
            pygame.display.update()  # Экранды жанарту
            time.sleep(3) # 3 секунд куту
            snake.reset()  # Змейканы калпына келтыру

        if snake.history[0][0] > 500: 
            snake.history[0][0] = 0  

        if snake.history[0][0] < 0:  # Егер змейка сол жак шекарадан асып кетсе он жак шекарага жыберу
            snake.history[0][0] = 500  
            
        if snake.history[0][1] > 500:  # Егер змейка томенгы шекарадн асып кетсе
            snake.history[0][1] = 0  # Змейканы жогаргы шекарага кошыру
        if snake.history[0][1] < 0:  # Егер змейка жогаргы шекарадан асып кетсе томенгы шекарага жыберу
            snake.history[0][1] = 500  # томенгы шекарага кошыру змейканы

        pygame.display.update()  # Экранды жанарту
        clock.tick(SPEED)  # Ойын жылдамдыгы

gameLoop()  # Ойыннын манызды циклын косу
