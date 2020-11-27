def block(x, y,grid):
    grid
    x, y = int(x), int(y)
    if x < 256 and y < 256:
        # limits
        if grid[x // 16][y // 16] != 1:
            return True
        else:
            return False