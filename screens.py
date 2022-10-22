import pygame
import sys
from spacecraft import Spacecraft
from asteroids import Asteroid_big,Asteroid_mid
from sqlite_database import ScoreDatabase
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
                    sys.exit()

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        return

            self.screen.blit(self.background, (0, 0))
            MAGENTA = (255, 0, 255)
            menu = self.font.render("Pulsa ENTER para comenzar", True, MAGENTA)
            self.screen.blit(menu, (self.screen.get_width() // 2, self.screen.get_height() - 200))
            pygame.display.flip()


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
        self.database = ScoreDatabase()



    def run(self):
        input_box = pygame.Rect(100, 100, 140, 32)
        status = 0 # 0 Waiting user input, 1 Getting information from DB, 2 Printing informatin from DB
        username = ''
        base_print_width = 50
        base_print_height = 100

        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.database.close_connection()
                    sys.exit()

                if status == 0:
                    if evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_RETURN:
                            status = 1
                        elif evento.key == pygame.K_BACKSPACE:
                            username = username[:-1]
                        else:
                            username += evento.unicode
                            username = username[:3]

            self.screen.blit(self.background, (0, 0))
            MAGENTA = (255, 0, 255)
            #TODO: Ajustar posicion game over
            game_over_font = self.font.render("GAME OVER", True, MAGENTA)
            self.screen.blit(game_over_font, (base_print_width, base_print_height))

            # TODO: Ajustar posicion final score
            score_font = self.font.render(f"Final score: {self.score}", True, MAGENTA)

            self.screen.blit(score_font, (base_print_width, base_print_height + 100))

            if status == 2:
                # TODO: Ajustar posicion players
                score_font = self.font.render(f"Best scores:", True, MAGENTA)
                self.screen.blit(score_font, (base_print_width, base_print_height + 200))
                starting_db_score_position = 0
                for db_score in self.best_scores:
                    score_font = self.font.render(f"    {db_score[0]}: {db_score[1]}", True, MAGENTA)
                    self.screen.blit(score_font, (base_print_width, base_print_height + 300 + starting_db_score_position))
                    starting_db_score_position += 100

            if status == 1:
                self.database.add_score(username, self.score)
                self.best_scores = self.database.get_best_scores()
                self.database.close_connection()
                status = 2

            if status == 0:
                score_font = self.font.render(f"Input username: {username}", True, MAGENTA)
                self.screen.blit(score_font, (base_print_width, base_print_height + 200))

            pygame.display.flip()

class  Moon():
    def __init__(self,screen,spacecraft,asteroid_big,Asteroid_mid):
        pass 