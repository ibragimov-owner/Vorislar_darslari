"""
25.10.2025
Sun’iy intellektli chatbot (sodda versiya) 
Bu bot oddiy savollarga javob beradi.
"""
while True:
    savol = input("Siz: ").lower()
    if "salom" in savol:
        print("Bot: Salom! Yaxshimisan?")
    elif "yaxshi" in savol:
        print("Bot: Zo‘r! Men ham yaxshi man 😎")
    elif "isming" in savol:
         print("Bot: Zo‘r! Men ham yaxshi man 😎")
    elif "Bugun havo qanaqa" in savol:
        print("Bot: Issiq, taxminan 25 daraja!")
    elif "exit" in savol or "xayr" in savol:
        print("Bot: Xayr! 😊")
        break
    else:
        print("Bot: Buni tushunmadim...")
