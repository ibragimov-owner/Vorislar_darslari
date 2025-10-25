"""
   25.10.2025
   Methodlar bilan ishlash. Methodlar va Function lar bilan ishlash
   method(sort()) 
   function(sum ), sorted(), max(), min(), list()
   Ro'yxattlardan nusxa olish
   Tuple() o'zgarmas ro'yxat
"""


# davlatlar = ["Ozbekiston", "AQSH", "Rossiya", "Xitoy", "Turkiya"]
# davlatlar.sort()
# print(davlatlar)

# mashinalar = list(("bmw", "audi", "Ferrari", "mersedes"))
# mashinalar.sort()
# print(mashinalar)

# sonlar = list((0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
# sonlar.sort()
# print(sonlar)

# son = list((2, 9, 7, 5, 3, 1, 4, 6, 8, 0))
# son.sort(reverse=True)
# print(son)


# sonlar1 = list(range(0, 21))
# print(sonlar1)

# sonlar2 = list(range(1, 30, 2))
# print(sonlar2)

# sonlar3 = list(range(-8, 30, 3))
# print(sonlar3)
# print(len(sonlar3))

# sonlar4 = max((30, 0, -3, 15, 7, 22, 19))
# print(sonlar4)

# sonlar5 = min(30, 0, -3, 15, 7, 22, 19)
# print(sonlar5)

# sonlar6 = sum((30, 0, 3, 15, 7, 22, 19))
# print(sonlar6)




davlatlar = ["Ozbekiston", "AQSH", "Rossiya", "Xitoy", "Turkiya"]

country = davlatlar

print("davlatlar nomli ro'yxat", davlatlar)
print("country nomli ro'yxat", country)

country.insert(0, "Angliya")
print(country)

print(davlatlar)
print(country)

toqson = list(range(1, 20, 2))
print("asl ko'rinishi:", toqson)
print("1 dan 7 gacha :", toqson[0:4])
print(toqson [:])












