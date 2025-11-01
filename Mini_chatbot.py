"""Mini Markov chatbot — kichik trening faylidan hazil javoblar chiqaradi

markov_chat.py

Kod quyidagicha:"""
import random
from collections import defaultdict

def build_chain(words, n=2):
    chain = defaultdict(list)
    for i in range(len(words)-n):
        key = tuple(words[i:i+n])
        chain[key].append(words[i+n])
    return chain

with open("small_corpus.txt", encoding="utf-8") as f:
    text = f.read().replace("\n", " ").split()
chain = build_chain(text, n=2)

def gen(start=None, length=15):
    if not start:
        start = random.choice(list(chain.keys()))
    output = list(start)
    for _ in range(length):
        key = tuple(output[-2:])
        nxt = random.choice(chain.get(key, list(chain.keys())[0]))
        output.append(nxt)
    return " ".join(output)

print("Markov-chat - chiqish uchun CTRL+C bosing")
try:
    while True:
        user = input("Siz: ")
        if user.strip() == "":
            print("Bot:", gen())
        else:
            # reply starts with last two words of user if available
            parts = user.split()
            start = tuple(parts[-2:]) if len(parts) >= 2 else None
            print("Bot:", gen(start))
except KeyboardInterrupt:
    print("\nXayr!")