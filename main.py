import pygame
from pygame.locals import *

import gamelib
from element import *

from random import *

class ShakyGame(gamelib.SimpleGame):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    GREEN = pygame.Color('green')
    
    def __init__(self):
        super(ShakyGame, self).__init__('ShakyShaky', ShakyGame.BLACK)
        self.time = 0
        
        lock_left = Arrow(0)
        lock_down = Arrow(1)
        lock_up = Arrow(2)
        lock_right = Arrow(3)
        self.lock_arrow = [lock_left,lock_down,lock_up,lock_right]

    def init(self):
        super(ShakyGame, self).init()
        self.music = Music()
        y = 600
        self.arrow = Arrow(y=y)
        self.bg = Background()

    def update(self):
        self.check_key_pressed()
        if self.is_started:
            self.play_game()

    def render(self, surface):
        if self.is_started: 
            self.bg.render(surface)
            surface.blit(self.time_image, (625,10))
            self.render_arrow(surface)
    
    def render_time(self):
        self.time += self.clock.get_time()/1000.0
        self.time_image = self.font.render("Time = %.3f" % self.time, 0,ShakyGame.WHITE)
            
    def render_arrow(self, surface):
        for lock in self.lock_arrow:
            lock.render(surface)
        if self.time > 3.0 and self.arrow.y > 20:
            self.arrow.render(surface)
                 
    def move_arrow(self):
        if self.time > 3.0:
            self.arrow.move(self.fps, self.time)

    def check_key_pressed(self):
        if self.is_key_pressed(K_UP):
            print "up"
        elif self.is_key_pressed(K_DOWN):
            print "down"
        elif self.is_key_pressed(K_LEFT):
            print "left"
        elif self.is_key_pressed(K_RIGHT):
            print "right"
        elif self.is_key_pressed(K_RETURN):
            self.is_started = True
            self.music.play()

    def play_game(self): 
        self.render_time()
        self.move_arrow()

def main():
    game = ShakyGame()
    game.run()

if __name__ == '__main__':
    main()
