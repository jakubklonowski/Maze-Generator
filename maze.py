import random

class Maze:
    def __init__(self, width, height):
        self.width = width + 1
        self.height = height + 1
        self.grid = [[1 for _ in range(self.width)] for _ in range(self.height)] # every cell is a WALL
    
    def generate(self):
        start_x, start_y = 1, 0  # start at (1,0)
        self.grid[start_y][start_x] = 0  # create entrance
        stack = [(start_x, start_y+1)]  # start generating from (1, 1)
        self.grid[start_y+1][start_x] = 0
        
        while stack:
            current_x, current_y = stack[-1] # take last element of stack of PASSAGES
            neighbors = self.get_unvisited_neighbors(current_x, current_y) # look for it's (legal) neighbors
            
            if neighbors: # if legal neighbor exist => choose one, make it PASSAGE
                next_x, next_y = random.choice(neighbors)
                self.remove_wall(current_x, current_y, next_x, next_y)
                stack.append((next_x, next_y))
            else: # if no legal neighbors => cancel this PASSAGE-candidate and look for another
                stack.pop()

        end_x, end_y = self.width - 2, self.height - 1
        self.grid[end_y][end_x] = 0
        self.remove_wall(end_x - 1, end_y - 1, end_x, end_y)

    def get_unvisited_neighbors(self, x, y):
        neighbors = []
        for dx, dy in [(0, 2), (2, 0), (0, -2), (-2, 0)]:
            nx, ny = x + dx, y + dy 
            # for each sum above (sum of coordinates of X, Y (current position) and DX, DY)
            # check rule below (it's WALL that is not outermost wall)
            if 0 < nx < self.width-1 and 0 < ny < self.height-1 and self.grid[ny][nx] == 1:
                neighbors.append((nx, ny))
        return neighbors
    
    # turns WALL into PASSAGE
    def remove_wall(self, x1, y1, x2, y2):
        self.grid[y1][x1] = 0 # current cell
        self.grid[y2][x2] = 0 # next cell
        self.grid[(y1+y2)//2][(x1+x2)//2] = 0 # between current and next
    
    # turn WALL into "██" and PASSAGE into "  "; print
    def __str__(self):
        maze_str = ""
        for row in self.grid:
            for cell in row:
                maze_str += "██" if cell else "  "
            maze_str += "\n"
        return maze_str

maze = Maze(20, 20) # maze dimensions
maze.generate()
print(maze)
