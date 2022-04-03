import pygame
pygame.init()
window = pygame.display.set_mode((1200, 400))
track = pygame.image.load('track1.png')
car = pygame.image.load('SeekPng.com_car-top-view-png_544318.png')
car= pygame.transform.scale(car,(40,60))
drive = True
while drive :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            drive= False
    window.blit(track, (0, 0))
    window.blit(car, (0, 0))
    pygame.display.update()