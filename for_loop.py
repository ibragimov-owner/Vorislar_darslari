"""
01.11.2025
for loop sikl - sikl yaratishda ishlatiladigan eng asosiy konstruktsiyalardan biridir.
for loop yordamida biz ma'lum bir amalni yoki kod blokini takrorlashimiz mumkin.
Misol uchun, quyidagi kod 1 dan 5 gacha bo'lgan sonlarni konsolga chiqaradi:
for i in range(1, 6):
    print(i)
Bu kodda range(1, 6) funksiyasi 1 dan 5 gacha bo'lgan sonlar ketma-ketligini yaratadi va for loop har bir son uchun print(i) amalini bajaradi.
Natijada, quyidagi chiqish hosil bo'ladi:

1
2
3
4
5

for loop yordamida ro'yxatlar, lug'atlar va boshqa ma'lumot tuzilmalaridagi elementlar ustida ham ishlash mumkin.
"""

oquvchilar = ["Ali", "Vali", "Gulbahor", "Doston", "Madina"]

for ism in oquvchilar:
    print(f"assalomu alaykum xurmatli {ism.title} ishlar qanday?")  
    print(f"Yaxshi kun tilayman xurmatli {ism.title()} ")

# Bu kod for loop yordamida oquvchilar ro'yxatidagi har bir o'quvchi uchun salomlashish xabarini chiqaradi.
     

# print(f"assalomu alaykum xurmatli {oquvchilar[0]} ishlar qanday?")
# print(f"assalomu alaykum xurmatli {oquvchilar[1]} ishlar qanday?")
# print(f"assalomu alaykum xurmatli {oquvchilar[2]} ishlar qanday?")
# print(f"assalomu alaykum xurmatli {oquvchilar[3]} ishlar qanday?")
# print(f"assalomu alaykum xurmatli {oquvchilar[4]} ishlar qanday?")

# raqamlar = list((1, 2, 3, 4, 5, -8, 13, 21, 34, 55, 89, 69))
# for raqam in raqamlar:
#    print(f"{raqam} ning kvadrati {raqam**2} ga teng")
#    print(f"{raqam} ning kubi {raqam**3} ga teng")


# raqamlar = list(range(30, 91,))
# for raqam in raqamlar:
#     print(f"{raqam}  sonini toqqqizga bolganda {raqam / 9} ga teng")



raqamlar = list(range(27, 54, 7))
for raqam in raqamlar:
    print(f"{raqam}  tortinchi darajasi {raqam **4} ga teng")
    

natija = [f"{raqam} tortinchi darajasi {raqam ** 4} ga teng" for raqam in raqamlar]

print("\nRo‘yxat ko‘rinishida:")
print(natija)

    




