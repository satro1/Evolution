import numpy as np
from functools import reduce

random_angle_range = np.pi / 8
padding_x = 40
padding_y = 40
backup_steps = 20

class Ball:
    def __init__(self, size, speed, color, width, height, canvas, tk):
        self.ball = canvas.create_oval(width//2, height//2, width//2 + size, height//2 + size, fill=color)
        canvas.pack()
        self.speed = speed
        self.speedx, self.speedy = self.getInitialSpeed()
        self.canvas = canvas
        self.tk = tk
        self.width = width
        self.height = height
        self.xflag, self.yflag = False, False
        self.stepsx, self.stepsy = 0, 0
  #      self.movement()

    def getInitialSpeed(self):
        speed = [np.random.rand() - 0.5, np.random.rand() - 0.5]
        norm = np.sqrt(reduce(lambda a, b: a + b, map(lambda a: a ** 2, speed)))
        return map(lambda a: self.speed * a / norm, speed)

    def getSpeed(self):
        theta = np.arctan(self.speedy / self.speedx)
 #       if self.speedx < 0:
  #          theta += np.pi
        theta += ((-1) ** np.random.randint(0, 2)) * random_angle_range / 2
        return map(lambda a: self.speed * a, [np.cos(theta), np.sin(theta)])

    def movement(self):
        if self.xflag:
            self.stepsx += 1
            if self.stepsx >= backup_steps:
                self.stepsx = 0
                self.xflag = False
        if self.yflag:
            self.stepsy += 1
            if self.stepsy >= backup_steps:
                self.stepsy = 0
                self.yflag = False
        if (not self.xflag) and (not self.yflag):
            self.speedx, self.speedy = self.getSpeed()
        pos = self.canvas.bbox(self.ball)
        if (pos[2] >= self.width - padding_x or pos[0] <= padding_x):
            self.speedx *= -1
            self.xflag = True
        if (pos[3] >= self.height - padding_y or pos[1] <= padding_y):
            self.speedy *= -1
            self.yflag = True

        self.canvas.move(self.ball, self.speedx, self.speedy)
        self.tk.after(50, self.movement)

class Creature(Ball):
    def __init__(self, size, speed, color, width, height, canvas, tk):
        super(Creature, self).__init__(size, speed, color, width, height, canvas, tk)
        
    def movement(self):
        super(Creature, self).movement()
