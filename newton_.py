import tkinter as tk

class NewtonProject:
    def __init__(self, root):
        self.root = root
        self.root.title("뉴턴의 운동 법칙 시뮬레이션")

        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack()

        self.object1 = self.canvas.create_oval(50, 200, 100, 250, fill="blue")
        self.object2 = self.canvas.create_oval(500, 200, 550, 250, fill="red")
        self.velocity1 = 0
        self.velocity2 = 0
        self.position1 = 50
        self.position2 = 500
        self.mass1 = 1
        self.mass2 = 2
        self.force = 0
        self.time = 0
        self.running = False

        self.start_button = tk.Button(root, text="시작", command=self.toggle_simulation)
        self.start_button.pack(side="left", padx=10)

        self.reset_button = tk.Button(root, text="리셋", command=self.reset_simulation)
        self.reset_button.pack(side="left", padx=10)

        self.force_scale = tk.Scale(root, label="힘의 크기", from_=-1, to=1, orient="horizontal", resolution=0.01)
        self.force_scale.pack(side="left", padx=10)

        self.initial_state = {
            "velocity1": self.velocity1,
            "velocity2": self.velocity2,
            "position1": self.position1,
            "position2": self.position2
        }

        self.update()

    def toggle_simulation(self):
        self.running = not self.running

    def reset_simulation(self):
        self.velocity1 = self.initial_state["velocity1"]
        self.velocity2 = self.initial_state["velocity2"]
        self.position1 = self.initial_state["position1"]
        self.position2 = self.initial_state["position2"]
        self.force = 0
        self.running = False

    def update(self):
        if self.running:
            distance = self.position2 - self.position1
            self.force = self.force_scale.get() * distance  # 물체 간의 힘 (간단화된 모델)
            acceleration1 = self.force / self.mass1
            acceleration2 = -self.force / self.mass2

            self.velocity1 += acceleration1
            self.velocity2 += acceleration2

            self.position1 += self.velocity1
            self.position2 += self.velocity2

            if self.position1 >= 550:
                self.velocity1 = -self.velocity1
                self.position1 = 550
            if self.position2 <= 50:
                self.velocity2 = -self.velocity2
                self.position2 = 50

            self.canvas.coords(self.object1, self.position1, 200, self.position1 + 50, 250)
            self.canvas.coords(self.object2, self.position2, 200, self.position2 + 50, 250)
            self.time += 1

        self.root.after(50, self.update)

if __name__ == "__main__":
    root = tk.Tk()
    app = NewtonProject(root)
    root.mainloop()
