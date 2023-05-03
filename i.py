#ya importiroval biblioteku
import pygame
#ya inicializiroval pygame
pygame.init()

#ya izmenil shiriny i vysotu
a = 700
b = 800

#ya dal shirinu i vysotu oknu
e = pygame.display.set_mode((a,b))
#ya izmenil nazvanie okna
pygame.display.set_caption("window of window")

pygame.draw.circle(e,(255, 255, 0), (200, 300), 150)
pygame.draw.rect((255,0,0), (100, 50) )

#uslovie istinno
while True:
    #pereimenoval komandu na ivent
    for event in pygame.event.get():
        #dal uslovie uslovnomu operatoru
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    
