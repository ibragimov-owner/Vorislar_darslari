# Mini quiz dasturi JSON formatida saqlangan savollar bilan ishlaydi.

# Mini Quiz (JSON bilan) — fayldan savollar o‘qib, hisoblaydi.

# Istalgan savol qo‘shiladi.


import json

data = [
    {"q":"O‘zbekiston poytaxti?","a":"toshkent"},
    {"q":"2+2 = ?","a":"4"}
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
