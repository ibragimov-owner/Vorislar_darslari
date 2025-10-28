"""
28.10.2025
3d_cube.py — Terminalda aylanadigan 3D kub (ASCII)

3d_cube.py

Bu skript terminalda aylanadigan 3D kubni ASCII san'atida chizadi.

Ishlatish:
      python3 3d_cube.py
"""
import math, os, time

A = B = 0
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    z = [0]*1760
    b = [' '] * 1760
    for j in range(0, 628, 7):
        for i in range(0, 628, 2):
            c = math.sin(i); d = math.cos(j)
            e = math.sin(A); f = math.sin(j)
            g = math.cos(A); h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i); m = math.cos(B); n = math.sin(B)
            t = c * h * g - f * e
            x = int(40 + 30 * D * (l * h * m - t * n))
            y = int(12 + 15 * D * (l * h * n + t * m))
            o = int(x + 80 * y)
            if 0 <= o < 1760 and D > z[o]:
                z[o] = D
                b[o] = ".,-~:;=!*#$@"[int(12 * (c * h * e - f * g))]
    print(''.join(b))
    A += 0.04
    B += 0.08
    time.sleep(0.03)