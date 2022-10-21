from main import pygame
from spacecraft import Spacecraft
from asteroids import Asteroid_big,Asteroid_mid



class Menu():
    def __init__(self,screen,time,spacecraft,font):
        self.screen = screen
        self.time = time
        self.spacecraft = Spacecraft
        pygame.display.set_caption("START")
        self.background_image = pygame.image.load("planets/space.png")
        self.font = pygame.font.Font("fonts/space_age.ttf",50)

    def Level_1(self,screen,spacecraft,asteroid_big,asteroid_mid):
        pass 
    