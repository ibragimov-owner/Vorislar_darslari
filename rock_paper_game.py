import random

opts = ["rock","paper","scissors","lizard","spock"]
wins = {("scissors","paper"),("paper","rock"),("rock","lizard"),
        ("lizard","spock"),("spock","scissors"),("scissors","lizard"),
        ("lizard","paper"),("paper","spock"),("spock","rock"),("rock","scissors")}

score = {"player":0,"ai":0}
for _ in range(5):
    ai = random.choice(opts)
    p = input(f"Choose {opts}: ").lower()
    if p not in opts:
        print("Noto'g'ri tanlov.")
        continue
    print("AI:", ai)
    if p == ai:
        print("Draw")
    elif (p,ai) in wins:
        print("You win!")
        score["player"] += 1
    else:
        print("AI wins!")
        score["ai"] += 1
    print("Score:", score)
print("Final:", score)
