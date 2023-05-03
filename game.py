import game_2
import spritesheet

game_2.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = game_2.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game_2.display.set_caption("Spritesheets")

sprite_sheet_image = game_2.image.load("doux.png").convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

BG = (50, 50, 50)
BLACK = (0,0, 0)

animation_list = []
animation_steps = 4
last_update = game_2.time.get_ticks()
animation_cooldown = 500
frame = 0

for x in range(animation_steps):
    animation_list.append(sprite_sheet.get_image(x, 24, 24, 3, BLACK))
    

run = True
while run:
    
    screen.fill(BG)
    
    current_time = game_2.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time 
    
    
    screen.blit(animation_list[frame], (x * 72, 0))
  
    
    for event in game_2.event.get():
        if event.type == game_2.QUIT:
            run = False
            
            game_2.display.update() 