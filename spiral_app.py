import math
import tkinter as tk
from PIL import Image

IMAGE_PATH = "image_2d82c0.jpg"
WIDTH, HEIGHT = 800, 800

class SpiralAnimationApp:
    def __init__(self, root, image_path):
        self.root = root
        self.root.title("Spiral Image Animation - Sundas")
        self.root.geometry(f"{WIDTH}x{HEIGHT}")
        self.root.configure(bg="black")

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        try:
            img = Image.open(image_path).convert("L")
            img = img.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)
            self.image_data = img.load()
        except Exception as e:
            print(f"Error loading image: {e}")
            self.image_data = None

        self.max_theta = 50 * 2 * math.pi
        self.current_theta = 0.0
        self.step = 0.5
        self.animate_spiral()

    def animate_spiral(self):
        if self.current_theta < self.max_theta and self.image_data:
            batch_end = min(self.current_theta + 15.0, self.max_theta)
            cx, cy = WIDTH / 2, HEIGHT / 2

            while self.current_theta < batch_end:
                a = 2.2
                r = a * self.current_theta
                x = cx + r * math.cos(self.current_theta)
                y = cy + r * math.sin(self.current_theta)

                if 0 <= int(x) < WIDTH and 0 <= int(y) < HEIGHT:
                    brightness = self.image_data[int(x), int(y)]
                    if brightness < 200:
                        size = max(1, int((255 - brightness) / 60))
                        self.canvas.create_oval(x, y, x + size, y + size, fill="white", outline="")

                self.current_theta += self.step

            self.root.after(10, self.animate_spiral)

if __name__ == "__main__":
    root = tk.Tk()
    app = SpiralAnimationApp(root, IMAGE_PATH)
    root.mainloop()
