import tkinter as tk
from datetime import datetime
from datetime import timedelta

class StopwatchApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Секундомер")

        self.is_running = False
        self.start_time = None

        self.label = tk.Label(master, text="0:00:00", font=("Helvetica", 48))
        self.label.pack(pady=20)

        self.start_button = tk.Button(master, text="Старт", command=self.start_stop)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(master, text="Сброс", command=self.reset)
        self.reset_button.pack(side=tk.RIGHT, padx=10)

        self.update()

    def start_stop(self):
        if self.is_running:
            self.is_running = False
        else:
            self.is_running = True
            self.start_time = datetime.now()

    def reset(self):
        self.is_running = False
        self.start_time = None

    def update(self):
        if self.is_running and self.start_time:
            elapsed_time = datetime.now() - self.start_time
            timer_str = str(timedelta(seconds=elapsed_time.seconds))
            self.label.config(text=timer_str)
        else:
            self.label.config(text="0:00:00")

        self.master.after(1000, self.update)

if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()
