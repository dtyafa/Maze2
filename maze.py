import pygame
from data import *

pygame.init()


class Sprite(pygame.Rect):
    def __init__(self, x, y, width, height, image_list, speed):
        super().__init__(x, y, width, height)
        self.IMAGE_LIST = image_list
        self.SPEED = speed
        self.IMAGE = self.IMAGE_LIST[0]
        self.IMAGE_NOW = self.IMAGE_LIST[0]
        self.COUNT_IMG = 0

    def move_image(self, max):
        if self.COUNT_IMG == max:
            self.COUNT_IMG = 0
        self.COUNT_IMG += 1
        if self.COUNT_IMG // 10 == self.COUNT_IMG / 10:
            self.IMAGE = self.IMAGE_LIST[self.COUNT_IMG // 10 - 1]
        




class Hero(Sprite):
    def __init__(self, x, y, width, height, image_list, speed):
        super().__init__(x, y, width, height, image_list, speed) 
        self.i = 0
        self.int = 0
        self.start_x = x
        self.start_y = self.y
        self.MOVE = {"UP": False, "DOWN": False, "LEFT": False, "RIGHT": False}
        
    def move(self):
        if self.MOVE["UP"]:
            self.y -= self.SPEED
            self.move_image(len(self.IMAGE_LIST) * 10 + 9)
        elif self.MOVE["DOWN"]:
            self.y += self.SPEED
            self.move_image(len(self.IMAGE_LIST) * 10 + 9)
        elif self.MOVE["LEFT"]:
            self.x -= self.SPEED
            self.move_image(len(self.IMAGE_LIST) * 10 + 9)
        elif self.MOVE["RIGHT"]:
            self.x += self.SPEED
            self.move_image(len(self.IMAGE_LIST) * 10 + 9)
        if self.x >= (setting_win["Width"] - 74): 
            self.x = self.x - self.SPEED
        if self.x <= -1: 
            self.x = self.x + self.SPEED
        if self.y >= (setting_win["Height"] - 175): 
            self.y = self.y - self.SPEED
        if self.y <= -2: 
            self.y = self.y + self.SPEED
        


    def lose(self):
        self.x = self.start_x
        self.y = self.start_y
    
class Enemy(Sprite):
    def __init__(self, x, y, width, height, image_list, speed, direction):
        super().__init__(x, y, width, height, image_list, speed)
        self.DIRECTION = direction
        self.start_x = self.x
        self.start_y = self.y
        self.GOBACK = False
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
        self.move_image(len(self.IMAGE_LIST) * 10 + 9)

    def lose(self):
        self.x = self.start_x
        self.y = self.start_y


class Wall(pygame.Rect):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height)
        self.COLOR = color
                                                       
def create_wall(key):
    x, y = 0, 0
    x1,y1 = 0,0
    step = setting_win["Width"] // 20

    index = 0
    for string in maps[key]:
        for element in string:
            if element == "1":
                for string in maps[key]:
                    if string[index] == "2":
                        wall_list.append(Wall(x,y, 20, y + y1, (255,100,45)))
                        break
                    y1 += step
            if element == "3":
                for element in string:
                    if element == "4":
                        wall_list.append(Wall(x - step + 20, y - 20, x +x1, 20, (255,100,45)))
                        break
                    x1 += step
            index += 1
            y += step
        y += step
        x = 0
create_wall("MAP1")
    