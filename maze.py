import pygame

pygame.init()

class Hero(pygame.Rect):
    def __init__(self, x, y, width, height, image, speed, win):
        super().__init__(x, y, width, height)
        self.IMAGE = image
        self.SPEED = speed
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
    def draw(self):
        self.WIN.blit(pygame.image.load(self.IMAGE), (self.x, self.y))

