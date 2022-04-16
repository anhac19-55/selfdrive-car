import pygame
pygame.init()
window = pygame.display.set_mode((1200, 400))
track = pygame.image.load('track2.png')
car = pygame.image.load('SeekPng.com_car-top-view-png_544318.png')
car= pygame.transform.scale(car,(38,58))
car_x = 148
car_y =300
focal_dist = 25
drive = True
clock = pygame.time.Clock()

while drive :
    clock.tick(60)
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            drive= False
 #detect road with camera
    cam_x = car_x + 19
    cam_y = car_y + 15
    up_px = window.get_at((cam_x, cam_y - focal_dist))[0]
    print(up_px)
    if up_px == 255:
       car_y = car_y - 2
    window.blit(track, (0, 0))
    window.blit(car, (car_x, car_y))
    pygame.draw.circle(window,(0 ,255 ,0),(cam_x, cam_y),5 ,5)
    pygame.display.update()
