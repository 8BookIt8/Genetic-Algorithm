import BIbear

import yaml

import random
import math

with open("settings.yaml") as file: 
    settings = yaml.load(file, Loader=yaml.FullLoader)

next_bear = settings['generation_settings']['next_bear']
count_bear = settings['basic_settings']['count_bear']
chance_mutant = settings['generation_settings']['chance_mutant']

def nextGeneration(list_bear): 
    new_list = []

    list_bear = list_bear.sprites()
    for i in range(0, int(count_bear / (next_bear / 2))): 
        random.shuffle(list_bear)
        j = 0
        while j < next_bear: 
            child = makeChild(list_bear[j], list_bear[j+1], i, j / 2)
            new_list.append(child)
            j += 2

    return new_list

            
def makeChild(mom, dad, i, j): 
    speed_min = min(mom.speed, dad.speed)
    speed_max = max(mom.speed, dad.speed)

    size_min = min(mom.size, dad.size)
    size_max = max(mom.size, dad.size)

    speed = random.uniform(speed_min, speed_max)
    size = random.randrange(size_min, size_max + 1)

    if (random.randrange(1, 101) <= chance_mutant): 
        speed = speed * random.uniform(0.75, 1.5)
    if (random.randrange(1, 101) <= chance_mutant): 
        size = int(size * random.uniform(0.75, 1.5))
    
    pos = getPostion(i, j, size)
    return BIbear.BIBear(pos[0], pos[1], speed, size)

def getPostion(i, j, size): 
    spawn_distance = settings['basic_settings']['distance_bear']

    time = (next_bear * 0.5 * i) + j
    x = math.sin(((2 * math.pi) / count_bear) * time) * (spawn_distance - (size * 0.85))
    y = math.cos(((2 * math.pi) / count_bear) * time) * (spawn_distance - (size * 0.85))

    return (x, y)