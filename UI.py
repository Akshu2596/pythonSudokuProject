import pygame
import sys

from settings import *


class App:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.grid = game_board

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

    def update(self):
        pass

    def draw(self):
        self.window.fill(WHITE)
        self.drawGrid(self.window)
        pygame.display.update()

    def drawGrid(self,window):
        pygame.draw.rect(window, BLACK ,(gridPos[0], gridPos[1], WIDTH-40 ,HEIGHT-120),2)



