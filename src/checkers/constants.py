import pygame
import os

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128,128,128)


cwd = os.getcwd()
cwd = cwd + '\checkers\checkers_crown.png'
CROWN = pygame.transform.scale(pygame.image.load(cwd), (44,25))