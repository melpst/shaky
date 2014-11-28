import pygame
from pygame.locals import *

from random import *

class Arrow:
    def __init__(self,type = 4, y = 20):
        self.type = type
        self.y = y
        self.vy = 50
        self.is_changed = False
        
        if self.type == 4:
            self.type = randint(0,3)
        self.init()
        
    def render(self,surface):
        surface.blit(self.img,(self.x,self.y))

    def init(self):
        if self.type == 0:
            self.x = 300
            self.img = pygame.image.load("res/left.png")
        elif self.type == 1:
            self.x = 500
            self.img = pygame.image.load("res/down.png")
        elif self.type == 2:
            self.x = 400
            self.img = pygame.image.load("res/up.png")
        elif self.type == 3:
            self.x = 600
            self.img = pygame.image.load("res/right.png")
    
    def change_speed(self):
        self.vy += 100
        self.is_changed = True

    def move(self,delta_t, time):
        if time >= 3.0:
            self.y -= self.vy*(1./delta_t)
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
