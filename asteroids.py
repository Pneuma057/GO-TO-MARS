import pygame, random

width = 1400
height = 800
black = (0,0,0)


class Asteroid_big(pygame.sprite.Sprite):
    def __init__(self,black):
        super().__init__()
        self.pics = {list : ["b1.png","b2.png","b3.png"]}
        self.image = pygame.image.load("asteroids/big_1.png")
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(4000,15000)
        self.rect.y = random.randint(70,730)
        self.speedy = random.randint(5,10)
        self.speedx = random.randint(-10,-1)

        self.pic_active = self.pics
        self.pic_active = 0
        self.change_pic = 10
        self.fps_count = 0

    def load_pic(self,pics):
        self.pics = {}
        for picture in self.pics:
            A = pygame.image.load(f"asteroids/{picture}")
            pics.append(A)

        #TODO: asteroids rotate


        """
        self.frames = []
        self.index = 0
        self.how_images = 0
        self.animation_time = fps // 2
        self.w
        self.y

        self.load.frames()

    def Asteroid_big_sheet(self,h,y):
        self.w
        self.y

        asteroid_big_sheet = pygame.image.load("asteroids/asteroid_big_list.png")
        for row in range(5):
            y = row = self.h
            image = pygame.surface((self.w,self.h),pygame.SRCALPHA).pygame.Surface.convert_alpha()
            image.blit(asteroid_big_sheet, )
            """        
    asteroid_list = 10

    def update(self):
        
        self.speedy = random.randint(-10,10) 
        self.speedx = random.randint(-10,-5)
        self.rect.x += self.speedx #Generate a asteroid movement
        self.rect.y += self.speedy
        #reset and new object
        if self.rect.x < -100 or self.rect.y < 0 or self.rect.y > 600: #reset margins
            self.rect.y = random.randint(70,730)
            self.rect.x = random.randint(1400,10000)
    

        
        

class Asteroid_mid(pygame.sprite.Sprite):
    def __init__(self, black):
        super().__init__()
        self.image = pygame.image.load("asteroids/mid.png")
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(5000,15000)
        self.rect.y = random.randint(70,730)
        self.speedy = random.randint(1,100)
        self.speedx = random.randint(-25,-5)
    asteroid_list = 10

    def update(self):
        
        self.speedy = random.randint(-10,10) 
        self.speedx = random.randint(-25,-5)
        self.rect.x += self.speedx #Generate a asteroid movement
        self.rect.y += self.speedy
        #reset and new object
        if self.rect.x < -100 or self.rect.y < 0 or self.rect.y > 800: #reset margins
            self.rect.y = random.randint(70,730)
            self.rect.x = random.randint(1400,10000)
            

    