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
        #list of lemmings
        #self.l_lemmings= l_lemmings



    def fall(self):
        # Checking if there is floor. The program has to check if there is a floor first
        if Blocker.block(self.px, self.py + 1,self.grid):
            # To make it fall.
            self.py += 1
            #if it hit the platform or the ground
            if self.grid[self.px][self.py] == 2 or self.py == 15:
                Lemming.delete_leming()


    def update(self):
        #It's moving
        if self.direction==1:
            Lemming.fall(self)
            #Checking if there is a block on the right
            if Blocker.block(self.px+1, self.py,self.grid):
                #Makes it move. Left to right
                self.px += 1
            #check if we can go up to use the ladder
            # elif b.block(self.px+16, self.py-16) and #ladder is activated???? Maybe pixel has to be different than 1 or 0 for tools:
            #     self.px+= 16
            #     self.py -=16
            else:
                self.direction = 0
        #Changed direction. position = 0
        else:
            Lemming.fall(self)
            #Checking if there is a block on the left
            if Blocker.block(self.px-1, self.py,self.grid):
                self.px -= 1
            # elif Blocker.block(self.px-16, self.py-16,self.grid):
            #     self.px-= 16
            #     self.py -=16
            else:
                #change direction, moves to right. Goes back to if above
                self.direction = 1
    def draw_lemming(self):
        if self.px <= 256 and self.py <= 256:
            #draws the lemming in the rectangle
            pyxel.blt(16*self.px, 16*self.py,0,48,0,16,16)

    def delete_leming(self):
        if self.px > 256 and self.py > 256:
            self.l_lemmings.remove()


    # WIDTH = 256
    # HEIGHT = 256
    # CAPTION = "This is an example of drawing figures in pyxel"
    #
    # # The first thing to do is to create the screen, see API for more parameters
    # pyxel.init(WIDTH, HEIGHT, caption=CAPTION,scale=2)
    # pyxel.load("assets/my_resource.pyxres")
    # # To start the game we invoke the run method with the update and draw functions
    # pyxel.run(movement, draw_lemming)
