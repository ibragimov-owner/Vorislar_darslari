import tkinter as tk
from tkinter import font

class ModernCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🧮 Neon Kalkulyator")
        self.geometry("340x500")
        self.resizable(False, False)
        self.attributes("-topmost", True)
        self.configure(bg="#0d0d1a")

        self.expression = ""
        self.display_var = tk.StringVar()

        # Shriftlar
        self.display_font = font.Font(family="Consolas", size=26, weight="bold")
        self.btn_font = font.Font(size=14, weight="bold")

        # Displey
        display = tk.Entry(
            self,
            textvariable=self.display_var,
            font=self.display_font,
            bg="#191933",
            fg="#00ffcc",
            justify="right",
            bd=0,
            relief="flat",
        )
        display.pack(fill="x", padx=15, pady=20, ipady=15)
        display.focus_set()

        # Tugmalar
        buttons = [
            ["C", "←", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["±", "0", ".", "="],
        ]

        # Ranglar
        self.colors = {
            "num": "#2a2a4a",
            "op": "#0066ff",
            "sp": "#ff0055",
            "eq": "#00cc88",
        }

        frame = tk.Frame(self, bg="#0d0d1a")
        frame.pack()

        for r, row in enumerate(buttons):
            for c, char in enumerate(row):
                color = (
                    self.colors["num"]
                    if char in "0123456789."
                    else self.colors["op"]
                    if char in ["+", "-", "*", "/", "%"]
                    else self.colors["eq"]
                    if char == "="
                    else self.colors["sp"]
                )

                btn = tk.Button(
                    frame,
                    text=char,
                    font=self.btn_font,
                    fg="white",
                    bg=color,
                    activebackground="#333366",
                    activeforeground="#00ffcc",
                    bd=0,
                    width=6,
                    height=2,
                    relief="flat",
                    command=lambda ch=char: self.on_click(ch),
                )
                btn.grid(row=r, column=c, padx=6, pady=6, sticky="nsew")

        for i in range(4):
            frame.columnconfigure(i, weight=1)

        # 🔹 Klaviatura boshqaruvlarini bog‘laymiz
        self.bind("<Return>", lambda e: self.calculate())  # Enter
        self.bind("<BackSpace>", lambda e: self.backspace())  # Backspace
        self.bind("<Escape>", lambda e: self.clear())  # Esc
        for key in "0123456789+-*/.%":
            self.bind(key, lambda e, ch=key: self.key_input(ch))

    def key_input(self, ch):
        """Klaviaturadan raqam va belgi bosilganda"""
        if self.expression and self.expression[-1] in "+-*/" and ch in "+-*/":
            self.expression = self.expression[:-1] + ch
        else:
            self.expression += ch
        self.display_var.set(self.expression)

    def on_click(self, ch):
        if ch == "C":
            self.clear()
        elif ch == "←":
            self.backspace()
        elif ch == "=":
            self.calculate()
        elif ch == "±":
            self.toggle_sign()
        elif ch == "%":
            self.percent()
        else:
            if self.expression and self.expression[-1] in "+-*/" and ch in "+-*/":
                self.expression = self.expression[:-1] + ch
            else:
                self.expression += str(ch)
            self.display_var.set(self.expression)

    def clear(self):
        self.expression = ""
        self.display_var.set("")

    def backspace(self):
        self.expression = self.expression[:-1]
        self.display_var.set(self.expression)

    def safe_eval(self, expr):
        try:
            return eval(expr)
        except Exception:
            return None

    def calculate(self):
        if not self.expression:
            return
        while self.expression and self.expression[-1] in "+-*/.":
            self.expression = self.expression[:-1]

        expr = self.expression.replace("%", "/100")
        result = self.safe_eval(expr)

        if result is None:
            self.display_var.set("0")
            self.expression = ""
        else:
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self.expression = str(result)
            self.display_var.set(self.expression)

    def toggle_sign(self):
        val = self.safe_eval(self.expression)
        if val is not None:
            val = -val
            self.expression = str(val)
            self.display_var.set(self.expression)

    def percent(self):
        val = self.safe_eval(self.expression)
        if val is not None:
            val = val / 100
            self.expression = str(val)
            self.display_var.set(self.expression)


if __name__ == "__main__":
    app = ModernCalculator()
    app.mainloop()