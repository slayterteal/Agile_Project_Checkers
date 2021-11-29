# this is the top level file for the app
import pygame 
from checkers.board import Board

# size variables
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# sys variables
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Agile Project Team 10: Checkers')

def get_pos_from_mouse(coord):
    x, y = coord
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row,col 

def main():
    run = True
    clk = pygame.time.Clock() 
    board = Board()

    while run:
        clk.tick(FPS) 

        for event in pygame.event.get(): # the pygame event loop
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                coord = pygame.mouse.get_pos()
                row, col = get_pos_from_mouse(coord)
                selected_piece = board.get_piece(row,col)
                board.move(selected_piece, 5,5)

        board.draw(WIN)
        pygame.display.update()

    pygame.QUIT

main()

