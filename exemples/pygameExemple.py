#!/usr/bin/python3

import pygame
from pygame.locals import *


def main():
    pygame.init()
    pygame.font.init()
    window = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
    font = pygame.font.SysFont('Arial', 30)
    image = pygame.image.load("../ressources/schema_bat2.png").convert()
    image = pygame.transform.scale(image, (720, 720))
    carre_rouge = pygame.image.load("../ressources/carre_rouge.png").convert()
    carre_rouge = pygame.transform.scale(carre_rouge, (340, 350))
    carre_vert = pygame.image.load("../ressources/carre_vert.png").convert()
    carre_vert = pygame.transform.scale(carre_vert, (320, 350))
    text = font.render('Salle Rétro', False, (0, 0, 0))
    window.blit(image, (0, 0))
    window.blit(carre_rouge, (35, 30))
    window.blit(carre_vert, (380, 30))
    window.blit(text, (55, 150))
    pygame.display.flip()
    on = True
    while on:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                on = False

if __name__ == "__main__":
    main()
