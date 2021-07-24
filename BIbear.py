from matplotlib.pyplot import specgram
import pygame
import yaml

import math
from random import randrange, uniform

with open('settings.yaml') as file: 
    settings = yaml.load(file, yaml.FullLoader)

center = (451, 451)
spawn_distance = settings['basic_settings']['distance_bear']

class BIBear(pygame.sprite.Sprite): 
    def __init__(self, x, y, speed, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.x = center[0] + x
        self.y = center[1] + y
        self.target_x = randrange(300, 600)
        self.target_y = randrange(300, 600)
        self.speed = speed
        self.spawn_distance = spawn_distance - (self.size * 0.85)
        self.energy = 100
        self.image = pygame.image.load("images/bear.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.setRect()

    def distanceFrom(self, bear, pos): 
        dist = ((pos[0] - bear[0]) ** 2) + ((pos[1] - bear[1]) ** 2)
        dist = math.sqrt(dist)
        return dist

    def setRect(self): 
        self.rect.left = self.x - 15
        self.rect.top = self.y - 15

    def changeTarget(self): 
        pos = (1000, 1000)
        while self.distanceFrom(pos, center) >= self.spawn_distance: 
            x = uniform(10, 891)
            y = uniform(10, 891)
            pos = (x, y)
        self.target_x = pos[0]
        self.target_y = pos[1]

    def move(self): 
        x = self.speed if self.target_x - self.x > 0 else -self.speed
        y = self.speed if self.target_y - self.y > 0 else -self.speed
        self.energy -= (0.5 * (self.speed ** 2) * (self.size)) / 300
        self.x += x
        self.y += y
        self.setRect()

        if randrange (1, 101) <= 1 or self.distanceFrom((self.x, self.y), (self.target_x, self.target_y)) <= self.speed: 
            self.changeTarget()
