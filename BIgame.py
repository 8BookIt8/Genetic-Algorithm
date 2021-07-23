import pygame
import BIbear
import BIfood
import math
import keyboard

class BIGame(): 
    def __init__(self): 
        self.screen_width = 901
        self.screen_height = 901
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Genetic Algorithm")

        self.background_color = (30, 30, 30)
        self.stage_color = (255, 255, 255)
        self.entity_color = (191, 1, 15)

        self.center = (451, 451)

        self.count_bear = 60
        self.count_food = 80

        self.spawn_distance = 430

        self.list_bear = []
        self.list_food = []

        self.is_paused = True
        self.is_running = True

    def startGame(self): 
        clock = pygame.time.Clock()
        while self.is_running: 
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    self.is_running = False

            clock.tick(10000)

            if keyboard.is_pressed('p'): 
                self.is_paused = True
            elif keyboard.is_pressed('o'): 
                self.is_paused = False

            self.drawBackGround()

            for bears in self.list_bear: 
                bears.draw()
                if self.is_paused == False: 
                    bears.move()

            for foods in self.list_food: 
                foods.draw()

            pygame.display.update()

    def drawBackGround(self): 
        self.screen.fill(self.background_color)
        pygame.draw.circle(self.screen, self.stage_color, (451, 451), 450, 2)

    def init(self): 
        for i in range(1, (self.count_bear + 1)): 
            x = math.sin(((2 * math.pi) / self.count_bear) * i) * self.spawn_distance
            y = math.cos(((2 * math.pi) / self.count_bear) * i) * self.spawn_distance
            new_bear = BIbear.BIBear(self.screen, x, y, 15)
            self.list_bear.append(new_bear)

        for i in range(1, (self.count_food + 1)): 
            new_food = BIfood.BIFood(self.screen)
            self.list_food.append(new_food)

new_game = BIGame()
new_game.init()
new_game.startGame()