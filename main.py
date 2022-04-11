# Import pygame
import pygame
from four_in_a_row.src.conf import Conf

# Init pygame
pygame.init()

import os

import argparse
parser = argparse.ArgumentParser()

parser.add_argument('-n1', '--name-player-1', help='Give the name of the first player.',  required=True)
parser.add_argument('-n2', '--name-player-2', help='Give the name of the second player.',  required=True)
parser.add_argument('-nr', '--number-rows', help='Give the number of rows.', default=5, type=int)
parser.add_argument('-nc', '--number-columns', help='Give the number of columns.', default=8, type=int)

args = parser.parse_args()

name1 = args.name_player_1
name2 = args.name_player_2
nr = args.number_rows
nc = args.number_columns


drivers = ['x11', 'directfb', 'fbcon', 'svgalib']

found = False
for driver in drivers:
    if not os.getenv('SDL_VIDEODRIVER'):
        os.environ['SDL_VIDEODRIVER'] = driver
    try:
        pygame.display.init()
    except pygame.error:
        print('Driver: {0} failed.'.format(driver))
        continue
    found = True
    break

if not found:
   raise Exception('No suitable video driver found!')
   


# Import after init
from four_in_a_row.src.game_factory import GameFactory


conf = Conf(nr, nc)
game = GameFactory().create(conf, name1, name2)

running = True
while running:
    x, y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            game.click(x)

        if event.type == pygame.QUIT:
            running = False

    game.update()
    pygame.display.update()

# Done! Time to quit.
pygame.quit()