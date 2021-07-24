import pygame
import yaml

import math
from random import randrange

with open('settings.yaml') as file: 
    settings = yaml.load(file, yaml.FullLoader)

center = (451, 451)
spawn_distance = settings['basic_settings']['distance_bear']

class BIBear(pygame.sprite.Sprite): 
    def __init__(self, screen, x, y, speed, size):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.size = size
        self.x = center[0] + x
        self.y = center[1] + y
        self.speed = speed
        self.spawn_distance = spawn_distance - (self.size * 0.85)
        self.energy = 100
        self.image = pygame.image.load("images/bear.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.setRect()

    def distanceFromCenter(self, pos): 
        dist = ((center[0] - pos[0]) ** 2) + ((center[1] - pos[1]) ** 2)
        dist = math.sqrt(dist)
        return dist

    def setRect(self): 
        self.rect.left = self.x - 15
        self.rect.top = self.y - 15

    def move(self): 
        x = randrange(-1, 2) * self.speed
        y = randrange(-1, 2) * self.speed
        self.energy -= (0.5 * (self.speed ** 2) * (self.size)) / 4500
        if (self.distanceFromCenter((self.x + x, self.y + y)) <= self.spawn_distance): 
            self.x += x
            self.y += y
            self.setRect()