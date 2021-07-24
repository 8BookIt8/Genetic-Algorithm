from os import name

import matplotlib
import BIbear
import BIfood
import BIgeneration

import pygame
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import yaml

from random import uniform, randrange
import math
import keyboard
import time

class BIGame(): 
    def __init__(self): 
        self.screen_width = 901
        self.screen_height = 901
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Genetic Algorithm')

        self.background_color = (30, 30, 30)
        self.graph_background_color = (1 / 8.5, 1 / 8.5, 1 / 8.5)
        self.stage_color = (255, 255, 255)

        self.center = (451, 451)

        self.count_bear = settings['basic_settings']['count_bear']
        self.count_food = settings['basic_settings']['count_food']

        self.food_saturation = settings['basic_settings']['food_saturation']
        
        self.now_bear = self.count_bear

        self.spawn_distance = settings['basic_settings']['distance_bear']

        self.font = pygame.font.Font('fonts/font.ttf', 30)
        self.pos_font = (10, 860)

        self.generation = 1
        self.next_bear = settings['generation_settings']['next_bear']

        self.list_bear = pygame.sprite.Group()
        self.list_food = pygame.sprite.Group()

        self.figure = plt.figure(figsize = (9.375, 9.375), facecolor = self.graph_background_color, edgecolor = self.graph_background_color)
        self.plot = self.figure.add_subplot()
        self.plot.set_facecolor(self.graph_background_color)
        self.plot.spines['top'].set_color('white')
        self.plot.spines['right'].set_color('white')
        self.plot.spines['bottom'].set_color('white')
        self.plot.spines['left'].set_color('white')
        self.plot.set_xlabel('속력')
        self.plot.set_ylabel('크기')
        self.plot.xaxis.label.set_color('white')
        self.plot.xaxis.label.set_size(30)
        self.plot.yaxis.label.set_color('white')
        self.plot.yaxis.label.set_size(30)
        self.plot.tick_params(axis = 'x', colors = 'white')
        self.plot.tick_params(axis = 'y', colors = 'white')
        name_font = fm.FontProperties(fname = 'fonts/font.ttf').get_name()
        for item in ([self.plot.title, self.plot.xaxis.label, self.plot.yaxis.label] + self.plot.get_xticklabels() + self.plot.get_yticklabels()): 
            item.set_fontfamily(name_font)
        plt.show(block=False)

        self.list_x = []
        self.list_y = []

        self.graph = None

        self.is_paused = True

    def startGame(self): 
        clock = pygame.time.Clock()
        while True: 
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    exit()

            clock.tick(10000)

            if keyboard.is_pressed('p'): 
                self.is_paused = True
            elif keyboard.is_pressed('o'): 
                self.is_paused = False

            self.drawBackGround()
            
            if self.is_paused == False:
                for bear in self.list_bear: 
                    bear.move()

                    list_collide = pygame.sprite.spritecollide(bear, self.list_food, True, pygame.sprite.collide_mask)
                    for food in list_collide: 
                        bear.energy += self.food_saturation

                    if bear.energy <= 0 and self.now_bear > self.next_bear: 
                        self.list_bear.remove(bear)
                        self.now_bear -= 1

            if self.now_bear == self.next_bear: 
                self.is_paused = True
                self.generation += 1
                self.now_bear = self.count_bear

                self.list_x.clear()
                self.list_y.clear()

                new_list = BIgeneration.nextGeneration(self.list_bear)
                self.list_bear = pygame.sprite.Group()
                for bear in new_list: 
                    self.list_bear.add(bear)
                    self.list_x.append(bear.speed)
                    self.list_y.append(bear.size)

                self.addFoods()
                    
                self.drawGraph()

                self.is_paused = False
                time.sleep(0.1)

            generation_text = self.font.render('Gene : {}'.format(self.generation), True, (255, 255, 255))
            self.screen.blit(generation_text, self.pos_font)

            self.list_food.draw(self.screen)
            self.list_bear.draw(self.screen)

            pygame.display.update()

    def drawGraph(self): 
        if self.graph != None: 
            self.graph.set_visible(False)
        self.graph = self.plot.scatter(self.list_x, self.list_y, s = 20, c = (1, 1, 1))
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()

    def drawBackGround(self): 
        self.screen.fill(self.background_color)
        pygame.draw.circle(self.screen, self.stage_color, (451, 451), 450, 2)

    def addFoods(self): 
        self.list_food = pygame.sprite.Group()
        for i in range(1, (self.count_food + 1)): 
            new_food = BIfood.BIFood()
            self.list_food.add(new_food)

    def init(self): 
        for i in range(1, (self.count_bear + 1)): 
            speed = uniform(2, 4)
            size = randrange(20, 61)
            x = math.sin(((2 * math.pi) / self.count_bear) * i) * (self.spawn_distance - (size * 0.85))
            y = math.cos(((2 * math.pi) / self.count_bear) * i) * (self.spawn_distance - (size * 0.85))
            new_bear = BIbear.BIBear(x, y, speed, size)
            self.list_bear.add(new_bear)
            self.list_x.append(new_bear.speed)
            self.list_y.append(new_bear.size)

        self.addFoods()
        
        self.drawGraph()

with open('settings.yaml') as file: 
    settings = yaml.load(file, yaml.FullLoader)

pygame.init()

new_game = BIGame()
new_game.init()
new_game.startGame()