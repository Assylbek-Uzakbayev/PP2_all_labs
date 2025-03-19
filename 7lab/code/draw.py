import pygame

BALL_RADIUS = 25
BALL_COLOR = (255, 0, 0)  
BALL_POSITION = [400, 300]  
BALL_SPEED = 21 

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255) 
pygame.init()
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Draw Circle")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        BALL_POSITION[1] = max(BALL_POSITION[1] - BALL_SPEED, BALL_RADIUS)
    if keys[pygame.K_DOWN]:
        BALL_POSITION[1] = min(BALL_POSITION[1] + BALL_SPEED, WINDOW_HEIGHT - BALL_RADIUS)
    if keys[pygame.K_LEFT]:
        BALL_POSITION[0] = max(BALL_POSITION[0] - BALL_SPEED, BALL_RADIUS)
    if keys[pygame.K_RIGHT]:
        BALL_POSITION[0] = min(BALL_POSITION[0] + BALL_SPEED, WINDOW_WIDTH - BALL_RADIUS)

    SCREEN.fill(BACKGROUND_COLOR)
    pygame.draw.circle(SCREEN, BALL_COLOR, BALL_POSITION, BALL_RADIUS)
    pygame.display.flip()

    pygame.time.Clock().tick(24)

pygame.quit()
