# The board object for the game
import pygame
from .piece import Piece

# Color variables
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# size variables
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS # size of the individual square on the board

class Board:
    def __init__(self):
        self.board = []
        self.red_remaining = self.white_remaining = 12
        self.red_kings = self.white_kings = 0
        self.set_board()
        print(self.board)

    # Draws the literal background
    def draw_board(self, window): 
        window.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(window, RED, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    # Sets the pieces on the board
    def set_board(self):
        for row in range(ROWS):
            self.board.append([]) # list for each row
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, window):
        self.draw_board(window)
        for row in range (ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(window)