import tkinter as tk
import time

class StopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("스톱워치")

        self.running = False
        self.start_time = 0
        self.elapsed_time = 0

        self.time_label = tk.Label(root, text="0:00:00.000", font=("Helvetica", 48))
        self.time_label.pack(pady=20)

        self.start_button = tk.Button(root, text="시작", command=self.start)
        self.start_button.pack(side="left", padx=10)

        self.stop_button = tk.Button(root, text="중지", command=self.stop)
        self.stop_button.pack(side="left", padx=10)

        self.reset_button = tk.Button(root, text="리셋", command=self.reset)
        self.reset_button.pack(side="left", padx=10)

        self.lap_button = tk.Button(root, text="랩", command=self.lap)
        self.lap_button.pack(side="left", padx=10)

        self.lap_times = []
        self.lap_listbox = tk.Listbox(root, font=("Helvetica", 16), width=20, height=10)
        self.lap_listbox.pack(pady=10)

        self.update_time()

    def update_time(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time

        minutes = int(self.elapsed_time // 60)
        seconds = int(self.elapsed_time % 60)
        milliseconds = int((self.elapsed_time % 1) * 1000)

        time_str = f"{minutes}:{seconds:02d}.{milliseconds:03d}"
        self.time_label.config(text=time_str)

        self.root.after(100, self.update_time)

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time()

    def stop(self):
        if self.running:
            self.running = False

    def reset(self):
        self.running = False
        self.elapsed_time = 0
        self.lap_times = []
        self.lap_listbox.delete(0, tk.END)

    def lap(self):
        if self.running:
            self.lap_times.append(self.elapsed_time)
            lap_str = f"Lap {len(self.lap_times)}: {int(self.elapsed_time // 60)}:{self.elapsed_time % 60:.3f}"
            self.lap_listbox.insert(tk.END, lap_str)

if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()
