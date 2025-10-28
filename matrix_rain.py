"""
28.10.2025

matrix_rain.py

matrix_rain.py bu terminalda "Matrix" filmidagi kod yomg'irini taqlid qiluvchi dasturdir.

Ishlatish uchun terminal oynasini oching va quyidagi buyruqni bajarish orqali skriptni ishga tushiring:

python matrix_rain.py

Dastur terminal oynasining kengligini aniqlaydi va har bir qator uchun tasodifiy "0" va "1" belgilaridan iborat satrlarni yaratadi. Har bir yangi qator ekranda pastga siljiydi, bu esa kod yomg'irining vizual effektini yaratadi.
"""
import random, os, time
cols = os.get_terminal_size().columns
chars = "01"
while True:
    print("".join(random.choice(chars) for _ in range(cols)))
    time.sleep(0.05)