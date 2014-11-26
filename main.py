import pygame
from pygame.locals import *

import gamelib

class ShakyGame(gamelib.SimpleGame):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    GREEN = pygame.Color('green')
    
    def __init__(self):
        super(ShakyGame, self).__init__('ShakyShaky', ShakyGame.BLACK)
        self.time = 0

    def init(self):
        super(ShakyGame, self).init()

    def update(self):
        if self.is_key_pressed(K_UP):
            self.player.move_up()
        elif self.is_key_pressed(K_DOWN):
            self.player.move_down()
        elif self.is_key_pressed(K_RETURN):
            self.is_started = True
        if self.is_started:
            self.render_time()
        
    def render_time(self):
        self.time += self.clock.get_time()
        self.time_image = self.font.render("Time = %d" % (self.time/1000.0), 0,ShakyGame.WHITE)

    def render(self, surface):
        if self.is_started:
            surface.blit(self.time_image, (480,10))

def main():
    game = ShakyGame()
    game.run()

if __name__ == '__main__':
    main()
