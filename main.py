# coding: utf-8
# jsobueno@gmail.com
# github/jsbueno
"""
Snake game with Atari Pitfall sounds
"""

import pygame
import sys
import random

w, h = 24, 18
BLOCK = 25
SIZE = BLOCK*w, BLOCK*h
COLOR_BG = (0, 0, 0)
COLOR_SNAKE = (0, 216, 0)
COLOR_FOOD = (216, 96, 0)

w, h = int(SIZE[0]/BLOCK), int(SIZE[1]/BLOCK)

def init():
    global screen, SOUND_FOOD, SOUND_DIED, SOUND_SWING
    screen = pygame.display.set_mode(SIZE)  #, pygame.FULLSCREEN)
    pygame.mixer.init()

    # source: http://www.digitpress.com/dpsoundz/soundfx.htm
    # SOUND_SWING = pygame.mixer.Sound("26KEYKAPR4.WAV")
    SOUND_FOOD = pygame.mixer.Sound("26PITFALL4.WAV")
    SOUND_DIED = pygame.mixer.Sound("26PITFALL2.WAV")

def play_food():
    SOUND_FOOD.play()

def play_died():
    SOUND_DIED.play()

def play_swing():
    # Playing this is too much
    # SOUND_SWING.play()
    pass

def clear_screen():
    pygame.draw.rect(screen, COLOR_BG, (0, 0, SIZE[0], SIZE[1]))

def get_keys(time_delay):
    pygame.time.delay(time_delay)
    # pygame.event.pump()
    # Source: http://stackoverflow.com/questions/5891808/how-to-invert-colors-of-an-image-in-pygame
    events = pygame.event.get()
    # print "len events", len(events)
    kk = []
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP,
             pygame.K_DOWN, pygame.K_ESCAPE]:
                kk.append(event.key)
    return kk


def quit():
    # pygame.time.delay(1500)
    pygame.quit()


def die(msg):
    print msg
    play_died()

    for i in range(27):
        pixels = pygame.surfarray.pixels2d(screen)
        pixels ^= 2 ** 32 - 1
        del pixels
        pygame.display.flip()
        pygame.time.delay(100)
    quit()
    sys.exit()

def loop():
    x, y = 0, 0
    old_x, old_y = 0, 0
    dx, dy = 1, 0
    snake_size = 1  # snake size
    food = []
    snake = [[0, 0]]
    kk = []

    while True:
        clear_screen()

        # renders non-visually
        m = [[0]*h for i in range(w)] # entities
        for seg in snake:
            m[seg[0]][seg[1]] = 1
        if len(food) > 0:
            m[food[0]][food[1]] = 2

        if len(food) == 0:
            while True:
                fx = random.randint(0, w-1)
                fy = random.randint(0, h-1)
                if m[fx][fy] == 0:
                    food = [fx, fy]
                    break

        # renders visually
        for i in range(w):
            for j in range(h):
                x_ = i*BLOCK
                y_ = j*BLOCK
                if m[i][j] == 1:
                    # snake
                    pygame.draw.rect(screen, COLOR_SNAKE, (x_, y_, BLOCK, BLOCK))
                elif m[i][j] == 2:
                    # food
                    pygame.draw.ellipse(screen, COLOR_FOOD, (x_, y_, BLOCK, BLOCK))

        pygame.display.flip()

        kk.extend(get_keys(200))
        if len(kk) > 0:
            key = kk[0]
            del kk[0]
            if key == pygame.K_RIGHT:
                if dx == 0:
                    dx, dy = 1, 0
                    play_swing()
            elif key == pygame.K_LEFT:
                if dx == 0:
                    dx, dy = -1, 0
                    play_swing()
            elif key == pygame.K_UP:
                if dy == 0:
                    dx, dy = 0, -1
                    play_swing()
            elif key == pygame.K_DOWN:
                if dy == 0:
                    dx, dy = 0, 1
                    play_swing()
            elif key == pygame.K_ESCAPE:
                break
        x += dx
        y += dy

        if x >= w or x < 0 or y >= h or y < 0:
            die("Crashed with border")
        if m[x][y] == 1:
            die("Collided with itself")
        if m[x][y] == 2:
            print "Ate sth"
            play_food()
            snake_size += 1
            food = []
        snake.append([x, y])
        while len(snake) > snake_size:
            del snake[0]

try:
    init()
    loop()
finally:
    quit()
