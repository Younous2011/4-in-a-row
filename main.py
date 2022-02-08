# Simple pygame program

from four_in_a_row.src.color import BLACK, GREEN_CHROMA_KEY, RED, RED_DARK, RED_LIGHT, WHITE, WHITE_ALPHA
from four_in_a_row.src.letter import Letter
from four_in_a_row.src.position import Position

# Import and initialize the pygame library

import pygame
import pygame.gfxdraw

pygame.init()

from four_in_a_row.src.token import RED_TOKEN as red_token
from four_in_a_row.src.square import BLUE_SQUARE as blue_square
from four_in_a_row.src.token import YELLOW_TOKEN as yellow_token

# Set up the drawing window

screen = pygame.display.set_mode([500, 500])

surface = pygame.Surface((200, 200))

screen.set_colorkey(GREEN_CHROMA_KEY.get(), 0)
screen.set_alpha(150)
surface.set_alpha(150)

l = Letter(Position(125, 125), "1", 200, BLACK)
# Run until the user asks to quit
list_position = [Position(0, 0)]*100

running = True

while running:

    # Did the user click the window close button?

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False


    # Fill the background with white

    screen.fill((255, 255, 255))
    

    x, y = pygame.mouse.get_pos()
    new_pos = Position(x, y)
    red_token.set_position(new_pos)

    list_position.append(new_pos)
    list_position = list_position[1:]

    yellow_token.set_position(list_position[0])

    red_token.blit_in(screen)
    yellow_token.blit_in(screen)
    blue_square.blit_in(screen)
    pygame.display.update()

# Done! Time to quit.

pygame.quit()
