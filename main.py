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
        
        self.music = Music()
        self.bg = Background()
        self.is_started = False
        self.is_ended = False
        
    def init(self):
        super(ShakyGame, self).init()
        
        self.arrow = [Arrow()]
        self.time = 0.0
        self.tmp_time = self.time
        self.score = 0
        self.life = 3
        self.chk_bg = False
        self.is_destroyed = True

       
    def start_game(self):
        self.init()
        self.is_started = True
        self.is_ended = False
        self.music.play()

    def update(self):
        if not self.board == []:
            self.check_board()
        if self.is_started and not self.is_ended:
            self.play_game()
            if self.chk_bg == False:
                print "in chk_bg"
                self.chk_bg = True
                self.bg.change_image()
        
        if self.life == 0:
            self.end_state()
            self.is_started = False
            self.is_ended = True
    
    def end_state(self):
        if not self.is_started and self.is_ended:
            if self.chk_bg == True :
                self.bg.change_image(self.is_ended)
                self.chk_bg = False
            self.music.stop()
            print "stop music in end state"

    def render(self, surface):
        self.bg.render(surface)
        
        if self.is_started: 
            surface.blit(self.time_image, (625,10))
            self.render_arrow(surface)
        elif self.is_ended:
            surface.blit(self.end_time,(400,280))
            
    def check_board(self):
        try:
            x = self.board.getAcceleroX()
            y = self.board.getAcceleroY()
        except USBError:
            pass

        arrow = self.arrow[0]
        if self.is_started:
            if self.is_destroyed:
                if arrow.y < 30 and arrow.y > 10:
                    if x<-200:
                        self.check_key_press(arrow,K_LEFT)
                    if x>200:
                        self.check_key_press(arrow,K_RIGHT)
                    if y<-200:
                        self.check_key_press(arrow,K_UP)
                    if y>200:
                        self.check_key_press(arrow,K_DOWN)
        else:
            if self.board.getSwitch():
                self.start_game()
            
    def on_key_up(self,key):
        if self.is_started == False:
            if key == K_RETURN:
                self.start_game()
        else:
            if len(self.arrow) > 0:
                arrow = self.arrow[0]
                if arrow.y < 30 and arrow.y > 10:
                    self.check_key_press(arrow,key)
                else:
                    if key == K_LEFT or key == K_DOWN or key == K_UP or key == K_RIGHT:
                        self.arrow_destroyer(arrow)
                        self.life -= 1


    def check_key_press(self,arrow,key):
        if key == K_LEFT:
            if arrow.type == 0:
                self.score += 1
                print self.score
                self.is_destroyed = False
            print "left"
        elif key == K_DOWN:
            if arrow.type == 1:
                self.score += 1
                print self.score
                self.is_destroyed = False
            print "down"
        elif key == K_UP:
            if arrow.type == 2:
                self.score += 1
                print self.score
                self.is_destroyed = False
            print "up"
        elif key == K_RIGHT:
            if arrow.type == 3:
                self.score += 1
                print self.score
                self.is_destroyed = False
            print "right"
        else:
            self.life -= 1
        if not self.is_destroyed:
            self.arrow_destroyer(arrow)

    def render_time(self):
        self.time += self.clock.get_time()/1000.0
        self.time_image = self.font.render("Time = %.3f" % self.time, 0,ShakyGame.WHITE)
        self.end_time = pygame.font.SysFont("Tlwg Typist,BlodOblique",30).render("YOUR TIME : %.3f"% self.time ,1,ShakyGame.WHITE)
            
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
                self.life -= 1

    def arrow_creator(self):
        self.arrow.append(Arrow())

    def arrow_destroyer(self,arrow):
        self.arrow.remove(arrow)
        self.is_destroyed = True
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
