import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("colour window")
run = True

while run:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_LEFT:
                screen.fill((255,0,0))
            if ev.key == pygame.K_RIGHT:
                screen.fill((0,255,0))
    pygame.display.update()