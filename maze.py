import pygame

pygame.init()

class Hero(pygame.Rect):
    def __init__(self, x, y, width, height, image, speed):
        super().__init__(x, y, width, height)
        self.IMAGE = image
        self.SPEED = speed
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
