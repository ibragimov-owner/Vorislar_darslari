# Pomodoro timer (Tkinter) — ishlash/ta’til sikli

# omodoro texnikasi, bu kod 25 daqiqalik ishlash va 5 daqiqalik ta’til uchun oddiy timer yaratadi.

# Mini GUI bilan fokus tizimi.

# Tkinter kutubxonasidan foydalaniladi.

# Har bir daqiqani hisoblash uchun threading va time kutubxonalaridan foydalaniladi.

# pomodoro_timer.py

# Kod quyidagicha:

import tkinter as tk
import time, threading

def start_timer():
    def run():
        t = 25*60
        while t:
            mins, secs = divmod(t, 60)
            label.config(text=f"{mins:02d}:{secs:02d}")
            time.sleep(1)
            t -= 1
        label.config(text="Break time!")
    threading.Thread(target=run, daemon=True).start()

root = tk.Tk()
root.title("Pomodoro")
label = tk.Label(root, text="25:00", font=("Arial", 40))
label.pack(padx=20, pady=20)
tk.Button(root, text="Start", command=start_timer).pack()
root.mainloop()
