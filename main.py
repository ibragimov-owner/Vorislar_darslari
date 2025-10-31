"""
25.10.2025
Bu har xil parolni buzish usullarini sinab ko'rish uchun qulay interfeysni taqdim etadi.

"""

import tkinter as tk
from tkinter import ttk, messagebox
import itertools
import string
import time
import threading
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation

class PasswordCrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Password Cracker - Enhanced Edition")
        self.root.geometry("900x750")
        self.root.configure(bg="#1a1a2e")
        
        # Variables
        self.attempt_count = 0
        self.found = False
        self.is_running = False
        self.start_time = 0
        self.attempts_data = []
        self.time_data = []
        self.cracking_thread = None
        
        # Statistics
        self.attempts_per_second = 0
        self.estimated_time = "Calculating..."
        
        self.setup_ui()
        
    def setup_ui(self):
        # Title Frame
        title_frame = tk.Frame(self.root, bg="#16213e", relief="raised", bd=3)
        title_frame.pack(fill="x", padx=10, pady=10)
        
        title_label = tk.Label(title_frame, text="🔐 Advanced Password Cracker", 
                              font=("Helvetica", 20, "bold"), 
                              bg="#16213e", fg="#00d4ff")
        title_label.pack(pady=10)
        
        # Input Frame
        input_frame = tk.Frame(self.root, bg="#1a1a2e")
        input_frame.pack(pady=10)
        
        tk.Label(input_frame, text="Target Password:", 
                font=("Helvetica", 12), bg="#1a1a2e", fg="white").grid(row=0, column=0, padx=5)
        
        self.password_entry = tk.Entry(input_frame, show="*", width=25, 
                                      font=("Helvetica", 12), relief="solid", bd=2)
        self.password_entry.grid(row=0, column=1, padx=5)
        
        self.show_password_var = tk.BooleanVar()
        show_check = tk.Checkbutton(input_frame, text="Show", variable=self.show_password_var,
                                   command=self.toggle_password_visibility,
                                   bg="#1a1a2e", fg="white", selectcolor="#16213e")
        show_check.grid(row=0, column=2, padx=5)
        
        # Charset Selection
        charset_frame = tk.Frame(self.root, bg="#1a1a2e")
        charset_frame.pack(pady=5)
        
        tk.Label(charset_frame, text="Character Set:", 
                font=("Helvetica", 11), bg="#1a1a2e", fg="white").pack(side="left", padx=5)
        
        self.lowercase_var = tk.BooleanVar(value=True)
        self.uppercase_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.special_var = tk.BooleanVar(value=False)
        
        tk.Checkbutton(charset_frame, text="a-z", variable=self.lowercase_var,
                      bg="#1a1a2e", fg="white", selectcolor="#16213e").pack(side="left")
        tk.Checkbutton(charset_frame, text="A-Z", variable=self.uppercase_var,
                      bg="#1a1a2e", fg="white", selectcolor="#16213e").pack(side="left")
        tk.Checkbutton(charset_frame, text="0-9", variable=self.digits_var,
                      bg="#1a1a2e", fg="white", selectcolor="#16213e").pack(side="left")
        tk.Checkbutton(charset_frame, text="!@#$%", variable=self.special_var,
                      bg="#1a1a2e", fg="white", selectcolor="#16213e").pack(side="left")
        
        # Max Length
        length_frame = tk.Frame(self.root, bg="#1a1a2e")
        length_frame.pack(pady=5)
        
        tk.Label(length_frame, text="Max Length:", 
                font=("Helvetica", 11), bg="#1a1a2e", fg="white").pack(side="left", padx=5)
        
        self.max_length_var = tk.IntVar(value=6)
        self.length_spinbox = tk.Spinbox(length_frame, from_=1, to=10, 
                                        textvariable=self.max_length_var,
                                        width=5, font=("Helvetica", 11))
        self.length_spinbox.pack(side="left")
        
        # Control Buttons
        button_frame = tk.Frame(self.root, bg="#1a1a2e")
        button_frame.pack(pady=10)
        
        self.start_button = tk.Button(button_frame, text="▶ Start Attack", 
                                      command=self.start_bruteforce,
                                      bg="#00d4ff", fg="black", 
                                      font=("Helvetica", 12, "bold"),
                                      width=15, relief="raised", bd=3,
                                      cursor="hand2")
        self.start_button.grid(row=0, column=0, padx=5)
        
        self.stop_button = tk.Button(button_frame, text="⏸ Stop", 
                                     command=self.stop_bruteforce,
                                     bg="#ff4757", fg="white", 
                                     font=("Helvetica", 12, "bold"),
                                     width=15, relief="raised", bd=3,
                                     cursor="hand2", state="disabled")
        self.stop_button.grid(row=0, column=1, padx=5)
        
        # Phone Screen Display
        phone_frame = tk.Frame(self.root, bg="#0f3460", bd=5, relief="raised")
        phone_frame.pack(pady=10)
        
        tk.Label(phone_frame, text="Current Attempt", 
                font=("Helvetica", 10, "bold"), bg="#0f3460", fg="#00d4ff").pack()
        
        self.phone_screen_var = tk.StringVar(value="Waiting...")
        phone_screen = tk.Label(phone_frame, textvariable=self.phone_screen_var, 
                               font=("Courier", 16, "bold"), 
                               bg="#000000", fg="#00ff00", 
                               width=20, height=3, relief="sunken", bd=3)
        phone_screen.pack(padx=15, pady=10)
        
        # Statistics Frame
        stats_frame = tk.Frame(self.root, bg="#16213e", relief="raised", bd=3)
        stats_frame.pack(fill="x", padx=10, pady=5)
        
        self.stats_labels = {}
        stats_info = [
            ("Attempts", "0"),
            ("Speed", "0 attempts/sec"),
            ("Elapsed Time", "0s"),
            ("Status", "Idle")
        ]
        
        for i, (label, value) in enumerate(stats_info):
            tk.Label(stats_frame, text=f"{label}:", 
                    font=("Helvetica", 10, "bold"), 
                    bg="#16213e", fg="#00d4ff").grid(row=i//2, column=(i%2)*2, 
                                                     sticky="w", padx=10, pady=5)
            
            var = tk.StringVar(value=value)
            self.stats_labels[label] = var
            tk.Label(stats_frame, textvariable=var, 
                    font=("Helvetica", 10), 
                    bg="#16213e", fg="white").grid(row=i//2, column=(i%2)*2+1, 
                                                   sticky="w", padx=10, pady=5)
        
        # Progress Bar
        self.progress = ttk.Progressbar(self.root, mode='indeterminate', length=400)
        self.progress.pack(pady=5)
        
        # Result Label
        self.result_label = tk.Label(self.root, text="", 
                                     font=("Helvetica", 12, "bold"), 
                                     bg="#1a1a2e", fg="#00ff00")
        self.result_label.pack(pady=5)
        
        # Graph
        self.fig, self.ax = plt.subplots(figsize=(7, 3), facecolor="#1a1a2e")
        self.ax.set_facecolor("#0f3460")
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(pady=10)
        
        self.setup_graph()
    
    def setup_graph(self):
        self.ax.clear()
        self.ax.set_xlabel("Time (seconds)", color="white", fontsize=10)
        self.ax.set_ylabel("Attempts", color="white", fontsize=10)
        self.ax.set_title("Real-time Cracking Progress", color="#00d4ff", fontsize=12, fontweight="bold")
        self.ax.tick_params(colors="white")
        self.ax.grid(True, alpha=0.3, color="#00d4ff")
        self.canvas.draw()
    
    def toggle_password_visibility(self):
        if self.show_password_var.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")
    
    def get_charset(self):
        charset = ""
        if self.lowercase_var.get():
            charset += string.ascii_lowercase
        if self.uppercase_var.get():
            charset += string.ascii_uppercase
        if self.digits_var.get():
            charset += string.digits
        if self.special_var.get():
            charset += string.punctuation
        return charset
    
    def start_bruteforce(self):
        password = self.password_entry.get()
        
        if not password:
            messagebox.showwarning("Error", "Please enter a password!")
            return
        
        charset = self.get_charset()
        if not charset:
            messagebox.showwarning("Error", "Please select at least one character set!")
            return
        
        self.attempt_count = 0
        self.found = False
        self.is_running = True
        self.attempts_data.clear()
        self.time_data.clear()
        self.start_time = time.time()
        
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        self.progress.start(10)
        
        self.stats_labels["Status"].set("Running...")
        self.result_label.config(text="", fg="#00ff00")
        
        self.cracking_thread = threading.Thread(target=self.bruteforce_worker, 
                                               args=(password, charset), 
                                               daemon=True)
        self.cracking_thread.start()
        
        self.update_ui()
    
    def stop_bruteforce(self):
        self.is_running = False
        self.stats_labels["Status"].set("Stopped")
        self.result_label.config(text="Attack stopped by user", fg="#ff4757")
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        self.progress.stop()
    
    def bruteforce_worker(self, password, charset):
        max_length = self.max_length_var.get()
        
        for length in range(1, max_length + 1):
            if not self.is_running:
                return
                
            for attempt_tuple in itertools.product(charset, repeat=length):
                if not self.is_running:
                    return
                
                attempt = ''.join(attempt_tuple)
                self.attempt_count += 1
                
                if attempt == password:
                    self.found = True
                    self.is_running = False
                    self.root.after(0, self.password_found, attempt)
                    return
        
        self.root.after(0, self.password_not_found)
    
    def password_found(self, password):
        elapsed = time.time() - self.start_time
        self.result_label.config(text=f"✓ Password Found: {password}", fg="#00ff00")
        self.stats_labels["Status"].set("Success!")
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        self.progress.stop()
        messagebox.showinfo("Success", 
                           f"Password cracked!\n\nPassword: {password}\n"
                           f"Attempts: {self.attempt_count:,}\n"
                           f"Time: {elapsed:.2f}s")
    
    def password_not_found(self):
        self.result_label.config(text="✗ Password not found in search space", fg="#ff4757")
        self.stats_labels["Status"].set("Failed")
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        self.progress.stop()
    
    def update_ui(self):
        if self.is_running:
            elapsed = time.time() - self.start_time
            
            # Update statistics
            self.stats_labels["Attempts"].set(f"{self.attempt_count:,}")
            
            if elapsed > 0:
                speed = self.attempt_count / elapsed
                self.stats_labels["Speed"].set(f"{speed:,.0f} attempts/sec")
            
            self.stats_labels["Elapsed Time"].set(f"{elapsed:.1f}s")
            
            # Update graph every 1000 attempts
            if self.attempt_count % 1000 == 0 and elapsed > 0:
                self.attempts_data.append(self.attempt_count)
                self.time_data.append(elapsed)
                self.update_graph()
            
            self.root.after(100, self.update_ui)
    
    def update_graph(self):
        if len(self.time_data) > 0:
            self.ax.clear()
            self.ax.plot(self.time_data, self.attempts_data, 
                        color="#00d4ff", linewidth=2, marker='o', markersize=4)
            self.ax.set_xlabel("Time (seconds)", color="white", fontsize=10)
            self.ax.set_ylabel("Attempts", color="white", fontsize=10)
            self.ax.set_title("Real-time Cracking Progress", 
                            color="#00d4ff", fontsize=12, fontweight="bold")
            self.ax.tick_params(colors="white")
            self.ax.grid(True, alpha=0.3, color="#00d4ff")
            self.canvas.draw()

def main():
    root = tk.Tk()
    app = PasswordCrackerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()






    