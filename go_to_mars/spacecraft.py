
from go_to_mars import pygame

width = 1400
height = 800
black = (0,0,0)

class Spacecraft(pygame.sprite.Sprite,):
    def __init__(self,black, width,height):
        super().__init__()
        self.image = pygame.image.load("spacecraft/nave_3.png").convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.centerx = 100
        self.rect.centery = height // 2
        self.speed_y = 0

    def update(self):
        self.speed_y = 0
        keystate = pygame.key.get_pressed()
        
        if keystate[pygame.K_w]:
            self.speed_y = -5
            #if keystate[pygame.K_w]>= 
             # self.speed_y = -50
        if keystate[pygame.K_s]:
           self.speed_y = 5
      

        self.rect.y += self.speed_y
        #define game limits
        if self.rect.centery > 750:
            self.rect.centery = 750
        if self.rect.centery < 50:
            self.rect.centery = 50

            #aumentar la velocidad con una tecla, aumentar el scrool y añadir un fuego 

        def shoot(self):
            pass #if pygame.keystate[pygame.K_SPACE]:
                