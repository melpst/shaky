import pygame
from pygame.locals import *

class Up:
    def __init__(self):
        self.pos = (400,20)
        self.img = pygame.image.load("up.png")
        
    def render(self,surface):
        pos = self.pos
        surface.blit(self.img,self.pos)

class Down(Up):
    def __init__(self):
        self.pos = (500,20)
        self.img = pygame.image.load("down.png")
        

class Left(Up):
    def __init__(self):
        self.pos = (300,20)
        self.img = pygame.image.load("left.png")

class Right(Up):
    def __init__(self):
        self.pos = (600,20)
        self.img = pygame.image.load("right.png")


######################################
class Music(object):

    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load('Nyan_Cat.ogg')

    def play(self):
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass
            #pygame.time.Clock().tick(10)

