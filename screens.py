import pygame
import sys
from spacecraft import Spacecraft
from asteroids import Asteroid_big,Asteroid_mid
spacecraft = Spacecraft


class Menu():
    #def __init__(self, screen, spacecraft, font):
    def __init__(self, screen, clock):
        self.screen = screen
        self.font = pygame.font.Font("fonts/silkscreen.ttf", 50)
        self.background = pygame.image.load("planets/menu.png")
        #self.clock = clock
        self.spacecraft = spacecraft
        pygame.display.set_caption("START")
        #self.font = pygame.font.Font("fonts/space_age.ttf", 50)

    def run(self):
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    #TODO: Uncomment sys.exit() and remove "return True"
                    #sys.exit()
                    return

                #TODO: Make this work
                keystate = pygame.key.get_pressed()
                if keystate[pygame.K_RETURN]:
                    return

            self.screen.blit(self.background, (0, 0))
            MAGENTA = (255, 0, 255)
            menu = self.font.render("Pulsa ENTER para comenzar", True, MAGENTA)
            self.screen.blit(menu, (self.screen.get_width() // 2, self.screen.get_height() - 200))
            pygame.display.flip()

#TODO: Poner iniciales etc
class GameOver():
    #def __init__(self, screen, spacecraft, font):
    def __init__(self, screen, clock, score):
        self.screen = screen
        self.score = score
        self.font = pygame.font.Font("fonts/silkscreen.ttf", 50)
        self.background = pygame.image.load("planets/menu.png")
        #self.clock = clock
        self.spacecraft = spacecraft
        pygame.display.set_caption("START")
        self.background_image = pygame.image.load("planets/menu.png")
        #self.font = pygame.font.Font("fonts/space_age.ttf", 50)

    def run(self):
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    sys.exit()

                #TODO: Hacer que al pulsar ENTER continue a la siguiente pantalla
                keystate = pygame.key.get_pressed()
                if keystate[pygame.K_RETURN]:
                    return

            self.screen.blit(self.background, (0, 0))
            MAGENTA = (255, 0, 255)
            #TODO: Ajustar posicion game over
            game_over_font = self.font.render("GAME OVER", True, MAGENTA)
            self.screen.blit(game_over_font, (self.screen.get_width() // 2, self.screen.get_height() - 200))
            # TODO: Ajustar posicion final score
            score_font = self.font.render(f"Final score: {self.score}", True, MAGENTA)
            self.screen.blit(score_font, (self.screen.get_width() // 2, self.screen.get_height() - 400))
            pygame.display.flip()

class  Moon():
    def __init__(self,screen,spacecraft,asteroid_big,Asteroid_mid):
        pass 