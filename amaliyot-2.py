"""
30.10.2025
··Shartlar:
· O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
· Ro'yxatning uzunligini konsolga chiqaring
· sorted () funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
· sorted () yordamida ro'yxatni teskari tartibda konsolga chiqaring
· Asl ro'yxatni qaytadan konsolga chiqaring
· reverse () metodi yordamida ro'yxatni ortidan boshlab chiqaring
· sort () metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
· 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
· Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
· Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
· Ro'yxatdagi elementlar sonini hisoblang
· Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
· taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
"""

# Davlatlar ro'yxatini yaratamiz
davlatlar = ["Ozbekiston", "AQSH", "Rossiya", "Xitoy", "Turkiya"]

# Ro'yxatni ekranga chiqaramiz
print(davlatlar)

# Ro'yxat uzunligini (nechta element borligini) chiqaramiz
print("Ro'yxat uzunligi:", len(davlatlar))

# Davlatlarni alifbo tartibida (A dan Z gacha) tartiblab chiqaramiz
print("Tartiblangan ro'yxat:", sorted(davlatlar))

# Davlatlarni alifboga teskari tartibda (Z dan A gacha) chiqaramiz
print("Teskari tartiblangan ro'yxat:", sorted(davlatlar, reverse=True))

# Asl ro'yxatni (tartiblanmagan holatda) yana chiqaramiz
print("Asl ro'yxat:", davlatlar)

# Ro'yxatni butunlay teskari tartibda aylantiramiz (birinchi element oxiriga, oxirgisi boshiga)
davlatlar.reverse()
print("Ortidan boshlab ro'yxat:", davlatlar)

# Davlatlarni yana alifbo tartibida chiqaramiz (asl ro'yxatdan mustaqil)
print("Alifbo bo'yicha tartiblangan ro'yxat:", sorted(davlatlar))

# Davlatlarni alifboga teskari tartibda chiqaramiz
print("Alifboga teskari tartibda ro'yxat:", sorted(davlatlar, reverse=True))


# 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini hosil qilamiz
# range(120, 1201, 2) -> 120 dan boshlaydi, 1200 gacha boradi, har safar 2 ga oshadi
juft_sonlar = list(range(120, 1201, 2))
print("Juft sonlar ro'yxati:", juft_sonlar)

# Juft sonlar yig'indisini hisoblaymiz
yigindi = sum(juft_sonlar)
print("Sonlar yig'indisi:", yigindi)

# Eng katta va eng kichik sonlarni topamiz
eng_katta = max(juft_sonlar)
eng_kichik = min(juft_sonlar)

# Eng katta va eng kichik sonlar orasidagi farqni hisoblaymiz
ayirma = eng_katta - eng_kichik
print("Eng katta va eng kichik son o'rtasidagi ayirma:", ayirma)

# Ro'yxatda nechta element borligini aniqlaymiz
print("Elementlar soni:", len(juft_sonlar))

# Ro'yxatning boshidagi 20 ta elementni chiqaramiz
print("Ro'yxatning boshidan 20 ta qiymat:", juft_sonlar[:20])

# Ro'yxatning o'rtasidan 20 ta elementni chiqaramiz
# len(juft_sonlar)//2 -> ro'yxat markazidagi indeks
# undan 10 ta oldin va 10 ta keyin elementlarni olamiz
print("Ro'yxatning o'rtasidan 20 ta qiymat:", juft_sonlar[len(juft_sonlar)//2-10 : len(juft_sonlar)//2+10])

# Ro'yxatning oxiridagi 20 ta elementni chiqaramiz
print("Ro'yxatning oxiridan 20 ta qiymat:", juft_sonlar[-20:])

# Taomlar ro'yxatini yaratamiz
taomlar = ["osh", "shashlik", "manti", "lag'mon", "somsa"]

# Taomlar ro'yxatini ekranga chiqaramiz
print("Taomlar ro'yxati:", taomlar)








