import pygame
from pygame.locals import *

import gamelib

class ShakyGame(gamelib.SimpleGame):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    GREEN = pygame.Color('green')
    
    def __init__(self):
        super(ShakyGame, self).__init__('ShakyShaky', ShakyGame.BLACK)
        self.score = 0

    def init(self):
        super(ShakyGame, self).init()
        self.render_score()

    def update(self):
        if self.is_key_pressed(K_UP):
            self.player.move_up()
        elif self.is_key_pressed(K_DOWN):
            self.player.move_down()
        
#self.render_score()
        
    def render_score(self):
        self.score_image = self.font.render("Score = %d" % self.score, 0,ShakyGame.WHITE)

    def render(self, surface):
        surface.blit(self.score_image, (10,10))

def main():
    game = ShakyGame()
    game.run()

if __name__ == '__main__':
    main()
