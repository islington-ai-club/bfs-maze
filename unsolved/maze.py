from point import Point
from colors import Colors

class Maze:

    all_dirs = list(map(lambda x: Point(x[0], x[1]),[[-1, 0], [1, 0], [0, -1], [0, 1]]))

    def __init__(self, width, height, block_size):
        self.width = width
        self.height = height
        self.block_size = block_size
        self.map = []
        for i in range(0, width*height):
            self.map.append(0)
            
    def set_walls(self, walls):
        for wall in walls:
            self.map[self.point_to_index(wall)] = 1

    def point_to_index(self, p):
        return p.x + p.y * self.width

    def index_to_point(self, i):
        x = i % self.width
        y = i // self.width
        return Point(x, y)

    def get_from_map(self, p):
        return self.map[self.point_to_index(p)]
    
    def draw_maze(self, pygame, canvas, font_style):
        canvas.fill(Colors.white)
        for i in range(0, self.width):
            for j in range(0, self.height):
                p = Point(i, j)
                index = self.point_to_index(p)
                rect_color, border_color = Colors.white, Colors.black
                
                if self.get_from_map(p) == 1:
                    rect_color, border_color = border_color, rect_color
                
                pygame.draw.rect(canvas, rect_color, (p.x * self.block_size, p.y * self.block_size, self.block_size, self.block_size))   
                pygame.draw.rect(canvas, border_color, (p.x * self.block_size, p.y * self.block_size, self.block_size, self.block_size), 1)   
                
                text = font_style.render(str(index), True, border_color)
                canvas.blit(text, [p.x * self.block_size +
                            (self.block_size/4), p.y * self.block_size + (self.block_size/4)]) 
    
    def is_wall(self, p):
        return self.get_from_map(p) == 1

    def is_valid(self, p):
        return p.x >= 0 and p.x < self.width and p.y >= 0 and p.y < self.height

    def get_neighbours(self, p):
        # TODO: return a list of neighbours of p: list of points
        
        pass

    def bfs(self, start, end):
        # TODO: return a list of points from start to end: list of points

        pass
    

        
        