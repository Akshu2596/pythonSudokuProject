import pygame
import sys

from settings import *
from buttonClass import *


class App:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.grid = finished_board
        self.selected = None
        self.mouse_pos = None
        self.state = "playing"
        self.finished = False
        self.cellChanged = False
        self.incorrectCells = []
        self.playingbuttons = []
        self.menubuttons = []
        self.endbuttons = []
        self.lockedCells = []
        self.load()
        self.font = pygame.font.SysFont("arial", cellSize // 2)

    def run(self):
        while self.running:
            if self.state == "playing":
                self.playing_events()
                self.playing_update()
                self.playing_draw()

        pygame.quit()
        sys.exit()

    ##### PLAYING STATE METHODS #####

    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # when user clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                selected = self.mouseOnGrid()
                if selected:
                    self.selected = selected
                else:
                    print("not on board")
                    self.selected = None

            # when user types a key
            if event.type == pygame.KEYDOWN:
                if self.selected != None and self.selected not in self.lockedCells:
                    if self.isInt(event.unicode):
                        # print(event.unicode)
                        # print(self.selected[0])
                        # print(self.selected[1])
                        # cell changed
                        self.grid[self.selected[1]][self.selected[0]] = int(event.unicode)
                        self.cellChanged = True

    def playing_update(self):
        self.mouse_pos = pygame.mouse.get_pos()
        for buttons in self.playingbuttons:
            buttons.update(self.mouse_pos)

        if self.cellChanged:
            self.incorrectCells = []
            if self.allCellsDone():
                # check if all cells are done correctly
                self.checkAllCells()
                # print(self.incorrectCells)
                if len(self.incorrectCells) == 0:
                    print("Congratulations!")

    def playing_draw(self):
        self.window.fill(PINK)

        for buttons in self.playingbuttons:
            buttons.draw(self.window)

        if self.selected:
            self.drawSelection(self.window, self.selected)

        self.shadeLockedCells(self.window, self.lockedCells)
        self.shadeIncorrectCells(self.window, self.incorrectCells)

        self.drawNumbers(self.window)
        self.drawGrid(self.window)
        pygame.display.update()

        self.cellChanged = False

        ##### BOARD CHECK METHODS #####

    def allCellsDone(self):
        for row in self.grid:
            for number in row:
                if number == 0:
                    return False
        return True

    def checkAllCells(self):
        # self.checkRows()
        # self.checkColumns()
        self.checkSmallGrid()

    def checkRows(self):
        for yidx, row in enumerate(self.grid):
            possibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for xidx in range(9):

                if self.grid[yidx][xidx] in possibles:
                    possibles.remove(self.grid[yidx][xidx])

                else:
                    if [xidx, yidx] not in self.lockedCells and [xidx, yidx] not in self.incorrectCells:
                        self.incorrectCells.append([xidx, yidx])

                    if [xidx, yidx] in self.lockedCells:
                        for k in range(9):
                            if self.grid[yidx][k] == self.grid[yidx][xidx] and [k, yidx] not in self.lockedCells:
                                self.incorrectCells.append([k, yidx])

    def checkColumns(self):
        for xidx in range(9):

            possibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for yidx, row in enumerate(self.grid):

                if self.grid[yidx][xidx] in possibles:
                    possibles.remove(self.grid[yidx][xidx])

                else:
                    if [xidx, yidx] not in self.lockedCells and [xidx, yidx] not in self.incorrectCells:
                        self.incorrectCells.append([xidx, yidx])
                    if [xidx, yidx] in self.lockedCells:
                        for k, row in enumerate(self.grid):
                            if self.grid[k][xidx] == self.grid[yidx][xidx] and [xidx, k] not in self.lockedCells:
                                self.incorrectCells.append([xidx, k])

    def checkSmallGrid(self):
        for x in range(3):
            for y in range(3):
                # print(x,y)
                possibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                # print("re setting possibles")
                for i in range(3):
                    for j in range(3):
                        # print(x*3+i,y*3+j)
                        xidx = x * 3 + i
                        yidx = y * 3 + j
                        if self.grid[yidx][xidx] in possibles:
                            possibles.remove(self.grid[yidx][xidx])
                        else:
                            if [xidx, yidx] not in self.incorrectCells and [xidx, yidx] not in self.lockedCells:
                                self.incorrectCells.append([xidx, yidx])
                                # print("checked by smallGrid")
                            if [xidx, yidx] in self.lockedCells:
                                for k in range(3):
                                    for l in range(3):
                                        xidx2 = x * 3 + k
                                        yidx2 = y * 3 + l
                                        if self.grid[yidx2][xidx2] == self.grid[yidx][xidx] and [xidx2,yidx2] not in self.lockedCells:
                                         self.incorrectCells.append([xidx2, yidx2])

        ##### HELP METHODS #####

    def shadeLockedCells(self, window, locked):
        for cell in locked:
            pygame.draw.rect(window, LOCKEDCLR, ((cell[0] * cellSize) + gridPos[0], (cell[1] * cellSize) + gridPos[1],
                                                 cellSize, cellSize))

    def shadeIncorrectCells(self, window, incorrect):
        for cell in incorrect:
            pygame.draw.rect(window, INCORRECTCLR,
                             ((cell[0] * cellSize) + gridPos[0], (cell[1] * cellSize) + gridPos[1],
                              cellSize, cellSize))

    def drawNumbers(self, window):
        for yidx, row in enumerate(self.grid):
            for xidx, num in enumerate(row):
                if num != 0:
                    pos = [(xidx * cellSize) + gridPos[0], (yidx * cellSize) + gridPos[1]]
                    self.textOnBoard(window, str(num), pos)

    def drawSelection(self, window, pos):
        pygame.draw.rect(window, GREEN,
                         ((pos[0] * cellSize) + gridPos[0], (pos[1] * cellSize) + gridPos[1], cellSize, cellSize))

    def drawGrid(self, window):
        pygame.draw.rect(window, BLACK, (gridPos[0], gridPos[1], WIDTH - 150, HEIGHT - 150), 2)
        for x in range(9):
            pygame.draw.line(window, BLACK, (gridPos[0] + (x * cellSize), gridPos[1]),
                             (gridPos[0] + (x * cellSize), gridPos[1] + 450), 2 if x % 3 == 0 else 1)
            pygame.draw.line(window, BLACK, (gridPos[0], gridPos[1] + (x * cellSize)),
                             (gridPos[0] + 450, gridPos[1] + (x * cellSize)), 2 if x % 3 == 0 else 1)

    def mouseOnGrid(self):
        if self.mouse_pos[0] < gridPos[0] or self.mouse_pos[1] < gridPos[1]:
            return False
        if self.mouse_pos[0] > gridPos[0] + gridSize or self.mouse_pos[1] > gridPos[1] + gridSize:
            return False
        return (self.mouse_pos[0] - gridPos[0]) // cellSize, (self.mouse_pos[1] - gridPos[1]) // cellSize

    def loadButtons(self):
        self.playingbuttons.append(Button(20, 40, 80, 40))

    def textOnBoard(self, window, text, pos):
        font = self.font.render(text, False, BLACK)
        fontWidth = font.get_width()
        fontHeight = font.get_height()
        pos[0] += (cellSize - fontWidth) // 2
        pos[1] += (cellSize - fontHeight) // 2
        window.blit(font, pos)

    def load(self):
        self.loadButtons()

        # settings for determining locked cells

        for yidx, row in enumerate(self.grid):
            for xidx, num in enumerate(row):
                if num != 0:
                    self.lockedCells.append([xidx, yidx])

        print(self.lockedCells)

    def isInt(self, string):
        try:
            int(string)
            return True
        except:
            return False
