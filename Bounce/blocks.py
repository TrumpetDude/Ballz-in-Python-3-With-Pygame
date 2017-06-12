import pygame, sys
from pygame.locals import *
from random import randint
from math import sqrt
pygame.init()
window = pygame.display.set_mode((350,700))
pygame.display.set_caption("Blocks","Blocks")
pygame.key.set_repeat(1,1)
window.fill((0,0,0))
pygame.display.update()

'''
Block has 3 attributes:
[xPos, yPos, strength]
'''

#method to draw text
def drawText(window, text, size, color, centerX, centerY):
    font=pygame.font.Font("PressStart2p.ttf", size)
    renderedText=font.render(str(text),True,color)
    textpos=renderedText.get_rect()
    textpos.centerx=centerX
    textpos.centery=centerY
    window.blit(renderedText, textpos)
    
#create blocks once per level
def makeBlocks():
    for xPos in range(0,300,50):
        if randint(2,5)<=2:
            if level >= 3:
                blocks.append([xPos,-50,randint(int(level/3),int(level*1.2))])
            else:
                blocks.append([xPos,-50,1])
                
#move blocks down
def moveBlock(block):
    block[1] += 50
    
#draw blocks
def drawBlock(block):
    pygame.draw.rect(window, (255,255,255), (block[0],block[1],50,50), 0)
    drawText(window, str(block[2]), 13, (0,0,0), block[0]+25, block[1]+25)

clock = pygame.time.Clock()
blocks = []
level = 1

#Game Loop
while True:
    window.fill((0,0,0))#background
    level += 1#increase level
    makeBlocks();#create blocks
    for block in blocks:
        moveBlock(block)
        drawBlock(block)
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE) or (event.type == KEYDOWN and event.key == K_q):
            pygame.quit()
            sys.exit(0)
    keys = pygame.key.get_pressed()
    clock.tick(1)
    pygame.display.update()
