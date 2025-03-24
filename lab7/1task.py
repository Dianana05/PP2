import pygame
import time

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("Mickey Clock")

background = pygame.image.load("images/clock.png")
minute_hand = pygame.image.load("images/min_hand.png")
second_hand = pygame.image.load("images/sec_hand.png")

center = (400, 300)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = time.localtime()
    minute_angle = -now.tm_min * 6
    second_angle = -now.tm_sec * 6

    screen.blit(background, (0, 0))

    min_rotated = pygame.transform.rotate(minute_hand, minute_angle)
    sec_rotated = pygame.transform.rotate(second_hand, second_angle)

    screen.blit(min_rotated, min_rotated.get_rect(center=center).topleft)
    screen.blit(sec_rotated, sec_rotated.get_rect(center=center).topleft)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
