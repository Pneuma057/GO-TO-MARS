from lib2to3.refactor import MultiprocessRefactoringTool
import pygame
from asteroids import Asteroid_big,Asteroid_mid
from spacecraft import Spacecraft
from screens import Menu, GameOver,Stage

def get_new_sprites(player):
    list_asteroid_big = pygame.sprite.Group() 
    list_asteroid_mid = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    asteroid_big = Asteroid_big(colors['black'])
    asteroid_mid = Asteroid_mid(colors['black'])
    all_sprites.add(player,asteroid_big,asteroid_mid)

    for i in range(18):
        asteroid_big = Asteroid_big(colors['black'])
        list_asteroid_big.add(asteroid_big)

    for i in range(50):
        asteroid_mid = Asteroid_mid(colors['black'])
        list_asteroid_mid.add(asteroid_mid)
    return all_sprites,list_asteroid_big,list_asteroid_mid

if __name__ == "__main__":
    pygame.init()

    #screen setup
    screen_size = (1400,800)#0,1
    colors = {"white" :(255,255,255), "black":(0,0,0)}#0,1
    fps = 60
    screen = pygame.display.set_mode((screen_size[0],screen_size[1]))
    clock = pygame.time.Clock()
    time = pygame.time.get_ticks()

    #sprites setup
    player = Spacecraft(colors['black'], screen_size,)
    
    #inits
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Exist")

    while True:
        score = 0
        health = 3
        Menu(screen, clock).run() #sound pero no lo coje
        all_sprites,list_asteroid_big,list_asteroid_mid = get_new_sprites(player)
        score,health = Stage(screen, clock,colors,fps,all_sprites,list_asteroid_big,list_asteroid_mid,player,health,score,"planets/moon.png","the moon").run()
       
        #  pass to next screen if you didn't die
        if health :
            all_sprites,list_asteroid_big,list_asteroid_mid = get_new_sprites(player)
            score,health = Stage(screen, clock,colors,fps,all_sprites,list_asteroid_big,list_asteroid_mid,player,health,score,"planets/mars.png","to mars").run()
        GameOver(screen, clock, score).run()


    pygame.quit()