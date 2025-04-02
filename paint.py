import pygame

WIDTH, HEIGHT = 1200, 800
FPS = 90

draw = False
radius = 2
color = 'blue'
mode = 'pen'

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Simple Paint')
clock = pygame.time.Clock()
screen.fill(pygame.Color('white'))
font = pygame.font.SysFont(None, 60)

def draw_line(surface, start, end, thickness, col):
    pygame.draw.line(surface, pygame.Color(col), start, end, thickness)

def draw_circle(surface, center, rad, thickness, col):
    pygame.draw.circle(surface, pygame.Color(col), center, rad, thickness)

def draw_rectangle(surface, start, end, thickness, col):
    x1, y1 = start
    x2, y2 = end
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    pygame.draw.rect(surface, pygame.Color(col), (min(x1, x2), min(y1, y2), width, height), thickness)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = 'rectangle'
            elif event.key == pygame.K_c:
                mode = 'circle'
            elif event.key == pygame.K_p:
                mode = 'pen'
            elif event.key == pygame.K_e:
                mode = 'eraser'
            elif event.key == pygame.K_1:
                color = 'black'
            elif event.key == pygame.K_2:
                color = 'green'
            elif event.key == pygame.K_3:
                color = 'red'
            elif event.key == pygame.K_4:
                color = 'blue'
            elif event.key == pygame.K_q:
                screen.fill(pygame.Color('white'))
        elif event.type == pygame.MOUSEBUTTONDOWN:
            draw = True
            prev_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if mode == 'rectangle':
                draw_rectangle(screen, prev_pos, event.pos, radius, color)
            elif mode == 'circle':
                draw_circle(screen, prev_pos, radius, radius, color)
            draw = False
        elif event.type == pygame.MOUSEMOTION:
            if draw and mode == 'pen':
                draw_line(screen, prev_pos, event.pos, radius, color)
            elif draw and mode == 'eraser':
                draw_line(screen, prev_pos, event.pos, radius, 'white')
            prev_pos = event.pos
    
    pygame.draw.rect(screen, pygame.Color('white'), (5, 5, 115, 75))
    text = font.render(str(radius), True, pygame.Color(color))
    screen.blit(text, (5, 5))
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()

