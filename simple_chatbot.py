"""
28.10.2025

simple_chatbot.py

bu sodda matn asosidagi chatbot dasturi

foydalanuvchi bilan oddiy suhbatlashadi

turli savollarga javob beradi

javoblar lug'atida saqlanadi

tasodifiy javob tanlash uchun random kutubxonasi ishlatiladi

dastur foydalanuvchi "chiq" deb yozganda to'xtaydi
"""

import random

javoblar = {
    "salom": ["Salom!", "Assalomu alaykum!", "Salom, yaxshimisiz?"],
    "qandaysan": ["Zo‘rman, sizchi?", "Yaxshi, rahmat!", "Har doimgidek ajoyib!"],
    "isming": ["Meni SimpleChatBot deb atashadi.", "Ismim Simple chat Bot."],
    "nima qilayapsan": ["Siz bilan suhbatlashyapman.", "Kod yozayapman 😊"],
    "xayr": ["Xayr!", "Ko‘rishguncha!", "Salomat bo‘ling!"]
}

print("ChatBot: Salom! Suhbatni boshlaymiz (chiqish uchun 'chiq' yozing).")

while True:
    user = input("Siz: ").lower()
    if user == "chiq":
        print("ChatBot: Xayr!")
        break
    javob = None
    for kalit in javoblar:
        if kalit in user:
            javob = random.choice(javoblar[kalit])
            break
    if not javob:
        javob = random.choice(["Hmm...", "Tushunmadim 🤔", "Qiziq fikr!"])
    print("ChatBot:", javob)