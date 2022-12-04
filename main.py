import pygame
from point import Point
from maze import Maze

pygame.init()
pygame.font.init()


block_size = 50
width = 10
height = 10
canvas_width = width *  block_size
canvas_height = height *  block_size

canvas = pygame.display.set_mode((canvas_width, canvas_height))
pygame.display.set_caption('BFS Maze')
font_style = pygame.font.SysFont("Times New Roman", 25)
        
show_maze = True

walls = list(map(lambda x: Point(x[0], x[1]),
                 [[2, 0],
                  [2, 1],
                  [2, 2],
                  [2, 3],
                  [2, 4],
                  [4, 5],
                  [4, 6],
                  [4, 7],
                  [4, 8],
                  [4, 9],
                  [6, 0],
                  [6, 1],
                  [6, 2],
                  [6, 3],
                  [6, 4],
                  [8, 5],
                  [8, 6],
                  [8, 7],
                  [8, 8],
                  [8, 9]]))

maze = Maze(10, 10, block_size)
maze.set_walls(walls)
maze.draw_maze(pygame, canvas, font_style)



while show_maze:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            show_maze = False
    
    pygame.display.update()
