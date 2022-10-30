
import pygame

class Spacecraft(pygame.sprite.Sprite):


    def __init__(self,colors, screen_size):
        super().__init__()
        self.set_spacecraft("spacecraft/nave_3.png", colors, 100, screen_size[1] // 2)
        self.colors = colors
        self.speed_y = 0
        self.auto_movement = False
        self.current_size = "full"
        self.is_exploding = False
        self.explosion_time = None
        self.explosion_sound = pygame.mixer.Sound("sounds/explosion.wav")
        self.last_key_pressed = None
        self.movement_time = None
        self.pressing_time_for_speed_up = 250
        self.regular_speed = 5
        self.turbo_speed = self.regular_speed * 3

    def set_spacecraft(self, image_file, colors, x, y):
        self.image = pygame.image.load(image_file).convert()
        self.image.set_colorkey(colors[1])
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
     

    def update(self):
        # if self.is_exploding and self.exploding_frames == self.current_exploding_frames:
        if self.is_exploding and not self.explosion_time:
            self.explosion_time = pygame.time.get_ticks()
            pygame.mixer.Sound.play(self.explosion_sound)
            self.set_spacecraft("spacecraft/bk_crash.png", self.colors, self.rect.centerx, self.rect.centery)
        elif self.is_exploding and self.explosion_time + 1000 < pygame.time.get_ticks():
            self.is_exploding = False
            self.explosion_time = None
            self.set_spacecraft("spacecraft/nave_3.png", self.colors, self.rect.centerx, self.rect.centery)

        if self.auto_movement:
            self.auto_move_spacecraft()
        else:
            self.control_spacecraft()

    def auto_move_spacecraft(self):
        self.speed_y = 0
        self.rect.centerx += 5
        
        if self.rect.x > 1100 and self.current_size == "medium":
            # small
            self.set_spacecraft("spacecraft/nave_32.png", self.colors, self.rect.centerx, self.rect.centery)
            self.current_size = "small"
        
        elif self.rect.x > 900 and self.current_size == "full":
            # change to medium
            self.set_spacecraft("spacecraft/nave_31.png", self.colors, self.rect.centerx, self.rect.centery)
            self.current_size = "medium"



    def control_spacecraft(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            if self.last_key_pressed != pygame.K_w:
                self.speed_y = -self.regular_speed
                self.last_key_pressed = pygame.K_w
                self.movement_time = pygame.time.get_ticks()
            elif self.last_key_pressed == pygame.K_w and self.movement_time + self.pressing_time_for_speed_up < pygame.time.get_ticks():
                self.speed_y = -self.turbo_speed
            elif self.last_key_pressed == pygame.K_w:
                self.speed_y = -self.regular_speed
        elif keystate[pygame.K_s]:
            if self.last_key_pressed != pygame.K_s:
                self.speed_y = self.regular_speed
                self.last_key_pressed = pygame.K_s
                self.movement_time = pygame.time.get_ticks()
            elif self.last_key_pressed == pygame.K_s and self.movement_time + self.pressing_time_for_speed_up < pygame.time.get_ticks():
                self.speed_y = self.turbo_speed
            elif self.last_key_pressed == pygame.K_s:
                self.speed_y = self.regular_speed
        else:
            self.speed_y = 0
            self.last_key_pressed = None
      

        self.rect.y += self.speed_y
        #define game limits
        if self.rect.centery > 750:
            self.rect.centery = 750

        if self.rect.centery < 50:
            self.rect.centery = 50

        

            
        

      
                