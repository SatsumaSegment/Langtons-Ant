import pygame

COLOR = (155, 0, 0)

class Cell:
    def __init__(self, screen, x, y, w, h):
        self.screen = screen
        self.x = x
        self.y = y 
        self.w = w
        self.h = h


    def draw(self, f):
        self.f = f
        self.this = pygame.draw.rect(self.screen, COLOR, (self.x, self.y, self.w, self.h), self.f)
    

class Ant:
    def __init__(self, screen, x, y, r):
        self.screen = screen
        self.x = x
        self.y = y
        self.r = r

    def draw(self):
        self.this = pygame.draw.rect(self.screen, (255,255,255), (self.x, self.y, 5, 5))

    def update(self, x, y, r):
        self.r = r
        self.x = x
        self.y = y