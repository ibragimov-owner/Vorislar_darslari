# 1. Do‘stlar ro‘yxatini yaratamiz
dostlar = ["Ali", "Kamolbek", "Umid"]

# Har bir do‘st uchun xabar chiqaramiz
print(f"Salom {dostlar[0]}, bugun choyxona bormi?")
print(f"{dostlar[1]}, choyxonaga boramizmi?")
print(f"{dostlar[2]}, kechga film ko'ramizmi?")

print("\n---\n")

# 2. Sonlar ro‘yxatini yaratamiz
sonlar = [12, -5, 7.5, 0, 3, -8]

# Arifmetik amallar
print("Barcha sonlar:", sonlar)
print("Birinchi + ikkinchi son:", sonlar[0] + sonlar[1])
print("Oxirgi son kvadrati:", sonlar[-1] ** 2)

# Ba'zilarini o'zgartiramiz
sonlar[1] = 15
sonlar[3] = 10
print("O‘zgartirilgan sonlar:", sonlar)

# Elementlarni almashtiramiz
sonlar[0], sonlar[-1] = sonlar[-1], sonlar[0]
print("Almashtirilgan ro‘yxat:", sonlar)

print("\n---\n")

# 3. Tarixiy va zamonaviy shaxslar ro‘yxati
t_shaxslar = ["Imom Buxoriy", "Amir Temur", "Beruniy"]
z_shaxslar = ["Bill Gates", "Elon Musk", "Cristiano Ronaldo"]

# Har biridan bittadan sug‘urib olish (pop)
t_shaxs = t_shaxslar.pop(0)
z_shaxs = z_shaxslar.pop(1)

print(f"Men tarixiy shaxslardan {t_shaxs} bilan, zamonaviy shaxslardan esa {z_shaxs} bilan suhbat qilishni istar edim.")

print("\n---\n")

# 4. Mehmonlar ro‘yxati
friends = []
friends.append("Umid")
friends.append("Kamolbek")
friends.append("Elbek")
friends.append("Boboxon")
friends.append("Ixtiyor")
friends.append("Baxtiyor")

print("Mehmonlar ro‘yxati:", friends)

# Mehmon bo‘la olmaydigan odamni o‘chiramiz
friends.remove("Umid")
print("Yangilangan mehmonlar:", friends)

# Ro‘yxatning boshiga, o‘rtasiga va oxiriga yangi mehmon qo‘shamiz
friends.insert(0, "Zuhriddin")
friends.insert(3, "Xolbek")
friends.append("Ilyosbek")
print("Yangi mehmonlar bilan ro‘yxat:", friends)

print("\n---\n")

# 5. Kela olgan mehmonlarni yangi ro‘yxatga ko‘chirish
mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(2))
mehmonlar.append(friends.pop(-1))

print("Kela olgan mehmonlar:", mehmonlar)
print("Kelolmaganlar:", friends)
