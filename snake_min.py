"""
28.10.2025

snake_min.py — Pygame yordamida juda oddiy "Snake" (minimal)

snake_min.py

Oddiy "Snake" o'yinining minimal versiyasi Pygame kutubxonasi yordamida amalga oshirilgan.

O'yin oynasi 400x400 piksel o'lchamda bo'lib, har bir segment 20x20 piksel o'lchamda.

O'yinchi o'q tugmalari yordamida ilonni boshqaradi. Ilon o'z tanasiga yoki devorlarga urilganda o'yin tugaydi.

Ilon ovqatni yeganida, u o'sadi va yangi ovqat tasodifiy joyda paydo bo'ladi.

Iltimos, Pygame kutubxonasi o'rnatilganligiga ishonch hosil qiling: pip install pygame
"""
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