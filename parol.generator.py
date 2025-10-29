"""
27.10.2025
Parol generatori dasturi
Tavsif: Ushbu dastur foydalanuvchidan parol uzunligini so'raydi va tasodifiy parol yaratadi.
Parol harflar, raqamlar va maxsus belgilarni o'z ichiga oladi.

Qoidalar:
1. Foydalanuvchi parol uzunligini kiritadi.
2. Dastur tasodifiy parol yaratadi va uni foydalanuvchiga ko'rsatadi.
"""


import random
import string

uzunlik = int(input("Parol uzunligini kiriting: "))
belgilar = string.ascii_letters + string.digits + string.punctuation
parol = "".join(random.choice(belgilar) for i in range(uzunlik))

print("🔐 Sizning parolingiz:", parol)
