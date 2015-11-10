# coding: utf-8
"""
Snake game
"""

import pygame

SIZE = 640, 480
BLOCK = 50
BGCOLOR = (255, 255, 255)

def init():
    global screen
    screen = pygame.display.set_mode(SIZE, pygame.FULLSCREEN)
    pygame.draw.rect(screen, BGCOLOR, (0, 0, SIZE[0], SIZE[1]))
        
    
def loop():
    x, y = 0, 0
    old_x, old_y = 0, 0
    speed = BLOCK // 6
    vx, vy = speed, 0
    snake = [(x, y)]
    length = 10

    while True:
        if len(snake) >= length:
            pos = snake.pop(0)

        pygame.draw.rect(screen, BGCOLOR, (old_x, old_y, BLOCK, BLOCK))
        pygame.draw.rect(screen, (255, 0, 0), (x, y, BLOCK, BLOCK))
        pygame.display.flip()
        pygame.time.delay(100)
        old_x = x
        old_y = y
        pygame.event.pump()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            x += BLOCK
        elif keys[pygame.K_LEFT]:
            x -= BLOCK
        elif keys[pygame.K_UP]:
            y -= BLOCK
        elif keys[pygame.K_DOWN]:
            y += BLOCK
        elif keys[pygame.K_ESCAPE]:
            break

def quit():
    # pygame.time.delay(1500)
    pygame.quit()

try:
    init()
    loop()
finally:
    quit()
    