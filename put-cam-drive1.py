import pygame
pygame.init()
window = pygame.display.set_mode((1200, 400))
track = pygame.image.load('track1.png')
car = pygame.image.load('SeekPng.com_car-top-view-png_544318.png')
car= pygame.transform.scale(car,(38,58))
car_x = 148
car_y =300
drive = True
clock = pygame.time.Clock()

while drive :
    clock.tick(60)
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            drive= False

    cam_x = car_x + 19
    cam_y = car_y + 15
    #car_y = car_y - 2
    window.blit(track, (0, 0))
    window.blit(car, (car_x, car_y))
    pygame.draw.circle(window,(0 ,255 ,0),(cam_x, cam_y),5 ,5)
    pygame.display.update()
