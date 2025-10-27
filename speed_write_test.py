import time, random

matnlar = [
    "hello world", "python is fun", "write faster baby", "salom dunyo",
    "machine learning basics", "never stop learning"
]
text = random.choice(matnlar)
print("Type this:", text)
input("Boshlash uchun Enter...")
start = time.time()
typed = input()
end = time.time()

if typed.strip() == text:
    wpm = len(text.split()) / ((end-start)/60)
    print(f"Good! Vaqt: {end-start:.2f}s | WPM: {wpm:.1f}")
else:
    print("Matn to‘liq mos kelmadi. Qayta urin.")
