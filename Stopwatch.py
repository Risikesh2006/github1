import tkinter as tk
import time

def start():
    global running, start_time
    if not running:
        running = True
        start_time = time.time() - elapsed_time
        update_timer()

def stop():
    global running, elapsed_time
    if running:
        running = False
        elapsed_time = time.time() - start_time

def reset():
    global running, elapsed_time
    running = False
    elapsed_time = 0
    time_label.config(text="00:00:00")

def update_timer():
    if running:
        current_time = time.time() - start_time
        mins, secs = divmod(int(current_time), 60)
        hours, mins = divmod(mins, 60)
        time_label.config(text=f"{hours:02}:{mins:02}:{secs:02}")
        root.after(1000, update_timer)

# Initialize variables
running = False
elapsed_time = 0

# Create main window
root = tk.Tk()
root.title("Stopwatch")
root.geometry("300x200")

time_label = tk.Label(root, text="00:00:00", font=("Arial", 30))
time_label.pack(pady=20)

start_button = tk.Button(root, text="Start", command=start)
start_button.pack(side=tk.LEFT, padx=10)

stop_button = tk.Button(root, text="Stop", command=stop)
stop_button.pack(side=tk.LEFT, padx=10)

reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.pack(side=tk.LEFT, padx=10)

root.mainloop()
