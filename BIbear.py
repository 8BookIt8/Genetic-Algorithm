import math
from random import randrange
import pygame

center = (451, 451)
spawn_distance = 430

class BIBear(): 
    def __init__(self, screen, x, y, size):
        self.screen = screen
        self.x = center[0] + x
        self.y = center[1] + y
        self.size = size
        self.speed = 3
        self.energy = 100

    def distanceFromCenter(self, pos): 
        dist = ((center[0] - pos[0]) ** 2) + ((center[1] - pos[1]) ** 2)
        dist = math.sqrt(dist)
        return dist

    def move(self): 
        x = randrange(-1, 2) * self.speed
        y = randrange(-1, 2) * self.speed
        if (self.distanceFromCenter((self.x + x, self.y + y)) <= spawn_distance): 
            self.x += x
            self.y += y

    def draw(self): 
        pygame.draw.circle(self.screen, (255, 0, 0), (self.x, self.y), self.size, 0)