
from screens import time,Menu,Level_1,pygame
from main import pygame,screen,colors,fps
from asteroids import Asteroid_big,Asteroid_mid
from spacecraft import Spacecraft

#screen setup
screen = pygame.display.set_mode((screen[0],screen[1]))
clock = pygame.time.Clock()
time = pygame.time.get_ticks()
scroll = 0
font = pygame.font.SysFont("Arial",30)


#sprites setup
player = Spacecraft(colors[1],screen[0],screen[1])
asteroid_big = Asteroid_big(colors[1],screen[0],screen[1])
asteroid_mid = Asteroid_mid(colors[1],screen[0],screen[1])
all_sprites = pygame.sprite.Group()
all_sprites.add(player,asteroid_big,asteroid_mid)
background = pygame.image.load("planets/level_1.png").convert()
list_asteroid_big = pygame.sprite.Group() 
list_asteroid_mid = pygame.sprite.Group()
healt = 3
score = 0
gaming = True


#inits
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("THE QUEST")

#create asteroids random ( by camilo help)
#para aumentar el ritmo encuentanto corre el tiempo, crear un reloj y 
#if tiempo > 1000:
#    cantindad = 
for i in range(18):
    asteroid_big = Asteroid_big(colors[1],screen[0],screen[1])
    list_asteroid_big.add(asteroid_big)
for i in range(50):
    asteroid_mid = Asteroid_mid(colors[1],screen[0],screen[1])
    list_asteroid_mid.add(asteroid_mid)


#running 
while gaming:
    if screen[1] > -1150:
        time = pygame.time.get_ticks()
        score = font.render("Score Points",(score) ,True,(colors[0]))
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


#collides

    if collides:
            gaming = True #change for life damange
    #scroll time
    scroll -= 0.3
    if abs (scroll) > screen[1]:
        scroll = 0
    if time == 6000:
        gaming = False
    pygame.display.flip()
    all_sprites.update()





pygame.quit()