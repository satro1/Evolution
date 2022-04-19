
class Ball:
    def __init__(self, size, speed, color, width, height, canvas, tk):
        self.ball = canvas.create_oval(width//2, height//2, width//2 + size, height//2 + size, fill=color)
        canvas.pack()
        self.speed = speed
        self.speedx = speed
        self.speedy = speed
        self.canvas = canvas
        self.tk = tk
        self.width = width
        self.height = height
        self.movement()

    def movement(self):
        self.canvas.move(self.ball, self.speedx, self.speedy)
        pos = self.canvas.coords(self.ball)
        if pos[2] >= self.width or pos[0] <= 0:
            self.speedx *= -1
        if pos[3] >= self.height or pos[1] <= 0:
            self.speedy *= -1
        self.tk.after(40, self.movement)
