import pygame
from pygame.locals import *

import gamelib
from element import *

from random import *
from practicum import findDevices
from peri import PeriBoard
from usb import USBError

class ShakyGame(gamelib.SimpleGame):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    GREEN = pygame.Color('green')
    
    def __init__(self):
        super(ShakyGame, self).__init__('ShakyShaky', ShakyGame.BLACK)
        
        self.board = []
        for i,dev in enumerate(findDevices()):
            self.board = PeriBoard(dev)
            print "Board connect"
        self.pressed_switch = 0
        self.time = 0
        
        lock_left = Arrow(0)
        lock_down = Arrow(1)
        lock_up = Arrow(2)
        lock_right = Arrow(3)
        self.lock_arrow = [lock_left,lock_down,lock_up,lock_right]
        

    def init(self):
        super(ShakyGame, self).init()
        
        self.music = Music()
        self.bg = Background()
        self.arrow = [Arrow()]
        self.tmp_time = self.time
        self.score = 0
        self.hp = 50

    def update(self):
        if not self.board == [] and self.board.getSwitch():
            if self.is_started == False:
                print 'True'
                self.is_started = True
                self.music.play()
        if self.is_started:
            self.play_game()
            self.bg.change_image(1)
        if self.score == -3:
            self.is_started = False
#            self.bg.change_image() #if change_image()*2 == endgameImage

    def render(self, surface):
        self.bg.render(surface)
        if self.is_started: 
            surface.blit(self.time_image, (625,10))
            self.render_arrow(surface)

    def on_key_up(self,key):
        if len(self.arrow) > 0:
            arrow = self.arrow[0]
            if arrow.y < 30 and arrow.y > 10:
                self.check_key_press(arrow,key)
                self.arrow_destroyer(arrow)
            else:
                if key == K_LEFT or key == K_DOWN or key == K_UP or key == K_RIGHT:
                    self.arrow_destroyer(arrow)
                    self.score -= 1

        if self.is_started == False:
            if key == K_RETURN:
                self.is_started = True
                self.music.play()

    def check_key_press(self,arrow,key):
        if key == K_LEFT:
            if arrow.type == 0:
                self.score += 1
                print self.score
            print "left"
        elif key == K_DOWN:
            if arrow.type == 1:
                self.score += 1
                print self.score
            print "down"
        elif key == K_UP:
            if arrow.type == 2:
                self.score += 1
                print self.score
            print "up"
        elif key == K_RIGHT:
            if arrow.type == 3:
                self.score += 1
                print self.score
            print "right"

    def render_time(self):
        self.time += self.clock.get_time()/1000.0
        self.time_image = self.font.render("Time = %.3f" % self.time, 0,ShakyGame.WHITE)
            
    def render_arrow(self, surface):
        for lock in self.lock_arrow:
            lock.render(surface)
        
        if self.time > 1.0 and len(self.arrow) > 0:
            for arrow in self.arrow:
                arrow.render(surface)
                 
    def move_arrow(self):
        for arrow in self.arrow:
            arrow.move(self.fps, self.time)
            if arrow.y < -100:
                self.arrow_destroyer(arrow)

    def arrow_creator(self):
        self.arrow.append(Arrow())

    def arrow_destroyer(self,arrow):
        self.arrow.remove(arrow)
        print "remove"

    def play_game(self): 
        self.render_time()
        
        if len(self.arrow) > 0:
            self.move_arrow()
        
        if int(self.time) == self.tmp_time+5: 
            self.arrow_creator()
            self.tmp_time += 2

def main():
    game = ShakyGame()
    game.run()

if __name__ == '__main__':
    main()
