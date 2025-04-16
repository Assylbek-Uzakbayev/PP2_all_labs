import pygame 
import sys 
import random 
import psycopg2 

pygame.init() 

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 

BLACK = (0, 0, 0) 
WHITE = (255, 255, 255) 
GREEN = (0, 255, 0) 
RED = (255, 0, 0) 

snake_position = [[100, 50], [90, 50], [80, 50]] 
snake_velocity = [10, 0] 
food_item = {'pos': [0, 0], 'weight': 1, 'spawn_time': 0} 
food_is_spawned = True 
current_score = 0 
game_level = 1 
velocity_increase_rate = 0.1 
food_counter = 0   

fps_clock = pygame.time.Clock() 
game_paused = False

def initialize_database():
    try:
        conn = psycopg2.connect(dbname='mydb', user='postgres', password='uzakbaev2006', host='localhost', port='5432')
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS snake_game_scores (
                id SERIAL PRIMARY KEY,
                player_name VARCHAR(100),
                score INT,
                level INT
            );
        """)
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error while connecting: {e}")
        sys.exit()

def save_score_to_db(name, score, level): 
    try:
        conn = psycopg2.connect(dbname='mydb', user='postgres', password='uzakbaev2006', host='localhost', port='5432') 
        cursor = conn.cursor() 
        insert_query = "INSERT INTO snake_game_scores (player_name, score, level) VALUES (%s, %s, %s)" 
        cursor.execute(insert_query, (name, score, level)) 
        conn.commit() 
        cursor.close() 
        conn.close() 
    except Exception as e:
        print(f"Error during saving score: {e}")
        sys.exit()

def retrieve_scores(name): 
    try:
        conn = psycopg2.connect(dbname='mydb', user='postgres', password='uzakbaev2006', host='localhost', port='5432') 
        cursor = conn.cursor() 
        query = "SELECT score, level FROM snake_game_scores WHERE player_name = %s ORDER BY score DESC" 
        cursor.execute(query, (name,)) 
        results = cursor.fetchall() 
        cursor.close() 
        conn.close() 
        return results 
    except Exception as e:
        print(f"Error: {e}")
        sys.exit()

player_name = input("Enter your name: ") 
player_name = player_name.encode('utf-8', 'ignore').decode('utf-8') 
scores = retrieve_scores(player_name) 
if scores: 
    print("Your previous scores:") 
    for score, level in scores: 
        print(f"Score: {score}, Level: {level}") 
    sys.exit()   

def check_for_collision(pos): 
    if pos[0] < 0 or pos[0] > SCREEN_WIDTH - 10 or pos[1] < 0 or pos[1] > SCREEN_HEIGHT - 10: 
        return True 
    if pos in snake_position[1:]: 
        return True 
    return False 

def spawn_food(): 
    global food_counter 
    while True: 
        pos = [random.randrange(1, (SCREEN_WIDTH // 10)) * 10, random.randrange(1, (SCREEN_HEIGHT // 10)) * 10] 
        if pos not in snake_position: 
            weight = 2 if food_counter >= 2 else 1 
            food_counter = 0 if weight == 2 else food_counter + 1 
            return {'pos': pos, 'weight': weight, 'spawn_time': pygame.time.get_ticks()} 

initialize_database()  

try: 
    while True: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit() 
                sys.exit() 
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_UP and snake_velocity[1] == 0: 
                    snake_velocity = [0, -10] 
                elif event.key == pygame.K_DOWN and snake_velocity[1] == 0: 
                    snake_velocity = [0, 10] 
                elif event.key == pygame.K_LEFT and snake_velocity[0] == 0: 
                    snake_velocity = [-10, 0] 
                elif event.key == pygame.K_RIGHT and snake_velocity[0] == 0: 
                    snake_velocity = [10, 0] 
                elif event.key == pygame.K_p: 
                    game_paused = not game_paused 

        if not game_paused: 
            snake_position.insert(0, list(map(lambda x, y: x + y, snake_position[0], snake_velocity))) 

            if check_for_collision(snake_position[0]): 
                save_score_to_db(player_name, current_score, game_level) 
                pygame.quit() 
                sys.exit() 

            if snake_position[0] == food_item['pos']: 
                current_score += food_item['weight'] 
                if current_score % 3 == 0: 
                    game_level += 1 
                    fps_clock.tick(10 + game_level * velocity_increase_rate) 
                food_is_spawned = True 
            else: 
                snake_position.pop() 

            if food_is_spawned: 
                food_item = spawn_food() 
                food_is_spawned = False 

            current_time = pygame.time.get_ticks() 
            if current_time - food_item['spawn_time'] > 10000: 
                food_is_spawned = True 

        screen.fill(BLACK) 
        for pos in snake_position: 
            pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10)) 

        food_color = RED if food_item['weight'] == 1 else (255, 165, 0) 
        pygame.draw.rect(screen, food_color,
                         pygame.Rect(food_item['pos'][0], food_item['pos'][1], 10, 10)) 

        font = pygame.font.SysFont('arial', 20) 
        score_text = font.render(f"Score: {current_score} Level: {game_level}", True, WHITE) 
        screen.blit(score_text, [0, 0]) 

        if game_paused: 
            pause_text = font.render("Paused", True, WHITE) 
            screen.blit(pause_text, [SCREEN_WIDTH // 2 - 30, SCREEN_HEIGHT // 2]) 

        pygame.display.flip() 
        fps_clock.tick(10 + game_level * velocity_increase_rate) 

except SystemExit: 
    pygame.quit()
