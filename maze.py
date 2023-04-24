import pygame
from data import *

pygame.init()

class Hero(pygame.Rect):
    def __init__(self, x, y, start_x, start_y, width, height, image, speed, win):
        super().__init__(x, y, width, height)
        self.IMAGE = image
        self.SPEED = speed
        self.start_x = self.x
        self.start_y = self.y
        self.WIN = win
        self.MOVE = {"UP": False, "DOWN": False, "LEFT": False, "RIGHT": False}
        
    def move(self):
        if self.MOVE["UP"]:
            self.y -= self.SPEED
        if self.MOVE["DOWN"]:
            self.y += self.SPEED
        if self.MOVE["LEFT"]:
            self.x -= self.SPEED
        if self.MOVE["RIGHT"]:
            self.x += self.SPEED
        if self.x >= (setting_win["Width"] - 74): 
            self.x = self.x - self.SPEED
        if self.x <= -1: 
            self.x = self.x + self.SPEED
        if self.y >= (setting_win["Height"] - 175): 
            self.y = self.y - self.SPEED
        if self.y <= -2: 
            self.y = self.y + self.SPEED

    def draw(self):
        self.WIN.blit(pygame.image.load(self.IMAGE), (self.x, self.y))

    def lose(self):
        self.x = self.start_x
        self.y = self.start_y
    
class Enemy(pygame.Rect):
    def __init__(self, x, y, start_x, start_y, width, height, image, speed, win, direction):
        self.IMAGE = image
        self.SPEED = speed
        self.DIRECTION = direction
        self.start_x = self.x
        self.start_y = self.y
        self.GOBACK = False
        self.WIN = win
    def move(self):
        if self.DIRECTION == "x":
            if self.GOBACK == False:
                self.x = self.x + self.SPEED
                if self.x >= (setting_win["Width"] - 98):
                    self.GOBACK = True
            elif self.GOBACK == True:
                self.x = self.x - self.SPEED
                if self.x <= -1:
                    self.GOBACK = False
        if self.DIRECTION == "y":
            if self.GOBACK == False:
                self.y = self.y + self.SPEED
                if self.y >= (setting_win["Height"] - 100):
                    self.GOBACK = True
            elif self.GOBACK == True:
                self.y = self.y - self.SPEED
                if self.y <= -2:
                    self.GOBACK = False

    def draw(self):
        self.WIN.blit(pygame.image.load(self.IMAGE), (self.x, self.y))
            
            