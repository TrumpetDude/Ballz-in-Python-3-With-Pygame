import pygame, sys
from pygame.locals import *
from random import randint
from math import sqrt
pygame.init()
window = pygame.display.set_mode((350,700))
pygame.display.set_caption("Balls","Balls")
pygame.key.set_repeat(1,1)
window.fill((0,0,0))
pygame.display.update()

'''
4 Lists control the balls
[px]position x
[py]position y
[vx]velocity x
[vx]velocity y
'''

px = []
py = []
vx = []
vy = []
level = 1

def moveAndDrawBalls(level, px, vx, py, vy, xspeed, yspeed):
    counter = 0
    notBouncing = 0
    while (notBouncing < level-1):
        notBouncing = 0

        #get quit
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE) or (event.type == KEYDOWN and event.key == K_q):
                pygame.quit()
                sys.exit(0)

        #launch
        launchTime = 10
        if counter%launchTime == 0 and counter//launchTime < level-1:
            vx[counter//launchTime] = xspeed
            vy[counter//launchTime] = yspeed

        for b in range(0, level-1):
            #erase
            pygame.draw.circle(window, (0,0,0), (int(px[b]), int(py[b])), 2, 0)
            #move x
            px[b] += vx[b]
            #reverse x
            if px[b] >= 350 or px[b] <= 0:
                vx[b] *= -1
            #move y
            py[b] += vy[b]
            #reverse y
            if py[b] <= 0:
                vy[b] *= -1
            #stop
            if py[b]>=705:
                vx[b] = 0
                vy[b] = 0
                notBouncing += 1
            #draw
            pygame.draw.circle(window, (127,127,127), (int(px[b]), int(py[b])), 2, 0)

        pygame.display.update()
        counter+=1
        

#Game Loop
while True:
    window.fill((0,0,0))#background


    #increase/reset
    px.append(175)
    for n in range(0,level):
        px[n] = 175

    vx.append(0)
    for n in range(0,level):
        vx[n] = 0

    py.append(700)
    for n in range(0,level):
        py[n] = 700

    vy.append(0)
    for n in range(0,level):
        vy[n] = 0

    level += 1

    #get click and calculate initial velocities
    mousePos=pygame.mouse.get_pos()
    mousePressed=pygame.mouse.get_pressed()
    while not(sum(mousePressed)):
        mousePos=pygame.mouse.get_pos()
        mousePressed=pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE) or (event.type == KEYDOWN and event.key == K_q):
                pygame.quit()
                sys.exit(0)
    if sum(mousePressed) > 0:
        xspeed = 175 - mousePos[0] 
        yspeed = 700 - mousePos[1] 
        magnitude = sqrt(xspeed*xspeed+yspeed*yspeed)
        speed = 0.17
        xspeed /= -magnitude*speed
        yspeed /= -magnitude*speed

    
    moveAndDrawBalls(level, px, vx, py, vy, xspeed, yspeed)
    
    
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE) or (event.type == KEYDOWN and event.key == K_q):
            pygame.quit()
            sys.exit(0)
    keys = pygame.key.get_pressed()
    pygame.display.update()
