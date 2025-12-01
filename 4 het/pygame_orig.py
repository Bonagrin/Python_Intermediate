import pygame

KEPERNYO_SZELESSEG = 480
KEPERNYO_MAGASSAG = 360

pygame.init()
kepernyo = pygame.display.set_mode((KEPERNYO_SZELESSEG, KEPERNYO_MAGASSAG))
pygame.display.set_caption('Űrhajós játék')

űrhajó = pygame.Surface((30, 50))
űrhajó.fill((255, 255, 255))
kepernyo.blit(űrhajó, ((KEPERNYO_SZELESSEG - űrhajó.get_width()) // 2, KEPERNYO_MAGASSAG - 70))

fut = True
while fut:
    for esemeny in pygame.event.get():
        if esemeny.type == pygame.QUIT:
            fut = False

    pygame.display.flip()

pygame.quit()
