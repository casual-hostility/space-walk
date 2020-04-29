import pygame
import random

# creating the data structure for pieces
# setting up global vars
# functions
# - create_grid
# - draw_grid
# - draw_window
# - rotating shape in main
# - setting up the main

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

pygame.font.init()

# GLOBALS VARS
s_width = 800
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per block
block_size = 30

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height

# SHAPE FORMATS

S = [[\'.....\',
\'......\',
\'..00..\',
\'.00...\',
\'.....\'],
[\'.....\',
\'..0..\',
\'..00.\',
\'...0.\',
\'.....\']]

Z = [[\'.....\',
\'.....\',
\'.00..\',
\'..00.\',
\'.....\'],
[\'.....\',
\'..0..\',
\'.00..\',
\'.0...\',
\'.....\']]

I = [[\'..0..\',
\'..0..\',
\'..0..\',
\'..0..\',
\'.....\'],
[\'.....\',
\'0000.\',
\'.....\',
\'.....\',
\'.....\']]

O = [[\'.....\',
\'.....\',
\'.00..\',
\'.00..\',
\'.....\']]

J = [[\'.....\',
\'.0...\',
\'.000.\',
\'.....\',
\'.....\'],
[\'.....\',
\'..00.\',
\'..0..\',
\'..0..\',
\'.....\'],
[\'.....\',
\'.....\',
\'.000.\',
\'...0.\',
\'.....\'],
[\'.....\',
\'..0..\',
\'..0..\',
\'.00..\',
\'.....\']]

L = [[\'.....\',
\'...0.\',
\'.000.\',
\'.....\',
\'.....\'],
[\'.....\',
\'..0..\',
\'..0..\',
\'..00.\',
\'.....\'],
[\'.....\',
\'.....\',
\'.000.\',
\'.0...\',
\'.....\'],
[\'.....\',
\'.00..\',
\'..0..\',
\'..0..\',
\'.....\']]

T = [[\'.....\',
\'..0..\',
\'.000.\',
\'.....\',
\'.....\'],
[\'.....\',
\'..0..\',
\'..00.\',
\'..0..\',
\'.....\'],
[\'.....\',
\'.....\',
\'.000.\',
\'..0..\',
\'.....\'],
[\'.....\',
\'..0..\',
\'.00..\',
\'..0..\',
\'.....\']]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
# index 0 - 6 represent shape


class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0


def create_grid(locked_positions = {}): #creates blank tetris grid
    grid = [[(0,0,0) for x in range(10)] for x in range(20)]] #0,0,0 is black, just stands for color

    for i in range(len(grid)): #in the 20 list, rows represented by i, columns represented by j
        for j in range(len(grid[i])): #in the 10 list
            if (j, i) in locked_pos:
                c = locked_pos[(j, i)]
                grid[i][j] = c
    return grid

def convert_shape_format(shape):
    pass


def valid_space(shape, grid):
    pass


def check_lost(positions):
    pass


def get_shape():
    return random.choice(shapes) #gets random shape from shapes lists above


def draw_text_middle(text, size, color, surface):
    pass


def draw_grid(surface, row, col):
    surface.fill((0,0,0,)) #fills in grid with black color

    pygame.font.init() #initialize font objects to draw title to screen
    font = pygame.font.SysFont('timesnewroman', 60) #name and size of font
    label = font.render('Tetris', 1, (255,255,255)) #the title that will be displayed, anti-aliasing setting to 1, color of title white

    surface.blit(label, (top_left_x + play_width/2 - label.get_width()/2, 30))

    for i in range(leg(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j*30, top))


def clear_rows(grid, locked):


def draw_next_shape(shape, surface):


def draw_window(surface):
    pass


def main():
    pass


def main_menu():
    pass


main_menu()  # start game
