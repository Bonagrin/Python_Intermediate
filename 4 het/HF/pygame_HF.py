import pygame
import random

pygame.init()

SZÉLESSÉG, MAGASSÁG = 600, 400
ablak = pygame.display.set_mode((SZÉLESSÉG, MAGASSÁG))
pygame.display.set_caption("Pygame")

FEHÉR = (255, 255, 255)
PIROS = (255, 0, 0)
ZÖLD = (0, 255, 0)

játékos_mérete = 40
játékos_x = SZÉLESSÉG // 2
játékos_y = MAGASSÁG // 2
játékos_sebesség = 5

pont_mérete = 30
pont_x = random.randint(0, SZÉLESSÉG - pont_mérete)
pont_y = random.randint(0, MAGASSÁG - pont_mérete)

pontszám = 0
betű = pygame.font.SysFont(None, 36)

fut = True
fps = pygame.time.Clock()

while fut:
    fps.tick(60)
    
    for esemény in pygame.event.get():
        if esemény.type == pygame.QUIT: fut = False

    billentyű = pygame.key.get_pressed()
    if billentyű[pygame.K_LEFT]: játékos_x  -= játékos_sebesség
    if billentyű[pygame.K_RIGHT]: játékos_x += játékos_sebesség
    if billentyű[pygame.K_UP]: játékos_y    -= játékos_sebesség
    if billentyű[pygame.K_DOWN]: játékos_y  += játékos_sebesség

    játékos_x = max(0, min(SZÉLESSÉG - játékos_mérete, játékos_x))
    játékos_y = max(0, min(MAGASSÁG - játékos_mérete, játékos_y))

    játékos_rect = pygame.Rect(játékos_x, játékos_y, játékos_mérete, játékos_mérete)
    pont_rect = pygame.Rect(pont_x, pont_y, pont_mérete, pont_mérete)
    
    if játékos_rect.colliderect(pont_rect):
        pontszám += 1
        pont_x = random.randint(0, SZÉLESSÉG - pont_mérete)
        pont_y = random.randint(0, MAGASSÁG - pont_mérete)

    ablak.fill(FEHÉR)
    pygame.draw.rect(ablak, PIROS, játékos_rect)
    pygame.draw.rect(ablak, ZÖLD, pont_rect)
    pont_szöveg = betű.render(f"Pontszám: {pontszám}", True, (0, 0, 0))
    ablak.blit(pont_szöveg, (10, 10))
    
    pygame.display.update()

pygame.quit()
