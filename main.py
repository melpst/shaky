import pygame
from pygame.locals import *

import gamelib
from element import * 

class ShakyGame(gamelib.SimpleGame):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    GREEN = pygame.Color('green')
    
    def __init__(self):
        super(ShakyGame, self).__init__('ShakyShaky', ShakyGame.BLACK)
        self.time = 0
        
        self.lock_up = Up()
        self.lock_down = Down()
        self.lock_left = Left()
        self.lock_right = Right()

    def init(self):
        super(ShakyGame, self).init()
        self.music = Music()
        y = 600
        
        self.up = Up(y=y)
        self.down = Down(y=y)
        self.left = Left(y=y)
        self.right = Right(y=y)

        self.run_arrow = [self.left,self.down,self.up,self.right]

    def update(self):
        self.check_key_pressed()
        if self.is_started:
            self.play_game()



    def render(self, surface):
        if self.is_started: 
            surface.blit(self.time_image, (800,10))
            
            self.lock_up.render(surface)
            self.lock_down.render(surface)
            self.lock_left.render(surface)
            self.lock_right.render(surface)
            
            self.render_arrow(surface)
    
    def render_time(self):
        self.time += self.clock.get_time()/1000.0
        self.time_image = self.font.render("Time = %.3f" % self.time, 0,ShakyGame.WHITE)
            
    def render_arrow(self, surface):
        if self.time > 3.0 and self.up.y > 20:
            self.up.render(surface)
    
    def move_arrow(self):
        if not self.up == None and self.time > 3.0:
            self.up.move(self.fps, self.time)

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

    def play_game(self): 
        self.render_time()
        #self.music.play()
        self.move_arrow()

def main():
    game = ShakyGame()
    game.run()

if __name__ == '__main__':
    main()
