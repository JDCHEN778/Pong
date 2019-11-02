import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Pong: The Game")
timer = pygame.time.Clock()

back = pygame.Surface((500,500))
background = back.convert()
background.fill((0,0,0))




run = True
while run:


    fps = timer.tick(30)
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            run = False

    keys = pygame.key.get_pressed()
    if(keys[pygame.K_ESCAPE]):
        run = False





pygame.quit()
