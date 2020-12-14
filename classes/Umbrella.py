class umbrella:
    def __init__(selfself,x_umbrella,y_umbrella):
        self.x_umbrella = x_umbrella
        self.y_umbrella = y_umbrella

    def draw(self):
        pyxel.blt(self.x_umbrella,self.y_umbrella,0,0,16,16,16)
