
import pygame, random, sys
pygame.init()
W, H = 400, 400
s = pygame.display.set_mode((W,H))
clock = pygame.time.Clock()
cell = 20
snake = [(W//2, H//2)]
dir = (0, -cell)
food = (random.randrange(0,W,cell), random.randrange(0,H,cell))

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: sys.exit()
        if e.type == pygame.KEYDOWN:
            if e.key==pygame.K_UP: dir=(0,-cell)
            if e.key==pygame.K_DOWN: dir=(0,cell)
            if e.key==pygame.K_LEFT: dir=(-cell,0)
            if e.key==pygame.K_RIGHT: dir=(cell,0)
    head = (snake[0][0]+dir[0], snake[0][1]+dir[1])
    if head in snake or not (0<=head[0]<W and 0<=head[1]<H):
        print("O'ynash tugadi.")
        break
    snake.insert(0, head)
    if head == food:
        food = (random.randrange(0,W,cell), random.randrange(0,H,cell))
    else:
        snake.pop()
    s.fill((0,0,0))
    for seg in snake:
        pygame.draw.rect(s, (0,255,0), (*seg, cell, cell))
    pygame.draw.rect(s, (255,0,0), (*food, cell, cell))
    pygame.display.flip()
    clock.tick(8)