# this is the top level file for the app
import pygame 
from checkers.board import Board

# size variables
WIDTH, HEIGHT = 800, 800

# sys variables
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Agile Project Team 10: Checkers')

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
                #TODO Define what to do when a player CLICKS on something... 
                print("Hey! I don't do anything yet!!")

        board.draw(WIN)
        pygame.display.update()

    pygame.QUIT

main()

