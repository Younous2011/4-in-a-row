# Import pygame
import pygame
import pygame.gfxdraw

# Init pygame
pygame.init()

# Import after init
# Imports base class and colors
from four_in_a_row.src.color import RED, RED_DARK, WHITE, YELLOW, YELLOW_DARK
from four_in_a_row.src.position import Position
from four_in_a_row.src.token import YELLOW_TOKEN as yellow_token
from four_in_a_row.src.game_factory import GameFactory

# Create all variables
nb_lignes = 5
nb_colonnes = 8
l_box = 120

l_grill = l_box * nb_lignes
L_grill = l_box * nb_colonnes

# Width and height of my pygame-window
screen = pygame.display.set_mode([L_grill, l_grill + l_box])

game = GameFactory().create(l_box, nb_lignes, nb_colonnes, "Younous", "Soufiane")

# l = Letter(Position(125, 125), "1", 200, BLACK)

i = 0

running = True

while running:

    x, y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            game.click(x)

        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill(WHITE.get())
    
    x, y = pygame.mouse.get_pos()
    new_pos = Position(x, l_box // 2)

    game.current_player.token.set_position(new_pos)
    game.current_player.token.blit_in(screen)
    
    game.grill_token.blit_in(screen)
    game.grill_box.blit_in(screen)

    # Update display-pygame
    pygame.display.update()

# Done! Time to quit.
pygame.quit()