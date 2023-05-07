import pygame
from data import *

pygame.init()
global key
key = False

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
            if self.collidelist(wall_list) != -1:
                self.y += self.SPEED
            if key != True:
                if self.collidelist(door_list) != -1:
                    self.y += self.SPEED
        elif self.MOVE["DOWN"]:
            self.y += self.SPEED
            self.move_image(len(self.IMAGE_LIST) * 10 + 9)
            if self.collidelist(wall_list) != -1:
                self.y -= self.SPEED
            if key != True:
                if self.collidelist(door_list) != -1:
                    self.y -= self.SPEED
        elif self.MOVE["LEFT"]:
            self.x -= self.SPEED
            self.move_image(len(self.IMAGE_LIST) * 10 + 9)
            if self.collidelist(wall_list) != -1:
                self.x += self.SPEED
            if key != True:
                if self.collidelist(door_list) != -1:
                    self.x += self.SPEED
        elif self.MOVE["RIGHT"]:
            self.x += self.SPEED
            self.move_image(len(self.IMAGE_LIST) * 10 + 9)
            if self.collidelist(wall_list) != -1:
                self.x -= self.SPEED
            if key != True:
                if self.collidelist(door_list) != -1:
                    self.x -= self.SPEED
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
    def __init__(self, x, y, width, height, image_list, speed):
        super().__init__(x, y, width, height, image_list, speed)
        self.start_x = self.x
        self.start_y = self.y
        self.GOBACK = False
    def move(self, x1, y1, x2, y2, key):
        if key == "x":
            if self.x  < x1 or self > x2:
                self.SPEED *= -1
            self.x += self.SPEED
        if key == "y":
            if self.y  < y1 or self.y > y2:
                self.SPEED *= -1
            self.y += self.SPEED
        self.move_image(len(self.IMAGE_LIST) * 10 + 9)
    def lose(self):
        self.x = self.start_x
        self.y = self.start_y


class Wall(pygame.Rect):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height)
        self.COLOR = color

door_list = []                                  
def create_wall(key):
    x, y = 0, 0
    x1, y1 = 0, 0
    step =setting_win["Width"] // 20

    index_h = 0
    index_v = 0
    for string in maps[key]:
        for element in string:
            #vertical
            if element == "1":
                index_temp = index_v
                while True:
                    if maps[key][index_temp][index_h] == "2":
                        wall_list.append(Wall(x, y, 20, y1, (0, 204, 204)))
                        break
                    y1 += step
                    index_temp += 1
                y1 = 0
            if element == "5":
                index_temp = index_v
                while True:
                    if maps[key][index_temp][index_h] == "4":
                        wall_list.append(Wall(x, y, 20, y1, (0, 204, 204)))
                        break
                    y1 += step
                    index_temp += 1
                y1 = 0
            if element == "8":
                index_temp = index_v
                while True:
                    if maps[key][index_temp][index_h] == "2":
                        wall_list.append(Wall(x, y - 20, 20, y1 + 20, (0, 204, 204)))
                        break
                    y1 += step
                    index_temp += 1
                y1 = 0
            #horizontal
            if element == "3":
                index_temp = index_h
                while True:
                    if string[index_temp] == "4":
                        wall_list.append(Wall(x - step + 20, y - 20, x1 + 30, 20, (0, 204, 204)))
                        break
                    x1 += step
                    index_temp += 1
                x1 = 0
            if element == "6":
                index_temp = index_h
                while True:
                    if string[index_temp] == "7":
                        wall_list.append(Wall(x - step, y - 20, x1 + step * 2, 20, (0, 204, 204)))
                        break
                    x1 += step
                    index_temp += 1
                x1 = 0

            if element == "s":
                index_temp = index_h
                while True:
                    if string[index_temp] == "e":
                        door_list.append(Wall(x - step, y - 20, x1 + step * 2, 20, (153, 76, 0)))
                        break
                    x1 += step
                    index_temp += 1
                x1 = 0
            index_h += 1
            x += step
        y += step
        x = 0
        index_v += 1
        index_h = 0

def key_up():
    key = True

create_wall("MAP1")
    