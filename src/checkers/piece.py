# the player piece on the board
import pygame

RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

#crown image download
CROWN = pygame.transform.scale(pygame.image.load('src/checkers/checkers_crown.png'), (44,25))


class Piece():
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False

        self.x = 0 
        self.y = 0
        self.position()

    def position(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2 # place the piece in the center of the square
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True
    
    def draw(self, window):
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(window, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(window, self.color, (self.x, self.y), radius)
        if self.king:
            window.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.position()