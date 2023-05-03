import game_2
from pygame.locals import * 
from sys import exit 
from random import randint

game_2.init()
game_2.display.set_caption('Snake')
screen = game_2.display.set_mode( (800, 600) )
clock = game_2.time.Clock()

head = Rect(400, 300, 30, 30)

SPEED = 10
DIRECTION =  [SPEED, 0]
COLOR = (255, 255, 255)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)
def move(head):
    global DIRECTION
    if head.bottom > 600:
        DIRECTION = [0, -SPEED]
        COLOR = random_color()
    elif head.top < 0:
        DIRECTION = [0, SPEED]
        COLOR = random_color()
    elif head.left < 0:
        DIRECTION = [SPEED, 0]
        COLOR = random_color()
    elif head.right > 800:
        DIRECTION = [-SPEED, 0]
        COLOR = random_color()
    
    head.move_ip((2, 2))


while 1:
    for event in game_2.event.get():
        if event.type:
            game_2.quit()
            exit()
            
    game_2.draw.rect(screen, COLOR, head)
    
    move(head)
                         
    game_2.display.update()
    clock.tick(30)