import pygame
from pygame.locals import *

from random import *

class Arrow:
    def __init__(self,type = -1, y = 20):
        self.type = type
        self.y = y
        self.vy = 50
        self.is_changed = False
        
        if self.type == -1:
            self.type = randint(0,3)
        self.init()
        
    def render(self,surface):
        surface.blit(self.img,(self.x,self.y))

    def init(self):
        if self.type == 0:
            self.x = 200
            self.img = pygame.image.load("res/left.png")
        elif self.type == 1:
            self.x = 300
            self.img = pygame.image.load("res/down.png")
        elif self.type == 2:
            self.x = 400
            self.img = pygame.image.load("res/up.png")
        elif self.type == 3:
            self.x = 500
            self.img = pygame.image.load("res/right.png") 
    
    def change_speed(self):
        self.vy += 100
        self.is_changed = True

    def move(self,delta_t, time):
        if time >= 3.0:
            self.y -= self.vy*(1.0/delta_t)
        if time > 5.0:
            if not self.is_changed:
                self.change_speed()

######################################
class Music(object):

    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load('res/Nyan_Cat.ogg')

    def play(self):
        pygame.mixer.music.play()
#######################################
class Background(object):
    def __init__(self):
        (self.x, self.y) = (-200, 0)
        self.images = ("res/Nyan-cat.jpg") # add image in tuple 
        self.pic ="res/Nyan-cat.jpg" # add image for first time
        self.time = 0
        self.count = 0

    def change_image(self):
        if self.count < len(self.images):
            self.count += 1
        else:
            self.count = 0
        self.pic = self.images[self.count]

    def render(self,surface):
        self.img =pygame.image.load(self.pic)
        self.time += pygame.time.Clock().get_time()
        if self.time/1000.0 > 3000.0:
            self.change_image()
        surface.blit(self.img,(self.x,self.y))

