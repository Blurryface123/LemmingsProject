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
from classes.Board import Board
import pyxel

if __name__== "__main__":
    WIDTH = 256
    HEIGHT = 256
    timer = 10
    interval = 10
    CAPTION = "Lemmings Project"
    pyxel.init(WIDTH,HEIGHT, caption=CAPTION, scale=2)
    pyxel.load("assets/my_resource.pyxres")
    Board(timer,interval)
