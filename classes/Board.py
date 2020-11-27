import pyxel
import random
# To use pyxel we need to define two functions, one will do all the
# calculations needed each frame, the other will paint things on the screen
# They can have any name, but the 'standard' ones are update and draw
#from classes.Lemmin import Lemming


class Board(object):
    def __init__(self,timer,interval):
        pyxel.cls(0)
        #total size
        #lemmings in the board
        self.lemmings = []
        self.timer = timer
        self.interval = interval
        self.max_lemmings = 10
        self.grid = [[random.randint(0,3) for y in range(0, 256, 16)] for x in range(0, 256, 16)]
        #ground and ceiling
        for x in range(16):
            self.grid[x][15] = 1
            self.grid[x][0] = 1
        for y in range(16):
            self.grid[15][y] = 1
            self.grid[0][x] = 1
        #making an opening at the top where the lemming will start
        self.grid[0][0] = 0
        self.grid[1][0] = 0
        self.grid[0][1] = 0
        self.grid[1][1] = 0
        pyxel.playm(0, loop=False)
        pyxel.run(self.update, self.draw())

    def update(self):
        ''' This function is executed every frame. Now it only checks if the
        Escape key or Q are pressed to finish the program'''
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()



    def draw(self):
        ''' This function puts things on the screen every turn. Now only text '''
        # We set the background color, anything on the screen is erased
        # See pyxel documentation for available colors (16)
        # 0 is black
        pyxel.cls(0)
        #should be 14??? Creating matrix
        for x in range(16):
            for y in range(16):
                if self.grid[x][1] == 1:
                    pyxel.blt(16*x, 16*y,0,0,0,16,16)
        for n in self.lemmings:
            n.draw(n)
        # with .text(x:int,y:int,text:str,color:int) we draw a text in the screen
        ##pyxel.text(0, 0, "alive", 1)
        # we use pyxel.frame_count to do things every frame (here changing color)
        ##pyxel.text(0, 10, "Changing color every frame", pyxel.frame_count % 16)
        # this is done every frame... moving a text until it reaches the end
        # we can know the width and height of the screen using pyxel.width or
        # pyxel.height
        ##x = pyxel.frame_count % pyxel.width
        ##pyxel.text(x, 20, "Moving text", 3)


    ################## main program ##################


    # Creating constants so it is easier to modify values
    # Maximum width and height are 256



