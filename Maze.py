import random

import pygame


class Maze:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.maze = [['H' for x in range(w)] for y in range(h)]
        self.scale = min(750 / self.h, 750 / self.w)
        self.dfs(1, 1)

    def show_maze(self):
        for i in range(self.h):
            for j in range(self.w):
                print(self.maze[i][j], end="")
            print("")

    def dfs(self, x, y):
        vec = [(2, 0), (0, 2), (-2, 0), (0, -2)]
        self.maze[y][x] = ' '
        random.shuffle(vec)
        self.next_show()
        for v in vec:
            if y+v[0] >= self.h or y+v[0] < 0 or x+v[1] < 0 or x+v[1] >= self.w:
                continue
            if self.maze[y+v[0]][x+v[1]] == 'H':
                self.maze[y + int(v[0] / 2)][x + int(v[1] / 2)] = ' '
                self.dfs(x+v[1], y+v[0])
        return 0

    def next_show(self):
        for i in range(self.h):
            for j in range(self.w):
                if self.maze[i][j] == ' ':
                    colorr = (255, 255, 255)
                    pygame.draw.rect(sc, colorr, pygame.Rect(j*self.scale, i*self.scale, self.scale+1, self.scale+1), 0)
        pygame.display.update()


pygame.init()
sc = pygame.display.set_mode((750, 750))
sc.fill((0, 0, 0))
color = (255, 0, 0)
maze = Maze(50, 50)
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False