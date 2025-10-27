import time, random

text = "python pro is coding speed"
print("Type this:", text)
input("Boshlash uchun Enter...")
start = time.time()
typed = input()
end = time.time()

ai_time = len(text) * 0.12 + random.uniform(-0.5, 0.8)  # AI tezligi
player_time = end - start

print(f"Your time: {player_time:.2f}s | AI time: {ai_time:.2f}s")
if player_time < ai_time:
    print("You beat the AI! 🏆")
else:
    print("AI won this time 😅")
