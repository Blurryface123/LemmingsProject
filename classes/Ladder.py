import pyxel


class Ladder():
    def __init__(self,px,py,grid):
        #size
        self.WIDTH = 16
        self.HEIGHT = 16
        #self.active=active Necessary?? Need a way to indetify it as a tool
        #position. Where the laddder is. We can move it with the keyboard
        self.px= px
        self.py= py
        self.grid=grid
        # self.ladder_type = 1
        # self.ladder_image_coord = [32,16]

    # def select_ladder(self,):
    #     first_ladder = 32
    #     second_ladder = 32
    #     if self.ladder_type == 1:
    #         pyxel.blt(16 * self.px, 16 * self.py, 0, first_ladder, 16, 16, 16)
    #     elif self.ladder_type == 2:
    #         pyxel.blt(16 * self.px, 16 * self.py, 0, second_ladder, 16, 16, 16)
    #         print(self.ladder_image_coord[0])
    #         self.ladder_image_coord[0]= self.ladder_image_coord[second_ladder]
    #         print(self.ladder_image_coord[0])
    def draw_first_ladder(self):
        self.grid[self.px][self.py] = 5
    def draw_second_ladder(self):
        self.grid[self.px][self.py] = 6


