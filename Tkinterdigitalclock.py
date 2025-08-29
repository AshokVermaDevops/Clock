# digital_clock_tk.py
import tkinter as tk
import time

root = tk.Tk()
root.title("Digital Clock")

label = tk.Label(root, font=("Segoe UI", 48), padx=20, pady=10)
label.pack()

def tick():
    label.config(text=time.strftime("%H:%M:%S"))
    label.after(200, tick)  # update ~5x per second for smoothness

tick()
root.mainloop()
