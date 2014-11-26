import pygame
from pygame.locals import *

class Up:
    
    def __init__(self, pos=(400,20)):
        (self.x,self.y) = pos
        self.img = pygame.image.load("res/up.png")
        self.vy =80
        self.count = 0

    def render(self,surface):
        surface.blit(self.img,(self.x,self.y))
    
    def change_speed(self):
        self.vy += 20

    def move(self,delta_t):
        self.y += self.vy*(1./delta_t)

class Down(Up):
    def __init__(self):
        (self.x,self.y) = (500,20)
        self.img = pygame.image.load("res/down.png")
        

class Left(Up):
    def __init__(self):
        (self.x,self.y) = (300,20)
        self.img = pygame.image.load("res/left.png")

class Right(Up):
    def __init__(self):
        (self.x,self.y) = (600,20)
        self.img = pygame.image.load("res/right.png")


######################################
class Music(object):

    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load('res/Nyan_Cat.ogg')

    def play(self):
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass
            #pygame.time.Clock().tick(10)

