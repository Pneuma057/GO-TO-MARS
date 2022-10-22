import pygame
from asteroids import Asteroid_big,Asteroid_mid
from spacecraft import Spacecraft
from screens import Menu, GameOver


pygame.init()

#screen setup

screen_size = (1400,800)#0,1
colors = {"white" :(255,255,255), "black":(0,0,0)}#0,1
fps = 60

screen = pygame.display.set_mode((screen_size[0],screen_size[1]))
clock = pygame.time.Clock()
time = pygame.time.get_ticks()
scroll = 0
font = pygame.font.SysFont("Arial", 30)



#sprites setup
player = Spacecraft(colors['black'], screen_size)
asteroid_big = Asteroid_big(colors['black'])
asteroid_mid = Asteroid_mid(colors['black'])
all_sprites = pygame.sprite.Group()
all_sprites.add(player,asteroid_big,asteroid_mid)
background = pygame.image.load("planets/level_1.png").convert()
list_asteroid_big = pygame.sprite.Group() 
list_asteroid_mid = pygame.sprite.Group()
#TODO set health to whatever we want
health = 1
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
    asteroid_big = Asteroid_big(colors['black'])
    list_asteroid_big.add(asteroid_big)
for i in range(50):
    asteroid_mid = Asteroid_mid(colors['black'])
    list_asteroid_mid.add(asteroid_mid)



#TODO: Uncomment the menu to run
#Menu(screen, clock).run()

#running 
runned_loops = 0
while gaming:

    time = pygame.time.get_ticks()

    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gaming = False



    #paint background
    screen.blit(background,(scroll,0))

    # Score rendering and computing
    score_font = font.render(f"Score Points: {score}", True, colors['white'])
    screen.blit(score_font, (20, 20))
    if runned_loops % 10 == 0:
        score += 100

    counting_time = font.render("Time: "+str(time), 0, (120,70,0))
    screen.blit(counting_time, (800,20))


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
        #gaming = True #change for life damange
        health -= 1
        if health == 0:
            break
    health_font = font.render(f"Health: {health}", True, colors['white'])
    screen.blit(health_font, (400, 20))

    #scroll time
    scroll -= 0.3
    if abs (scroll) > screen_size[1]:
        scroll = 0
    if time == 6000:
        gaming = False
    pygame.display.flip()
    all_sprites.update()

    runned_loops += 1

GameOver(screen, clock, score).run()


pygame.quit()