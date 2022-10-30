from textwrap import indent
import pygame, random

width = 1400
height = 800
black = (0,0,0)


class Asteroid_big(pygame.sprite.Sprite):
    def __init__(self,black):
        super().__init__()
        self.index=0
        self.pics = ["asteroids/b1.png","asteroids/b2.png","asteroids/b3.png","asteroids/b4.png","asteroids/b5.png","asteroids/b6.png","asteroids/b7.png","asteroids/b8.png","asteroids/b9.png","asteroids/b10.png","asteroids/b11.png","asteroids/b20.png"]
        self.image = pygame.image.load(self.pics[self.index])
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


    asteroid_list = 10

    def update(self):
        self.index+=0.15
        
        if self.index >= len(self.pics):
            self.index=0
        self.image=pygame.image.load(self.pics[int(self.index)])#el int es para que solo pueda tomar valores enteros 
    
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
        self.index=0
        self.pics = ["asteroids/m0.png","asteroids/m1.png","asteroids/m2.png","asteroids/m3.png","asteroids/m4.png","asteroids/m5.png","asteroids/m6.png"]
        self.image = pygame.image.load(self.pics[self.index])
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(5000,15000)
        self.rect.y = random.randint(70,730)
        self.speedy = random.randint(1,100)
        self.speedx = random.randint(-25,-5)

        self.pic_active = self.pics
        self.pic_active = 0
        self.change_pic = 10
        self.fps_count = 0


    asteroid_list = 10

    def update(self):
       
        self.index+=0.15
        
        if self.index >= len(self.pics):
            self.index=0
        self.image=pygame.image.load(self.pics[int(self.index)])#el int es para que solo pueda tomar valores enteros 
    
        self.speedy = random.randint(-10,10) 
        self.speedx = random.randint(-25,-5)
        self.rect.x += self.speedx #Generate a asteroid movement
        self.rect.y += self.speedy
        #reset and new object
        if self.rect.x < -100 or self.rect.y < 0 or self.rect.y > 800: #reset margins
            self.rect.y = random.randint(70,730)
            self.rect.x = random.randint(1400,10000)





    