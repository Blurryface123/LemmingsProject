"""import pyxel
import random
pyxel.cls(0)
HEIGHT = 256
WIDTH = 256
lemmings = [] #ver si dejar o no
timer = 8 #ver si dejar o no
interval = 10
# The first thing to do is to create the screen, see API for more parameters
pyxel.init(HEIGHT, WIDTH, caption="Lemmings Game",scale=2)
pyxel.load("assets/my_resource.pyxres")

grid = [[], []]

# To start the game we invoke the run method with the update and draw functions
pyxel.run(update, draw)"""
#from classes.Board import Board
#import pyxel

#from classes.Lemmin import Lemming

#if __name__== "__main__":
#    WIDTH = 256
#    HEIGHT = 256
#    timer = 10
#    interval = 10
#    CAPTION = "Lemmings Project"
#    pyxel.init(WIDTH,HEIGHT, caption=CAPTION, scale=2)
#    pyxel.load("my_resource.pyxres")
#    Board()
#    Lemming(10)
import pyxel
import random
import time

from classes.Ladder import Ladder
from classes.Lemmin import Lemming
from classes.platform import Platform


class App:
    def __init__(self):
        pyxel.init(256, 256,fps=6)
        pyxel.load("assets/my_resource.pyxres")
        #random.randint(0, 3)
        self.grid = [[0 for y in range(0, 256, 14)] for x in range(0, 256, 16)]
        #aqui abajo podria ir el lemming
        self.cursor_x = 0
        self.cursor_y= 0
        self.door_x=0
        self.door_y=0
        self.lemmings = []
        self.max_lemming = 10
        self.count = 0
        # ground, ceiling and walls
        for x in range(16):
            self.grid[x][15] = 1
            self.grid[x][0] = 1
        for y in range(16):
            self.grid[15][y] = 1
            self.grid[0][y] = 1

        #making an opening at the top where the lemming will start
        #self.grid[0][0] = 0
        #self.grid[1][0] = 0
        #self.grid[0][1] = 0
        #self.grid[1][1] = 0
        self.base_time = time.time()
        pl = Platform(self.grid)
        pl.create()
        self.door(pl.x_start,pl.x_end,pl.y, pl.n)



        #El run tiene que ir despues para coger los cambios del grid
        pyxel.run(self.update, self.draw)

    #CREAR HUECO ALEATORIA
    #plataformas tienen valor 2
    # def platform(self):
    #     count = 0
    #     x_index = []
    #     y_index = []
    #     platforms_sizes = []
    #     while count <7:
    #         # 14 espacios libres (contando paredes) y max blockques de 11
    #         j = random.randint(1, 14)
    #         platform_size = random.randint(5, 11)
    #         i = random.randint(1, 14-platform_size)
    #
    #         #to avoid repeated places. The grid i j == 0 is to avoid blocking the entrace
    #         if i not in x_index and j not in y_index and self.grid[i][j]==0:
    #             x_index.append(i)
    #             y_index.append(j)
    #             platforms_sizes.append(platform_size)
    #             count+=1
    #             for x in range(16):
    #                 #To place the platform. starts at i and ends at the i+random length
    #                 if x >=i and x <=i+platform_size:
    #                     self.grid[x][j] = 2
    #
    #
    #     return list(zip(x_index,y_index,platforms_sizes))

    def door(self, pl_start,pl_end, y,n_platforms):
        count = 0
        while count < 2:
            #random platform
            platform_index = random.randint(0,n_platforms-1)#number platforms
            door_coord_x = random.randint(pl_start[platform_index], pl_end[platform_index])
            door_coord_y = y[platform_index]
            #We only save the coords of the main door
            if count ==0:
                self.door_x = door_coord_x
                self.door_y = door_coord_y
            if self.grid[door_coord_x][door_coord_y-1] == 0:
                if count==0:
                    self.grid[door_coord_x][door_coord_y - 1] = 3
                else:
                    self.grid[door_coord_x][door_coord_y-1] = 4
                count+=1


    def update(self):
        #first lemming
        if self.count == 0:
            self.lemmings.append(Lemming(self.door_x, self.door_y - 1, self.grid))
            self.count +=1
        #Lemming created in intervals
        if int(time.time())-int(self.base_time) == 3 and len(self.lemmings)<self.max_lemming:
            self.lemmings.append(Lemming(self.door_x, self.door_y - 1, self.grid))
            self.base_time= time.time()
        for n in range(len(self.lemmings)):
            if self.lemmings[n].is_dead == True:
                self.lemmings.pop(n)
            elif self.lemmings[n].is_saved == True:
                self.lemmings.pop(n)
            else:
                self.lemmings[n].update()




    def draw_cursor(self,direction):
        #if self.cursor_x + right < 16 and self.cursor_y + down <= 16 and self.cursor_x - left > 0 and self.cursor_y - up > 0:
        up = self.cursor_y - 1
        down = self.cursor_y + 1
        left = self.cursor_x - 1
        right = self.cursor_x + 1
        if direction == "up" and up >= 0:
            self.cursor_y = up
        elif direction == "down" and down < 16:
            self.cursor_y = down
        elif direction == "left" and left >= 0:
            self.cursor_x = left
        elif direction == "right" and right < 16:
            self.cursor_x = right
        pyxel.blt(16 * self.cursor_x, 16 * self.cursor_y, 0, 16, 16, 16, 16)

    def move_cursor(self):
        if pyxel.btn(pyxel.KEY_UP):
            App.draw_cursor(self,"up")
        elif pyxel.btn(pyxel.KEY_DOWN):
            App.draw_cursor(self, "down")
        elif pyxel.btn(pyxel.KEY_LEFT):
            App.draw_cursor(self, "left")
        elif pyxel.btn(pyxel.KEY_RIGHT):
            App.draw_cursor(self, "right")

    def place_tool(self):
        if self.grid[self.cursor_x][self.cursor_y] == 0:
            #left to right Ladder
            if pyxel.btn(pyxel.KEY_X):
                Ladder(self.cursor_x, self.cursor_y, self.grid).draw_first_ladder()
            #right to left ladder
            elif pyxel.btn(pyxel.KEY_C):
                Ladder(self.cursor_x, self.cursor_y,self.grid).draw_second_ladder()
            #Umbrella
            elif pyxel.btn(pyxel.KEY_V):
                print("Umbrella")
            #blocker
            elif pyxel.btn(pyxel.KEY_B):
                print("blocker")

    def draw(self):
        pyxel.cls(0)
        for x in range(16):
            for y in range(16):
                if self.grid[x][y]==1:
                    #*16 because 1 square is 16 cells
                    pyxel.blt(16*x, 16*y,0,0,0,16,16)
                #platform
                elif self.grid[x][y]==2:
                    pyxel.blt(16 * x, 16 * y, 0, 16, 0, 16, 16)
                #main door
                elif self.grid[x][y]==3:
                    pyxel.blt(16 * x, 16 * y, 0, 32, 0, 16, 16)
                # exit door
                elif self.grid[x][y] == 4:
                    pyxel.blt(16 * x, 16 * y, 0, 0, 16, 16, 16)
                #ladder
                elif self.grid[x][y] == 5:
                    pyxel.blt(16 * x, 16 * y, 0, 32, 16, 16, 16)
                elif self.grid[x][y] == 6:
                    pyxel.blt(16 * x, 16 * y, 0, 48, 16, 16, 16)
        App.move_cursor(self)
        App.place_tool(self)

        for n in range(len(self.lemmings)):
            self.lemmings[n].draw_lemming()





                #for i in self.platform():
                    #if self.grid[x][y] == 0 and x + len(i) <y:


        #pyxel.rect(self.x, 0, 6, 6, 9)
App()