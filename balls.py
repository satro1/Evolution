import numpy as np
import utils
from functools import reduce

params = utils.parse_json("parameters.json")
random_angle_range = params["random_angle_range"]
padding_x = params["padding_x"]
padding_y = params["padding_y"]
backup_steps = params["backup_steps"]
y_padding_adjustment = params["y_padding_adjustment"]


class Ball:
    def __init__(self, size, speed, color, width, height, canvas, tk):
        w, h = np.random.rand() * (width - 2 * padding_x) + padding_x, \
               np.random.rand() * (height - 2 * padding_y) + padding_y + y_padding_adjustment
        self.ball = canvas.create_oval(w, h, w + size, h + size, fill=color)
        canvas.pack()
        self.speed = speed
        self.speedx, self.speedy = self.getInitialSpeed()
        self.canvas = canvas
        self.tk = tk
        self.width = width
        self.height = height
        self.xflag, self.yflag = False, False
        self.stepsx, self.stepsy = 0, 0

    def getInitialSpeed(self):
        speed = [np.random.rand() - 0.5, np.random.rand() - 0.5]
        norm = np.sqrt(reduce(lambda a, b: a + b, map(lambda a: a ** 2, speed)))
        return map(lambda a: self.speed * a / norm, speed)

    def getSpeed(self):
        theta = 0
        if self.speedx == 0:
            if self.speedy > 0:
                theta = np.pi / 2
            else:
                theta = 3 * np.pi / 2
        else:
            theta = np.arctan(self.speedy / self.speedx)
        if self.speedx < 0:
            theta += np.pi
        theta += ((-1) ** np.random.randint(2)) * random_angle_range / 2
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
        if (pos[2] >= self.width - padding_x or pos[0] <= padding_x) and not self.xflag:
            self.speedx *= -1
            self.xflag = True
        if (pos[3] >= self.height - padding_y or pos[1] <= padding_y) and not self.yflag:
            self.speedy *= -1
            self.yflag = True

        self.canvas.move(self.ball, self.speedx, self.speedy)
        self.tk.after(50, self.movement)


class Creature(Ball):
    def __init__(self, size, speed, color, width, height, canvas, tk):
        super(Creature, self).__init__(size, speed, color, width, height, canvas, tk)


class Food(Ball):
    def __init__(self, width, height, canvas, tk):
        super(Food, self).__init__(1, 0, "white", width, height, canvas, tk)
