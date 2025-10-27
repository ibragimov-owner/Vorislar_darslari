import time

while True:
    vaqt = time.strftime("%H:%M:%S")
    print("⏰ Hozirgi vaqt:", vaqt, end="\r")
    time.sleep(1)
