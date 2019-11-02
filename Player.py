import pygame, random

pygame.init()
pygame.display.set_mode((500, 500))
time = pygame.Clock()

run = True
while run:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            run = False

    keys = pygame.key.get_pressed()
    if(keys[pygame.K_ESCAPE]):
        run = False
pygame.quit()
