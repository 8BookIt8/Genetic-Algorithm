import pygame
import yaml

import math
from random import randrange

with open('settings.yaml') as file: 
    settings = yaml.load(file, yaml.FullLoader)

center = (451, 451)
spawn_distance = settings['basic_settings']['max_distance_food']

class BIFood(pygame.sprite.Sprite): 
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/food.png").convert_alpha()
        self.x = center[0]
        self.y = center[1]
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.top = 0
        self.size = 5
        self.init()

    def distanceFromCenter(self, pos): 
        dist = ((center[0] - pos[0]) ** 2) + ((center[1] - pos[1]) ** 2)
        dist = math.sqrt(dist)
        return dist

    def setRect(self): 
        self.rect.left = self.x - 5
        self.rect.top = self.y - 5

    def init(self): 
        while True: 
            x = randrange(spawn_distance * -1, spawn_distance + 1)
            y = randrange(spawn_distance * -1, spawn_distance + 1)
            if (self.distanceFromCenter((self.x + x, self.y + y)) <= spawn_distance): 
                self.x += x
                self.y += y
                self.setRect()
                break