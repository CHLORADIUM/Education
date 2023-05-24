from symbol import while_stmt
import pygame
import sys
import random

pygame.init()


screen_a = 800
screen_b = 600
screen = pygame.display.set_mode((screen_a, screen_b))
pygame.display.set_caption("racing game")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

player_png = pygame.image.load("car.png")
player_r = player_png.image.get_rect()
player_r.centerx = screen_a // 2
player_r.bottom = screen_b - 10
player_s = 5

oppo_png = pygame.image.load("oppo_car.png")
oppo_r = oppo_png.image.get_rect()
oppo_r.centerx = random.randint(100, screen_a - 100)
oppo_r.bottom =  -100
oppo_s = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_r.left > 0:
        player_r.x -= player_s
    if keys[pygame.K_RIGHT] and player_r.right < screen_a:
        player_r.x += player_s
        
        