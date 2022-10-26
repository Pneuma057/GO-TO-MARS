import pygame
import sys
from spacecraft import Spacecraft
from asteroids import Asteroid_big,Asteroid_mid
from sqlite_database import ScoreDatabase
spacecraft = Spacecraft
black = (0,0,0)
red = (215,64,64)

class Menu():
    #def __init__(self, screen, spacecraft, font):
    def __init__(self, screen, clock):
        self.screen = screen
        self.font = pygame.font.Font("fonts/space.ttf", 100)
        self.background = pygame.image.load("planets/menu.png")
        self.font2 = pygame.font.Font("fonts/space.ttf",25)
        self.font3 = pygame.font.Font("fonts/pack.ttf",35)
    
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

            menu = self.font.render("Press Enter", True, black)
            self.screen.blit(menu, (200, 600))

            controllers_up = self.font2.render("For up press:",True,black)
            self.screen.blit(controllers_up, (20,20))

            controllers_down = self.font2.render("For down press:",True,black)
            self.screen.blit(controllers_down,(20,70))

            key_w = self.font3.render("W",True,red)
            self.screen.blit(key_w,(350,15))

            key_s = self.font3.render("S",True,red)
            self.screen.blit(key_s,(335,60))
            self.center_x = 430
            self.center_y = 480
            pygame.display.flip()
            """
            self.image = pygame.image.load("spacecraft/nave_3.png").convert()
            self.image.set_colorkey(black)
            self.screen.blit(self.image,(480,430))

            self.image_astro = pygame.image.load("astronauts/astronaut.png").convert()
            self.image_astro.set_colorkey(black)
            self.screen.blit(self.image_astro,(600,400))
            
           """


            #########################################
       
class Stage():
    #def __init__(self, screen, spacecraft, font):
    def __init__(self, screen, clock,colors,fps,all_sprites,list_asteroid_big,list_asteroid_mid,player,health,score,background,title):
        self.screen = screen
        self.colors = colors
        self.fps = fps
        self.clock = clock
        self.player = player
        self.all_sprites = all_sprites
        self.list_asteroid_big = list_asteroid_big
        self.list_asteroid_mid = list_asteroid_mid
        self.health = health 
        self.score = score
        self.scroll = 0
        self.background = pygame.image.load(background)
        self.font = pygame.font.Font("fonts/space.ttf", 30)
        self.font2 = pygame.font.Font("fonts/pack.ttf",50)
        pygame.display.set_caption(title)
        #self.font = pygame.font.Font("fonts/space_age.ttf", 50)
        
    def run(self):
        runned_loops = 0
        gaming = True
        background_movement = True
        while gaming:

            time = pygame.time.get_ticks()

            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()



            #paint background
            self.screen.blit(self.background,(self.scroll,0))

            # Score rendering and computing
            score_font = self.font.render(f"Score Points: {self.score}", True, self.colors['white'])
            self.screen.blit(score_font, (600, 20))
            if runned_loops % 10 == 0:
                self.score += 100

            """counting_time = font.render("Time: "+str(time), 0, (120,70,0))
            screen.blit(counting_time, (800,20))
            """

            #counting_time.draw(screen)
            #counting_time.update()
            self.all_sprites.draw(self.screen)
            self.list_asteroid_big.draw(self.screen)
            self.list_asteroid_big.update()
            self.list_asteroid_mid.draw(self.screen)
            self.list_asteroid_mid.update()
            collides = pygame.sprite.spritecollide(self.player,self.list_asteroid_big,True)


        #collides

            if collides and background_movement:
                self.health -= 1
                if self.health == 0:
                    return self.score, self.health
            health_font = self.font2.render(f"LIVES: {self.health}", True, self.colors['white'])
            self.screen.blit(health_font, (20, 20))


            #scroll time
            if background_movement:
                self.scroll -= 0.4
            else:
                #for restore spacecraft image and position to initial state
                if self.player.rect.x >= self.screen.get_width():
                    #self.player.rect.x = 0
                    #self.player.rect.y = self.screen.get_height() // 2
                    self.player.set_spacecraft("spacecraft/nave_3.png", self.player.colors, 100, self.screen.get_height() // 2)
                    self.player.auto_movement = False
                    self.player.current_size = "full"
                    return self.score, self.health
            if abs (self.scroll) > self.screen.get_height():
                background_movement = False
                self.player.auto_movement = True
                #self.scroll = self.screen.get_height()
                #return self.score, self.health

            pygame.display.flip()
            self.all_sprites.update()

            runned_loops += 1

class GameOver():
    #def __init__(self, screen, spacecraft, font):
    def __init__(self, screen, clock, score):
        self.screen = screen
        self.score = score
        self.font = pygame.font.Font("fonts/space.ttf", 50)
        self.font_big = pygame.font.Font("fonts/space.ttf",75)
        self.background = pygame.image.load("planets/death.png")
        #self.clock = clock
        self.spacecraft = spacecraft
        pygame.display.set_caption("Game Over")
        self.background_image = pygame.image.load("planets/death.png")
        #self.font = pygame.font.Font("fonts/space_age.ttf", 50)
        self.database = ScoreDatabase()



    def run(self):
        input_box = pygame.Rect(100, 100, 140, 32)
        status = 0 # 0 Waiting user input, 1 Getting information from DB, 2 Printing informatin from DB
        username = ''
        base_print_width = 50
        base_print_height = 100
        run = True
        while run:
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
                elif status == 2 :
                    if evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_RETURN:
                            run = False

            self.screen.blit(self.background, (0, 0))
            MAGENTA = (255, 0, 255)
            #TODO: Ajustar posicion game over
            game_over_font = self.font_big.render("GAME OVER", True, MAGENTA)
            self.screen.blit(game_over_font, (800,10))

            # TODO: Ajustar posicion final score
            score_font = self.font.render(f"Final score: {self.score}", True, red)

            self.screen.blit(score_font, (10,10))

            if status == 2:
                # TODO: Ajustar posicion players
                score_font = self.font.render(f"Best scores:", True, red)
                self.screen.blit(score_font, (20,400))
                starting_db_score_position = 0
                for db_score in self.best_scores:
                    score_font = self.font.render(f"    {db_score[0]}: {db_score[1]}", True, red)
                    self.screen.blit(score_font, (10,500 + starting_db_score_position))
                    starting_db_score_position += 100

            if status == 1:
                self.database.add_score(username, self.score)
                self.best_scores = self.database.get_best_scores()
                self.database.close_connection()
                status = 2

            if status == 0:
                score_font = self.font.render(f"Input username: {username}", True, MAGENTA)
                self.screen.blit(score_font, (10,700))

            pygame.display.flip()
