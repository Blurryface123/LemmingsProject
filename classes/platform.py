import random

class Platform:
    def __init__(self,grid):
        self.x_start = []
        self.x_end = []
        self.y = []
        self.size = []
        self.n = 7
        self.grid = grid


    #plataformas tienen valor 2
    def create(self):
        count = 0

        platforms_sizes = []
        while count <self.n:
            # 14 espacios libres (contando paredes) y max blockques de 11
            j = random.randint(1, 14)
            platform_size = random.randint(5, 11)
            i = random.randint(1, 14-platform_size)

            #to avoid repeated places. The grid i j == 0 is to avoid blocking the entrace
            if i not in self.x_start and j not in self.y and self.grid[i][j]==0:
                self.x_start.append(i)
                self.y.append(j)
                platforms_sizes.append(platform_size)
                self.x_end.append(i+platform_size)
                count+=1
                for x in range(16):
                    #To place the platform. starts at i and ends at the i+random length
                    if x >=i and x <=i+platform_size:
                        self.grid[x][j] = 2


        #self.platform_coords = list(zip(x_index,y_index,platforms_sizes))