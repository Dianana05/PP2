import pygame

pygame.init()
screen = pygame.display.set_mode((1000,800))
done = False

x = 50
y = 50

RED = (255, 0, 0)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            if y > 30:
                y -= 20
        if pressed[pygame.K_DOWN]:
            if y < (screen.get_height() - 31):
                y += 20
        if pressed[pygame.K_LEFT]:
            if x > 30:
                x -= 20
        if pressed[pygame.K_RIGHT]:
            if x < (screen.get_width() - 31):
                x += 20
        
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, RED, (x, y), 25)
        pygame.display.flip()
        clock.tick(60)