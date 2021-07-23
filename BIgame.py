from random import randrange
import pygame
import BIbear
import BIfood
import math
import keyboard

pygame.init()

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
        
        self.now_bear = self.count_bear

        self.spawn_distance = 450

        self.font = pygame.font.Font("fonts/font.ttf", 30)
        self.pos_font = (10, 860)

        self.generation = 1
        self.next_bear = 40

        self.list_bear = pygame.sprite.Group()
        self.list_food = pygame.sprite.Group()

        self.cause_speed = True
        self.cause_size = True

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

            generation_text = self.font.render("Gene : {}".format(self.generation), True, (255, 255, 255))
            self.screen.blit(generation_text, self.pos_font)
            
            if self.is_paused == False:
                for bear in self.list_bear: 
                    bear.move()

                    list_collide = pygame.sprite.spritecollide(bear, self.list_food, True, pygame.sprite.collide_mask)
                    for food in list_collide: 
                        bear.energy = 100

                    if bear.energy <= 0 and self.now_bear > self.next_bear: 
                        self.list_bear.remove(bear)
                        self.now_bear -= 1

            if self.now_bear == self.next_bear: 
                self.is_paused = True

            self.list_food.draw(self.screen)
            self.list_bear.draw(self.screen)

            pygame.display.update()

    def drawBackGround(self): 
        self.screen.fill(self.background_color)
        pygame.draw.circle(self.screen, self.stage_color, (451, 451), 450, 2)

    def init(self): 
        size = 30
        for i in range(1, (self.count_bear + 1)): 
            if self.cause_size: 
                size = randrange(20, 40)
            x = math.sin(((2 * math.pi) / self.count_bear) * i) * (self.spawn_distance - (size * 0.85))
            y = math.cos(((2 * math.pi) / self.count_bear) * i) * (self.spawn_distance - (size * 0.85))
            new_bear = BIbear.BIBear(self.screen, x, y, size)
            self.list_bear.add(new_bear)

        for i in range(1, (self.count_food + 1)): 
            new_food = BIfood.BIFood(self.screen)
            self.list_food.add(new_food)

new_game = BIGame()
new_game.init()
new_game.startGame()