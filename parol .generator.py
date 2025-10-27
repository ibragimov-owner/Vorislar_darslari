import random
import string

uzunlik = int(input("Parol uzunligini kiriting: "))
belgilar = string.ascii_letters + string.digits + string.punctuation
parol = "".join(random.choice(belgilar) for i in range(uzunlik))

print("🔐 Sizning parolingiz:", parol)
