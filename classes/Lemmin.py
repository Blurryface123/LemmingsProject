from classes.Blocker import block as b
import pyxel


#CHANGE THE PX TO 14 BECAUSE ITS 14 X 16. EACH CELL
class Lemming(object):
    def __init__(self,l_lemmings):
        #size of lemmin
        self.width = 15
        self.height = 15
        #position. Where the lemming starts
        self.px= 0
        self.py= 0
        #0 means going to the left, and 1 goes to the right
        self.direction = 1
        self.l_lemmings= l_lemmings

    def gravity(self):
        # Checking if there is floor. The program has to check if there is a floor first
        if b.block(self.px, self.py + 16):
            # To make it fall.
            self.py += 16

    def movement(self):
        #It's moving
        if self.direction==1:
            Lemming.gravity(self)
            #Checking if there is a block on the right
            if b.block(self.px+16, self.py):
                #Makes it move. Left to right
                self.px += 16
            #elif b.block(self.x,self.py-16):
            else:
                self.direction = 0
        #Changed direction. position = 0
        else:
            Lemming.gravity(self)
            #Checking if there is a block on the left
            if b.block(self.px-16, self.py):
                self.px -= 16
            else:
                #change direction, moves to right. Goes back to if above
                self.direction = 1
    def draw_lemming(self):
        if self.px <= 256 and self.py <= 256:
            #draws the lemming in the rectangle
            pyxel.rect(self.px, self.py, 16, 16, 11)

    def delete_leming(self):
        if self.px > 256 and self.py > 256:
            self.l_lemmings.remove()


