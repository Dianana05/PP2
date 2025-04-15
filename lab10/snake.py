import pygame
import sys
import random
import time
from task2 import get_or_create_user, update_user_progress

pygame.init()

SW = 800
SH = 800
BLOCK_SIZE = 50

sc = pygame.display.set_mode((SW, SH))
pygame.display.set_caption("SNAKE")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)

username = input("Enter your username: ")
user_id, user_level = get_or_create_user(username)

level = user_level
score = 0
speed = 5 + (level - 1) * 1.5
game_over = False
paused = False

class Snake:
    def __init__(self):
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        self.body = [pygame.Rect(self.x - BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.dead = False

    def update(self):
        global game_over
        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
                self.dead = True

        if self.head.x not in range(0, SW) or self.head.y not in range(0, SH):
            self.dead = True

        if self.dead:
            game_over = True
            return

        self.body.append(self.head)
        for i in range(len(self.body) - 1):
            self.body[i].x, self.body[i].y = self.body[i + 1].x, self.body[i + 1].y
        self.head.x += self.xdir * BLOCK_SIZE
        self.head.y += self.ydir * BLOCK_SIZE
        self.body.remove(self.head)

class Applee:
    def __init__(self):
        self.respawn()

    def respawn(self):
        while True:
            self.x = random.randint(0, SW // BLOCK_SIZE - 1) * BLOCK_SIZE
            self.y = random.randint(0, SH // BLOCK_SIZE - 1) * BLOCK_SIZE
            self.ves = random.choice([1, 3, 5])
            self.color = {1: "yellow", 3: "red", 5: "white"}[self.ves]
            self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
            self.spawn_time = time.time()

            if not any(part.x == self.x and part.y == self.y for part in snake.body) and not (snake.head.x == self.x and snake.head.y == self.y):
                break

    def update(self):
        pygame.draw.rect(sc, self.color, self.rect)
        if time.time() - self.spawn_time > 10:
            self.respawn()

def drawGrid():
    for x in range(0, SW, BLOCK_SIZE):
        for y in range(0, SH, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(sc, (255, 255, 255), rect, 1)

def reset_game():
    global snake, apple, game_over, level, speed, score
    snake = Snake()
    apple = Applee()
    game_over = False
    score = 0
    level = user_level
    speed = 5 + (level - 1) * 1.5

drawGrid()
snake = Snake()
apple = Applee()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if not game_over and not paused:
                if event.key == pygame.K_DOWN:
                    snake.xdir = 0
                    snake.ydir = 1
                elif event.key == pygame.K_UP:
                    snake.xdir = 0
                    snake.ydir = -1
                elif event.key == pygame.K_RIGHT:
                    snake.xdir = 1
                    snake.ydir = 0
                elif event.key == pygame.K_LEFT:
                    snake.ydir = 0
                    snake.xdir = -1

            if event.key == pygame.K_r and game_over:
                reset_game()

            if event.key == pygame.K_p and not game_over:
                paused = not paused
                if paused:
                    update_user_progress(user_id, score, level)

    if not game_over and not paused:
        snake.update()

    sc.fill((0, 0, 0))
    drawGrid()
    apple.update()

    score_rect = font.render("Score: {}".format(score), True, "white")
    sc.blit(score_rect, (10, 10))

    level_rect = font.render("Level: {}".format(level), True, "blue")
    sc.blit(level_rect, (10, 50))

    pygame.draw.rect(sc, "red", snake.head)
    for square in snake.body:
        pygame.draw.rect(sc, "green", square)

    if snake.head.x == apple.x and snake.head.y == apple.y:
        score += apple.ves
        snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))
        apple.respawn()

        if score % 4 == 0:
            level += 1
            speed += 1.5

    if game_over:
        game_over_text = font.render("GAME OVER - Press R to Restart", True, (255, 0, 0))
        sc.blit(game_over_text, (SW // 4, SH // 2))

    pygame.display.update()
    clock.tick(speed)
