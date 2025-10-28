# matrix_rain.py
import random, os, time
cols = os.get_terminal_size().columns
chars = "01"
while True:
    print("".join(random.choice(chars) for _ in range(cols)))
    time.sleep(0.05)