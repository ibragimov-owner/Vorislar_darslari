# pip install pygame
import pygame, sys, random
pygame.init()
w,h=400,400
s=pygame.display.set_mode((w,h))
clock=pygame.time.Clock()
cell=20

def rand_pos():
    return (random.randrange(0,w,cell), random.randrange(0,h,cell))

snake=[(200,200),(180,200),(160,200)]
dir=(cell,0)
food=rand_pos()

while True:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: sys.exit()
        if e.type==pygame.KEYDOWN:
            if e.key==pygame.K_UP: dir=(0,-cell)
            if e.key==pygame.K_DOWN: dir=(0,cell)
            if e.key==pygame.K_LEFT: dir=(-cell,0)
            if e.key==pygame.K_RIGHT: dir=(cell,0)
    head=(snake[0][0]+dir[0], snake[0][1]+dir[1])
    head = (head[0]%w, head[1]%h)
    if head in snake:
        print("Game over")
        break
    snake.insert(0, head)
    if head==food:
        food=rand_pos()
    else:
        snake.pop()
    s.fill((0,0,0))
    for seg in snake: pygame.draw.rect(s,(0,255,0),(*seg,cell,cell))
    pygame.draw.rect(s,(255,0,0),(*food,cell,cell))
    pygame.display.flip()
    clock.tick(10)
