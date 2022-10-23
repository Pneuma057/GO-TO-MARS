
import pygame

class Spacecraft(pygame.sprite.Sprite):


    def __init__(self,colors, screen_size):
        super().__init__()
        self.set_spacecraft("spacecraft/nave_3.png", colors, 100, screen_size[1] // 2)
        self.colors = colors
        self.speed_y = 0
        self.auto_movement = False
        self.current_size = "full"

    def set_spacecraft(self, image_file, colors, x, y):
        self.image = pygame.image.load(image_file).convert()
        self.image.set_colorkey(colors[1])
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        #self.rect.x = x
        #self.rect.y = y

    def update(self):
        if self.auto_movement:
            self.auto_move_spacecraft()
        else:
            self.control_spacecraft()

    def auto_move_spacecraft(self):
        self.speed_y = 0
        self.rect.centerx += 10
        # 100 (full size:nave_3)--- 700 (medium size) --- 1400 (small
        if self.rect.x > 700 and self.current_size == "medium":
            # small
            self.set_spacecraft("spacecraft/nave_pull_1.png", self.colors, self.rect.centerx, self.rect.centery)
            self.current_size = "small"
        elif self.rect.x > 100 and self.current_size == "full":
            # change to medium
            self.set_spacecraft("spacecraft/nave_push_1.png", self.colors, self.rect.centerx, self.rect.centery)
            self.current_size = "medium"



    def control_spacecraft(self):
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
        def explosion (self):
            xplosion = pygame.image.load("spacecraft/crash.png").convert()
            pass
        def shoot(self):
            pass #if pygame.keystate[pygame.K_SPACE]:
                