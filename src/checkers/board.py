# The board object for the game
import pygame
from .piece import Piece
from .constants import *

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

    #Moves piece on board
    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row,col)

        #updates king status
        if row == ROWS or row == 0:
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings += 1
            else:
                self.red_kings += 1
    
    def get_piece(self, row, col):
        return self.board[row][col]

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
                    
    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row
        
        if piece.color == RED or piece.king:
            pass
            
        if piece.color == WHITE or piece.king:
            pass
            
    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        pass
       
    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        pass