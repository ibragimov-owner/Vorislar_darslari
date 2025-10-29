"""
27.10.2025

Mini O‘yin – “Son topish”
Foydalanuvchi kompyuter o‘ylagan sonni topadi.

Qoidalar:
1. Kompyuter 1 dan 10 gacha bo‘lgan son o‘ylaydi.
2. Foydalanuvchi taxmin kiritadi.
3. Agar foydalanuvchi kiritgan son kompyuter o‘ylagan sondan kichik bo‘lsa, 
   kompyuter “Kichik son aytding, yana urinib ko‘r!” deb javob beradi.
4. Agar foydalanuvchi kiritgan son katta bo‘lsa,
   kompyuter “Katta son aytding, yana urin!” deb javob beradi.
   5. Foydalanuvchi to‘g‘ri sonni topganda, kompyuter “To‘g‘ri! 🎉 Siz {taxminlar} urinishda topding!” deb javob beradi.
"""
import random

print("Men 1 dan 100 gacha bo'lgan son o'yladim. Topishga harakat qil!")
son = random.randint(1, 10)
taxminlar = 0

while True:
    taxmin = int(input("Taxminingni kiriting: "))
    taxminlar += 1
    if taxmin < son:
        print("Kichik son aytding, yana urinib ko‘r!")
    elif taxmin > son:
        print("Katta son aytding, yana urin!")
    else:
        print(f"To‘g‘ri! 🎉 {taxminlar} urinishda topding!")
        break
