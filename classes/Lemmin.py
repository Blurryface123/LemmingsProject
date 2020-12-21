from classes import Blocker
import pyxel


#CHANGE THE PX TO 14 BECAUSE ITS 14 X 16. EACH CELL
class Lemming():
    def __init__(self,px, py, grid):
        #size of lemmin
        self.width = 16
        self.height = 16
        #position. Where the lemming starts
        self.px = px
        self.py = py
        #0 means going to the left, and 1 goes to the right
        self.direction = 1
        self.grid = grid
        self.is_dead=False
        self.is_saved = False
        #list of lemmings
        #self.l_lemmings= l_lemmings

        #if the door appears near a wall
        if self.px == 15:
            self.px = 13
            self.direction == 0



    def fall(self):
        # Checking if there is floor. The program has to check if there is a floor first
        if not Lemming.check_platform(self):
            # To make it fall.
            self.py += 1
            #if it hit the platform or the ground
            if self.grid[self.px][self.py+1] == 2 or self.py+1 == 15:
                self.is_dead = True
            # if the lemming goes to the exit
            if self.grid[self.px][self.py+1] == 4:
                self.is_saved = True



    def check_platform(self):
        # check if there is a floor
        if Lemming.block(self,self.px, self.py+1, self.grid):
            return True
        else:
            return False
    # def check_corners(self):
    #     if not Lemming.block(self, self.px + 1, self.py + 1, self.grid) and not Lemming.check_platform(self):
    #         print("hola2")
    #         return True

    def move(self):
        if self.direction == 1:
            if not Lemming.block(self, self.px+1, self.py, self.grid) and Lemming.check_platform(self):
                print(self.px, self.py)
                #Makes it move. Left to right
                self.px += 1
                #if the lemming move to the exit from the right
                if self.grid[self.px+1][self.py] == 4:
                    self.is_saved = True
            #check if we can go up to use the ladder
            elif self.grid[self.px+1][self.py] == 5:
                 self.px+= 1
                 self.py -=1
            else:
                self.direction = 0
        else:
            #Checking if there is a block on the left
            if not Lemming.block(self, self.px-1, self.py,self.grid) and Lemming.check_platform(self):
                print(self.px, self.py)
                self.px -= 1
                # if the lemming move to the exit from the left
                if self.grid[self.px - 1][self.py] == 4:
                    self.is_saved = True
            elif self.grid[self.px + 1][self.py] == 5:
                self.px -= 1
                self.py += 1
            else:
                #change direction, moves to right. Goes back to if above
                self.direction = 1


    def update(self):
        #It's moving
        Lemming.move(self)
        Lemming.fall(self)

    def block(self,x, y, grid):
        x, y = int(x), int(y)
        if x < 16 and y < 16 and x >= 0 and y >= 0 and grid[x][y] == 0 or grid[x][y] == 3:
            # limits
            return False
        else:
            return True

    def draw_lemming(self):
        if self.px < 15 and self.py < 15:
            #draws the lemming in the rectangle
            pyxel.blt(16*self.px, 16*self.py,0,48,0,16,16)



    # WIDTH = 256
    # HEIGHT = 256
    # CAPTION = "This is an example of drawing figures in pyxel"
    #
    # # The first thing to do is to create the screen, see API for more parameters
    # pyxel.init(WIDTH, HEIGHT, caption=CAPTION,scale=2)
    # pyxel.load("assets/my_resource.pyxres")
    # # To start the game we invoke the run method with the update and draw functions
    # pyxel.run(movement, draw_lemming)
