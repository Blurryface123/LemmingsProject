def block(x, y,grid):
    x, y = int(x), int(y)
    if x < 15 and y < 15 and x >= 0 and y >= 0:
        # limits
        if grid[x][y] == 0:
            return True
        else:
            return False