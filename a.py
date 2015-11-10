import pygame
tela = pygame.display.set_mode([640, 480])
#pygame.draw.rect(tela, (255,0,0), (50,50,50,50))


for x in range(50, 640, 70):
    for y in range(50, 480, 70):
        a = pygame.draw.rect(tela, (255, x % 256, y % 256), (x, y, 50, 50))


pygame.display.flip()
raw_input('')