"""
28.10.2025

matrix_rain.py

matrix_rain.py bu terminalda "Matrix" filmidagi kod yomg'irini taqlid qiluvchi dasturdir.

Ishlatish uchun terminal oynasini oching va quyidagi buyruqni bajarish orqali skriptni ishga tushiring:

    python matrix_rain.py

Dastur terminal oynasining kengligini aniqlaydi va har bir qator uchun tasodifiy "0" va "1" belgilaridan iborat satrlarni yaratadi.

Har bir yangi qator ekranda pastga siljiydi, bu esa kod yomg'irining vizual effektini yaratadi.
"""


import random, os, time

# Terminal kengligini aniqlaymiz
cols = os.get_terminal_size().columns
chars = "01"

# Yashil rang kodi
GREEN = "\033[32m"
RESET = "\033[0m"

while True:
    line = "".join(random.choice(chars) for _ in range(cols))
    print(GREEN + line + RESET)
    time.sleep(0.05)

# Dastur tugatish uchun Ctrl+C tugmalarini bosing