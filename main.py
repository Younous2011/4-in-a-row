# Simple pygame program

from four_in_a_row.src.color import RED, RED_DARK, RED_LIGHT

# Import and initialize the pygame library

import pygame

pygame.init()


# Set up the drawing window

screen = pygame.display.set_mode([500, 500])
font = pygame.font.Font(None, 60)
text = font.render("Y", True, RED_DARK.get(), None)
textRect = text.get_rect()
textRect.center = (500 // 2, 500 // 2)
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

    pygame.draw.circle(screen, RED_DARK.get(), (250, 250), 85)
    pygame.draw.circle(screen, RED.get(), (250, 250), 75)



    # Flip the display

    # pygame.display.flip()
    screen.blit(text, textRect)
    pygame.display.update()

# Done! Time to quit.

pygame.quit()
