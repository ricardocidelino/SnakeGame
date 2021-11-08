import random,pygame
from pygame.locals import *

def on_grid_random():
    x = random.randint(0, 59)
    y = random.randint(0, 59)
    return (x * 10, y * 10)


def collision(c1,c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

def direction(snake,my_direction):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])
