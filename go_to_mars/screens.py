from main import pygame
from spacecraft import Spacecraft
from asteroids import Asteroid_big,Asteroid_mid
from game import font,screen
spacecraft = Spacecraft


class Menu():
    def __init__(self,screen,spacecraft,font):
        self.screen = screen
        #self.time = time
        self.spacecraft = Spacecraft
        pygame.display.set_caption("START")
        self.background_image = pygame.image.load("planets/menu.png")
        self.font = font
        self.font = pygame.font.Font("fonts/space_age.ttf",50)


class  Moon():
    def __init__(self,screen,spacecraft,asteroid_big,Asteroid_mid):
        pass 