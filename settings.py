WIDTH = 600
HEIGHT = 600

# colours

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (7, 208, 182)
PINK = (255, 223, 241)
LOCKEDCLR = (255,153,127)

# boards

game_board = [[0 for x in range(9)] for x in range(9)]
game_board2 = [[0, 0, 7, 0, 0, 0, 0, 0, 8],
               [0, 0, 0, 0, 3, 0, 0, 0, 0],
               [0, 0, 3, 0, 0, 0, 0, 0, 1],
               [0, 0, 0, 4, 0, 0, 0, 5, 0],
               [0, 5, 0, 0, 0, 0, 3, 0, 0],
               [0, 0, 0, 0, 0, 1, 0, 0, 7],
               [4, 0, 0, 0, 0, 0, 7, 0, 0],
               [0, 0, 6, 0, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 8, 2, 0]]

# position of grid

gridPos = [75, 100]
cellSize = 50
gridSize = cellSize * 9
