import pygame
import random
from pathfinding import astar

CELL_SIZE = 30
WHITE, BLACK, RED, GREEN, BLUE, GREY = (255,255,255), (0,0,0), (255,0,0), (0,255,0), (0,0,255), (200,200,200)

def visualize(grid, start, end, path):
    rows, cols = len(grid), len(grid[0])
    pygame.init()
    win = pygame.display.set_mode((cols * CELL_SIZE, rows * CELL_SIZE))
    pygame.display.set_caption("Mouse AI Pathfinding")

    running = True
    while running:
        win.fill(WHITE)
        for i in range(rows):
            for j in range(cols):
                color = WHITE
                if grid[i][j] == 1:
                    color = BLACK
                elif (i, j) == start:
                    color = GREEN
                elif (i, j) == end:
                    color = RED
                elif path and (i, j) in path:
                    color = BLUE
                pygame.draw.rect(win, color, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
