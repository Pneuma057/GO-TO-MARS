
from go_to_mars import pygame
from spacecraft import Spacecraft
from asteroids import Asteroid_big, Asteroid_mid
width = 1100
height = 800

black = (0,0,0)
white = (255,255,255)

screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
fps= 60
time = pygame.time.get_ticks()

player = Spacecraft(black,width,height,)
asteroid_big = Asteroid_big(black,width,height)
asteroid_mid = Asteroid_mid(black,width,height)
all_sprites = pygame.sprite.Group()
all_sprites.add(player,asteroid_big,asteroid_mid)
background = pygame.image.load("planets/level_1.png").convert()

scroll = 0
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("THE QUEST")
list_asteroid_big = pygame.sprite.Group() 
list_asteroid_mid = pygame.sprite.Group()
healt = 3
score = 0
font = pygame.font.SysFont("Arial",30)
#create asteroids random ( by camilo help)
#para aumentar el ritmo encuentanto corre el tiempo, crear un reloj y 
#if tiempo > 1000:
#    cantindad = 
for i in range(18):
    asteroid_big = Asteroid_big(black,width,height)
    list_asteroid_big.add(asteroid_big)
for i in range(50):
    asteroid_mid = Asteroid_mid(black,width,height)
    list_asteroid_mid.add(asteroid_mid)

#main buckles

gaming = True

while gaming:
    if width > -1150:
        time = pygame.time.get_ticks()
        score = font.render("Score Points",(score) ,True,(white))
        screen.blit(score,(20,20))
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gaming = False
       
        #paint background
    counting_time = font.render("Time :"+str(time),0,(120,70,0))
    screen.blit(background,(scroll,0))
    #counting_time.draw(screen)
    #counting_time.update()
    all_sprites.draw(screen)
    list_asteroid_big.draw(screen)
    list_asteroid_big.update()
    list_asteroid_mid.draw(screen)
    list_asteroid_mid.update()
    collides = pygame.sprite.spritecollide(player,list_asteroid_big,True)
    
    if collides:
        gaming = True #change for life damange
    #scroll time
    scroll -= 0.3
    if abs (scroll) > width:
        scroll = 0
    if time == 6000:
        gaming = False
    pygame.display.flip()
    all_sprites.update()
pygame.quit()