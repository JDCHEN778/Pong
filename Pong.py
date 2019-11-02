import pygame, random
pygame.init()

screen = pygame.display.set_mode( (640,480),0,32)
pygame.display.set_caption("Pong Game")
pygame.mixer.music.load("pong.mp3") #have to download and save in the same file/directory 
pygame.mixer.music.play(-1) #makes the song run forever until window closed

#Making bars, and ball
back = pygame.Surface( (640,480) )
background = back.convert()
background.fill( (0,0,0) )

bar = pygame.Surface( (10,50) )
bar1 = bar.convert()
bar1.fill( (0,0,255) )
bar2 = bar.convert()
bar2.fill( (255,0,0) )
circleSurface = pygame.Surface( (15,15) )
circleDraw = pygame.draw.circle(circleSurface, (0,255,0), (15//2,15//2), 15//2)
circle = circleSurface.convert()
circle.set_colorkey( (0,0,0) )
player1font = pygame.font.SysFont("comic sans",50)
player2font = pygame.font.SysFont("comic sans",50)



velocity = 7 #speed of bars
x1 = 10 # starting x position of bar1 
x2 = 620 #starting x position of bar2
y1 = 215 # starting y postition of bar1
y2 = 215 # starting y position of bar2
x3 = 320 # starting x position of ball
y3 = 230 # starting y position of ball
turnX = True
turnY = True

velocityx = 3 #speed of ball horizontally
velocityy = 3 #speed of ball verically
score1 = 0
score2 = 0


run = True
while(run):
    pygame.time.delay(10)
    player1text = player1font.render(str(score1), True, (255,255,255))
    player2text = player2font.render(str(score2), True, (255,255,255))
    player1rect = player1text.get_rect()
    player1rect.center = (260, 220)
    player2rect = player2text.get_rect()
    player2rect.center = (380, 220)
    

    

    
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            run = False

    if(x3 == 0):
        run = False
    if(x3 == 640):
        run = False
        
    
     
    if bar1.get_rect().move(x1,y1).collidepoint(x3-10,y3):
        turnX = False
        print("ball hits bar1")        
    if bar2.get_rect().move(x2,y2).collidepoint(x3+15,y3):
        turnX = True
        print("ball hits bar2")
    
    keys = pygame.key.get_pressed()

    if(keys[pygame.K_ESCAPE]):
        run = False
    if(keys[pygame.K_s] and y1 < 480 - velocity - 50):
        y1 += velocity
    if(keys[pygame.K_w] and y1 > velocity):
        y1 -= velocity
    if(keys[pygame.K_DOWN] and y2 < 480 - velocity - 50):
        y2 += velocity
    if(keys[pygame.K_UP] and y2 > velocity):
        y2 -= velocity

    if(turnX == True):
        x3 -= velocityx
        if(x3 <= 0):
            #print("Player 1 loses")
            score2 += 1
            x3 = 320
            y3 = random.randint(220,240)
##        if(x3 <= 10):
##            turnX = False
##    else:        ##    if(turn == False):
    else:
        x3 += velocityx
        if(x3 >= 640):
            #print("Player 2 loses")
            score1 += 1
            x3 = 320
            y3 = random.randint(220,240)
##        if(x3 >= 620):
##            turnX = True

    if(turnY == True):
        y3 -= velocityy
        if(y3 <= 10):
            turnY = False
    else:        ##    if(turn == False):
        y3 += velocityy
        if(y3 >= 460):
            turnY = True


 
    screen.blit(background, (0,0) )
    screen.blit(bar1, (x1,y1) )
    screen.blit(bar2, (x2,y2) )
    screen.blit(circle, (x3,y3) )
    screen.blit(player1text, player1rect)
    screen.blit(player2text, player2rect)
    border = pygame.draw.rect(screen,(255,255,255),(5,5,630,470),2)
    middle = pygame.draw.aaline(screen,(255,255,255),(330,5),(330,475))

    pygame.display.update()
    
pygame.quit()
