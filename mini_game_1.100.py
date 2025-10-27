# Mini O‘yin – “Son topish”
# Foydalanuvchi kompyuter o‘ylagan sonni topadi.
import random

print("Men 1 dan 100 gacha bo'lgan son o'yladim. Topishga harakat qil!")
son = random.randint(1, 100)
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
