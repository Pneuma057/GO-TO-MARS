from go_to_mars import pygame
from spacecraft import Spacecraft
from asteroids import Asteroid_big,Asteroid_mid
from launch import height,width,time,screen,font


class Menu():
    def __init__(self,screen,time,spacecraft,font):
        self.screen = screen
        self.time = time
        self.spacecraft = Spacecraft
        pygame.display.set_caption("START")
        self.background_image = pygame.image.load("planets/space.png")
        self.font = pygame.font.Font("fonts/space_age.ttf",50)
        
       