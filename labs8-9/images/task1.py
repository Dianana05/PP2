import pygame, sys
from pygame.locals import *
import random, time
 
pygame.init()
 
FPS = 60
FramePerSec = pygame.time.Clock()
 
# Colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINSCORE = 0 
level = 10
 
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load("AnimatedStreet.png")
 
# SCREEN
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
 
class Enemy(pygame.sprite.Sprite): # enemy class
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0) # set a random position 
 
    def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            # Move the car down and add +1 point if it goes off screen
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520) # player in this position 
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]: 
                self.rect.move_ip(-5, 0) # if pressed left going this positon 
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_RIGHT]:  # if right going this position
                self.rect.move_ip(5, 0)

class COIN(pygame.sprite.Sprite):
    cointype = 's' # coin type
    randomint = 0
    def __init__(self):
        super().__init__()
        self.randomint = random.randint(0, 10) 
        if self.randomint in [0, 1, 2, 3, 4]:
            self.image = pygame.image.load("SmallCoin.png")
            self.cointype = 's'
        elif self.randomint in [5, 6, 7]:
            self.image = pygame.image.load("MediumCoin.png")
            self.cointype = 'm'
        elif self.randomint in [8, 9]:
            self.image = pygame.image.load("BigCoin.png")
            self.cointype = 'b'
        # generate random type of coin and load image
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  # coin position random and start in up
    
    def move(self):
        self.rect.move_ip(0, 3)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    # We move the coin down and move it up if it goes off the screen.
    
    def disapper(self):
        global COINSCORE
        if self.cointype == 's':
            COINSCORE += 1
        elif self.cointype == 'm':
            COINSCORE += 3
        elif self.cointype == 'b':
            COINSCORE += 5
            # type coin, after score in up
        self.rect.top = 0
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = COIN()
 
# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
 
# every second SPEED increase
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
 
# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    coinscores = font_small.render(str(COINSCORE), True, BLACK)
    DISPLAYSURF.blit(coinscores, (SCREEN_WIDTH - 50, 10))
    # отображаем score
    
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
        # move and draw cars

    for coin in coins:
        coin.move()
        DISPLAYSURF.blit(coin.image, coin.rect)
        # draw coin

    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))
        pygame.display.update()
        pygame.quit()
        sys.exit()   
        # If a player crashes into a car, the game ends.
        
    collided_coins = pygame.sprite.spritecollide(P1, coins, True) # check collect coin 
    for coin in collided_coins:
        pygame.mixer.Sound('bell.wav').play()
        coin.disapper()
        coins.add(COIN())
        
        if COINSCORE >= level:
            SPEED += 4
            level += 5
            # Increase the difficulty if enough coins are collected
                      
    pygame.display.update()
    FramePerSec.tick(FPS)