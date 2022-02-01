# Simple pygame program

from four_in_a_row.src.color import BLACK, RED, RED_DARK, RED_LIGHT, WHITE, WHITE_ALPHA
from four_in_a_row.src.letter import Letter
from four_in_a_row.src.position import Position

# Import and initialize the pygame library

import pygame
import pygame.gfxdraw

pygame.init()


# Set up the drawing window

screen = pygame.display.set_mode([500, 500])

l = Letter(Position(125, 125), "1", 200, BLACK)
l.make()
# Run until the user asks to quit

running = True

while running:

    # Did the user click the window close button?

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False


    # Fill the background with white

    screen.fill((255, 255, 255))


    # Draw a solid blue circle in the center

    pygame.draw.circle(screen, RED.get(), (100, 250), 95)
    pygame.draw.circle(screen, RED_DARK.get(), (100, 250), 75)

    pygame.gfxdraw.filled_circle(screen, 300, 250, 95, RED.get())
    pygame.gfxdraw.filled_circle(screen, 300, 250, 75, RED_DARK.get())


    # Flip the display

    # pygame.display.flip()
    l.draw(screen)
    pygame.display.update()

# Done! Time to quit.

pygame.quit()
