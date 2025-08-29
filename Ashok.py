import tkinter as tk
from datetime import datetime
import time
import threading
from tkinter import messagebox

# ----------------------
# Main Clock + Alarm App
# ----------------------
class ClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clock with Alarm & Reminder")

        # Clock label
        self.time_label = tk.Label(root, font=("Segoe UI", 48), fg="blue")
        self.time_label.pack(pady=20)

        # Date label
        self.date_label = tk.Label(root, font=("Segoe UI", 18))
        self.date_label.pack(pady=5)

        # Alarm input
        self.alarm_time_var = tk.StringVar()
        tk.Label(root, text="Set Alarm (HH:MM:SS, 24hr)").pack()
        tk.Entry(root, textvariable=self.alarm_time_var).pack()

        # Reminder input
        self.reminder_msg_var = tk.StringVar()
        tk.Label(root, text="Reminder Message").pack()
        tk.Entry(root, textvariable=self.reminder_msg_var).pack()

        # Button
        tk.Button(root, text="Set Alarm", command=self.set_alarm).pack(pady=10)

        self.alarm_set = False
        self.alarm_time = None
        self.reminder_msg = ""

        # Start clock update
        self.update_clock()

    # ----------------------
    # Clock Update
    # ----------------------
    def update_clock(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_date = now.strftime("%A, %d %B %Y")

        self.time_label.config(text=current_time)
        self.date_label.config(text=current_date)

        if self.alarm_set and current_time == self.alarm_time:
            self.trigger_alarm()

        self.root.after(1000, self.update_clock)

    # ----------------------
    # Set Alarm
    # ----------------------
    def set_alarm(self):
        self.alarm_time = self.alarm_time_var.get().strip()
        self.reminder_msg = self.reminder_msg_var.get().strip()

        if self.alarm_time:
            self.alarm_set = True
            messagebox.showinfo("Alarm Set", f"⏰ Alarm set for {self.alarm_time}\n📌 Reminder: {self.reminder_msg}")
        else:
            messagebox.showerror("Error", "Please enter alarm time!")

    # ----------------------
    # Trigger Alarm
    # ----------------------
    def trigger_alarm(self):
        self.alarm_set = False  # reset after ringing
        threading.Thread(target=self.ring).start()

    def ring(self):
        for _ in range(5):  # beep 5 times
            print("\a")  # system beep
            time.sleep(1)
        messagebox.showinfo("Alarm", f"⏰ Time's up!\n📌 {self.reminder_msg}")

# ----------------------
# Run App
# ----------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = ClockApp(root)
    root.mainloop()
