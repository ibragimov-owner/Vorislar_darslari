# Sun’iy intellektli chatbot (sodda versiya) 
# Bu bot oddiy savollarga javob beradi.

while True:
    savol = input("Siz: ").lower()
    if "salom" in savol:
        print("Bot: Salom! Yaxshimisan?")
    elif "yaxshi" in savol:
        print("Bot: Zo‘r! Men ham yaxshi man 😎")
    elif "isming" in savol:
        print("Bot: Meni PyBot deb atashadi!")
    elif "exit" in savol or "xayr" in savol:
        print("Bot: Xayr! 😊")
        break
    else:
        print("Bot: Buni tushunmadim...")
