import pygame
import sys

from settings import *


class App:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.grid = game_board
        self.selected = None
        self.mouse_pos = None

    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()

        pygame.quit()
        sys.exit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                selected = self.mouseOnGrid()
                if selected:
                    self.selected = selected
                else:
                    print("not on board")
                    self.selected = None

    def update(self):
        self.mouse_pos = pygame.mouse.get_pos()

    def draw(self):
        self.window.fill(WHITE)
        self.drawGrid(self.window)
        if self.selected:
            self.drawSelection(self.window, self.selected)
        pygame.display.update()

    def drawSelection(self, window, pos):
        pygame.draw.rect(window, GREEN, ((pos[0] * cellSize) + gridPos[0], (pos[1] * cellSize) + gridPos[1], cellSize, cellSize))

    def drawGrid(self, window):
        pygame.draw.rect(window, BLACK, (gridPos[0], gridPos[1], WIDTH - 150, HEIGHT - 150), 2)
        for x in range(9):
            if x % 3:
                pygame.draw.line(window, BLACK, (gridPos[0] + (x * cellSize), gridPos[1]),
                                 (gridPos[0] + (x * cellSize), gridPos[1] + 450))
                pygame.draw.line(window, BLACK, (gridPos[0], gridPos[1] + (x * cellSize)),
                                 (gridPos[0] + 450, gridPos[1] + (x * cellSize)))
            else:
                pygame.draw.line(window, BLACK, (gridPos[0] + (x * cellSize), gridPos[1]),
                                 (gridPos[0] + (x * cellSize), gridPos[1] + 450), 2)
                pygame.draw.line(window, BLACK, (gridPos[0], gridPos[1] + (x * cellSize)),
                                 (gridPos[0] + 450, gridPos[1] + (x * cellSize)), 2)

    def mouseOnGrid(self):
        if self.mouse_pos[0] < gridPos[0] or self.mouse_pos[1] < gridPos[1]:
            return False
        if self.mouse_pos[0] > gridPos[0] + gridSize or self.mouse_pos[1] > gridPos[1] + gridSize:
            return False
        return (self.mouse_pos[0] - gridPos[0]) // cellSize, (self.mouse_pos[1] - gridPos[1]) // cellSize
