"""
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

davlatlar = ["Ozbekiston", "AQSH", "Rossiya", "Xitoy", "Turkiya"]
print(davlatlar)
print("Ro'yxat uzunligi:", len(davlatlar))
print("Tartiblangan ro'yxat:", sorted(davlatlar))
print("Teskari tartiblangan ro'yxat:", sorted(davlatlar, reverse=True))
print("Asl ro'yxat:", davlatlar)
davlatlar.reverse()
print("Ortidan boshlab ro'yxat:", davlatlar)
print("Alifbo bo'yicha tartiblangan ro'yxat:", sorted(davlatlar))
print("Alifboga teskari tartibda ro'yxat:", sorted(davlatlar, reverse=True))
juft_sonlar = list(range(120, 1201, 2))
print("Juft sonlar ro'yxati:", juft_sonlar)
yigindi = sum(juft_sonlar)
print("Sonlar yig'indisi:", yigindi)      
eng_katta = max(juft_sonlar)
eng_kichik = min(juft_sonlar)
ayirma = eng_katta - eng_kichik
print("Eng katta va eng kichik son o'rtasidagi ayirma:", ayirma)
print("Elementlar soni:", len(juft_sonlar))
print("Ro'yxatning boshidan 20 ta qiymat:", juft_sonlar[:20])
print("Ro'yxatning o'rtasidan 20 ta qiymat:", juft_sonlar[len(juft_sonlar)//2-10:len(juft_sonlar)//2+10])
print("Ro'yxatning oxiridan 20 ta qiymat:", juft_sonlar[-20:])
taomlar = ["osh", "shashlik", "manti", "lag'mon", "somsa"]
print("Taomlar ro'yxati:", taomlar)




