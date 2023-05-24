import pygame
import random

pygame.init
random.init
 
screen = pygame.display.set_mode((2000,3000))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

rect = pygame.display.draw((255,255,255), (500, 1500)