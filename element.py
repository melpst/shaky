import pygame
from pygame.locals import *

from random import *

class Arrow:
    def __init__(self,type = "none", y = 20):
        self.type = type
        self.y = y
        self.vy = 120
        
        if self.type == "left":
            self.x = 300
            self.img = pygame.image.load("res/left.png")
        elif self.type == "down":
            self.x = 500
            self.img = pygame.image.load("res/down.png")
        elif self.type == "up":
            self.x = 400
            self.img = pygame.image.load("res/up.png")
        elif self.type == "right":
            self.x = 600
            self.img = pygame.image.load("res/right.png")
        else:
            self.type = randint(0,3)

    def render(self,surface):
        surface.blit(self.img,(self.x,self.y))
    
    def change_speed(self):
        self.vy += 20

    def move(self,delta_t, time):
        is_changed = False
        if time < 13.0:
            self.y -= self.vy*(1./delta_t)
        else:
            if not is_changed:
                self.change_speed()
                is_changed = True

######################################
class Music(object):

    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load('res/Nyan_Cat.ogg')

    def play(self):
        pygame.mixer.music.play()
