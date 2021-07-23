import math
from random import randrange
import pygame

center = (451, 451)
spawn_distance = 350

class BIFood(): 
    def __init__(self, screen):
        self.screen = screen
        self.x = center[0]
        self.y = center[1]
        self.size = 5
        self.init()

    def distanceFromCenter(self, pos): 
        dist = ((center[0] - pos[0]) ** 2) + ((center[1] - pos[1]) ** 2)
        dist = math.sqrt(dist)
        return dist

    def init(self): 
        while True: 
            x = randrange(spawn_distance * -1, spawn_distance + 1)
            y = randrange(spawn_distance * -1, spawn_distance + 1)
            if (self.distanceFromCenter((self.x + x, self.y + y)) <= spawn_distance): 
                self.x += x
                self.y += y
                break

    def draw(self): 
        pygame.draw.circle(self.screen, (0, 255, 0), (self.x, self.y), self.size, 0)