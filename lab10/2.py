import pygame
import psycopg2
import ast
import random
import sys

# Настройки базы данных
DB_CONFIG = {
    'user': 'postgres',
    'password': '12345678',
    'host': 'localhost',
    'port': '5432',
    'database': 'postgres'
}

def connect_db():
    return psycopg2.connect(**DB_CONFIG)

def create_tables():
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    username TEXT UNIQUE NOT NULL
                );
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS user_score (
                    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
                    level INTEGER DEFAULT 1,
                    score INTEGER DEFAULT 0,
                    pos TEXT,
                    direction TEXT,
                    walls TEXT,
                    PRIMARY KEY (user_id)
                );
            """)
            conn.commit()

def get_or_create_user(username):
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id FROM users WHERE username=%s", (username,))
            result = cur.fetchone()
            if result:
                return result[0]
            else:
                cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
                conn.commit()
                return cur.fetchone()[0]

def get_user_state(user_id):
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT level, score, pos, direction, walls FROM user_score WHERE user_id=%s", (user_id,))
            result = cur.fetchone()
            if result:
                level, score, pos, direction, walls = result
                if pos is None or direction is None or walls is None:
                    return None
                return {
                    'level': level,
                    'score': score,
                    'pos': ast.literal_eval(pos),
                    'direction': direction,
                    'walls': ast.literal_eval(walls)
                }
            return None
def save_user_state(user_id, level, score, pos, direction, walls):
    with connect_db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO user_score (user_id, level, score, pos, direction, walls)
                VALUES (%s, %s, %s, %s, %s, %s)
                ON CONFLICT (user_id)
                DO UPDATE SET
                    level = EXCLUDED.level,
                    score = EXCLUDED.score,
                    pos = EXCLUDED.pos,
                    direction = EXCLUDED.direction,
                    walls = EXCLUDED.walls
            """, (user_id, level, score, str(pos), direction, str(walls)))
            conn.commit()


CELL_SIZE = 20
WIDTH, HEIGHT = 600, 400
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)

LEVELS = {
    1: {'speed': 10, 'walls': []},
    2: {'speed': 15, 'walls': [(10, i) for i in range(5, 15)]},
    3: {'speed': 20, 'walls': [(x, 10) for x in range(5, 15)]},
    4: {'speed': 25, 'walls': [(10, y) for y in range(5,15)]}
}

def random_food(snake, walls):
    while True:
        pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        if pos not in snake and pos not in walls:
            return pos

def draw(screen, snake, food, walls, score):
    screen.fill(BLACK)
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*[x * CELL_SIZE for x in segment], CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED, (*[x * CELL_SIZE for x in food], CELL_SIZE, CELL_SIZE))
    for wall in walls:
        pygame.draw.rect(screen, GRAY, (*[x * CELL_SIZE for x in wall], CELL_SIZE, CELL_SIZE))

    font = pygame.font.SysFont(None, 24)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))
    pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

# DB: creating tables and user login
    create_tables()
    username = input("Введите имя пользователя: ")
    user_id = get_or_create_user(username)
    state = get_user_state(user_id)

    if state:
        choice = input(f"Добро пожаловать, {username}! Найдено сохранение. Ввести 'c' для продолжения или 'n' для новой игры: ").lower()
        if choice == 'c':
            print(f"Продолжение с уровня {state['level']}")
            level = state['level']
            score = state['score']
            snake = state['pos']
            direction = state['direction']
            walls = state['walls']
        else:
            print("Начинаем новую игру!")
            level = 1
            score = 0
            snake = [(5, 5)]
            direction = 'RIGHT'
            walls = LEVELS[level]['walls']

            save_user_state(user_id, level, score, snake, direction, walls)
    else:
        print(f"Новый пользователь {username}. Игра начинается!")
        level = 1
        score = 0
        snake = [(5, 5)]
        direction = 'RIGHT'
        walls = LEVELS[level]['walls']

    dxdy = {'UP': (0, -1), 'DOWN': (0, 1), 'LEFT': (-1, 0), 'RIGHT': (1, 0)}
    food = random_food(snake, walls)
    paused = False

    while True:
        clock.tick(LEVELS[level]['speed'])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_user_state(user_id, level, score, snake, direction, walls)
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    save_user_state(user_id, level, score, snake, direction, walls)
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_p:
                    paused = not paused
                    if paused:
                        print("Пауза. Прогресс сохранен.")
                        save_user_state(user_id, level, score, snake, direction, walls)
                elif event.key == pygame.K_UP and direction != 'DOWN':
                    direction = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    direction = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    direction = 'RIGHT'

        if paused:
            continue


        dx, dy = dxdy[direction]
        new_head = (snake[0][0] + dx, snake[0][1] + dy)

        if (new_head in snake or
            new_head[0] < 0 or new_head[0] >= GRID_WIDTH or
            new_head[1] < 0 or new_head[1] >= GRID_HEIGHT or
            new_head in walls):
            print("Игра окончена!")
            save_user_state(user_id, level, score, snake, direction, walls)
            pygame.quit()
            sys.exit()

        snake.insert(0, new_head)

        if new_head == food:
            score += 10
            if score >= level * 50 and level < max(LEVELS.keys()):
                level += 1
                walls = LEVELS[level]['walls']
                print(f"Новый уровень: {level}")
            food = random_food(snake, walls)
        else:
            snake.pop()

        draw(screen, snake, food, walls, score)

main()