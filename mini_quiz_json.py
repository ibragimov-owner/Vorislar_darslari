"""
25.10.2025

Mini quiz dasturi JSON formatida saqlangan savollar bilan ishlaydi.

Mini Quiz (JSON bilan) — fayldan savollar o‘qib, hisoblaydi.

Istalgan savol qo‘shiladi.
"""


import json

data = [
    {"q":"O‘zbekiston poytaxti?","a":"toshkent"},
    {"q":"2+2 = ?","a":"4"},
    {"q":"Python dasturlash tili kim tomonidan yaratilgan?","a":"guidovan rossum"},
    {"q":"Dunyoning eng baland cho'qqisi?","a":"everest"},
    {"q":"Olimpiada o'yinlari nechanchi yilda boshlangan?","a":"1896"},
    {"q":"Inson tanasidagi eng katta organ?","a":"teri"},
    {"q":"Yer qaysi sayyra atrofida aylanadi?","a":"quyosh"},
]
# agar fayl ishlatmoqchi bo'lsang: json.dump(data, open("q.json","w"))

score = 0
for item in data:
    ans = input(item["q"] + " ").strip().lower()
    if ans == item["a"]:
        print("To'g'ri")
        score += 1
    else:
        print("Noto'g'ri")
print("Final score:", score, "/", len(data))
