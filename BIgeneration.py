import BIbear

import yaml

import random
import math

with open("settings.yaml") as file: 
    settings = yaml.load(file, Loader=yaml.FullLoader)

next_bear = settings['generation_settings']['next_bear']
count_bear = settings['basic_settings']['count_bear']
chance_mutant = settings['generation_settings']['chance_mutant']

# 다음 세대 생성
def nextGeneration(list_bear):
    '''
    다음 세대 생성
        
    Args: 
        list_bear (list): 이전 세대 곰 리스트

    Returns: 
        new_list (list): 새로운 세대 곰 리스트
    ''' 
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
    '''
        자손 생성
        
        Args: 
            mom (BIbear): 엄마 곰
            dad (BIbear): 아빠 곰
            i (int): 순환 수
            j (int): i의 j 번째

        Returns: 
            dist (float)): 필드 중앙으로부터 pos까지의 거리
        '''
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
    '''
    곰 배치 좌표 계산
        
    Args: 
        i (int): 순환 수
        j (int): i의 j 번째
        size (float): 곰 크기

    Returns: 
        (x, y) (tuple): 곰 좌표
    '''
    spawn_distance = settings['basic_settings']['distance_bear']

    time = (next_bear * 0.5 * i) + j
    x = math.sin(((2 * math.pi) / count_bear) * time) * (spawn_distance - (size * 0.85))
    y = math.cos(((2 * math.pi) / count_bear) * time) * (spawn_distance - (size * 0.85))

    return (x, y)