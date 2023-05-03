import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My game")

pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(10, 10, 100, 100))

pygame.draw.circle(screen, (255, 255, 0), (200, 200), 50)

image = ()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pass
            
            
    pygame.display.update()
            