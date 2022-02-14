# Imports base class and colors
from four_in_a_row.src.color import BLACK, RED, WHITE
from four_in_a_row.src.position import Position
from four_in_a_row.src.grill import Grill

# Import pygame
import pygame
import pygame.gfxdraw

# Init pygame
pygame.init()

# Import after init
from four_in_a_row.src.token import YELLOW_TOKEN as yellow_token
from four_in_a_row.src.token_factory import TokenFactory

# Create all variables
nb_lignes = 6
nb_colonnes = 7
l_box = 120

l_grill = l_box * 6 # 150 x 6 = 900
L_grill = l_box * 7 # 200 x 7 = 1050

# Width and height of my pygame-window
screen = pygame.display.set_mode([L_grill, l_grill + l_box])

# Create variables with value Class
p = Position(0, l_box)
g = Grill(l_box, nb_lignes, nb_colonnes, p)



# l = Letter(Position(125, 125), "1", 200, BLACK)

# Run until the user asks to quit
token = TokenFactory().create(1, l_box // 2, RED, BLACK, "B")

running = True

while running:

    # Did the user click the window close button?

    x, y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        # handle MOUSEBUTTONUP
        if event.type == pygame.MOUSEBUTTONUP:
            print(f"Vous êtes sur la colonne {Position(x, 0).get_column(l_box)}")

        if event.type == pygame.QUIT:
            running = False


    # Fill the background with white
    screen.fill(WHITE.get())
    

    x, y = pygame.mouse.get_pos()
    new_pos = Position(x, l_box // 2)

    # set_position of tokens
    token.set_position(new_pos)
    yellow_token.set_position(Position(l_box // 2, L_grill - (l_box // 2)))

    # blit_in tokens
    token.blit_in(screen)
    yellow_token.blit_in(screen)
    g.blit_in(screen)

    # Update display-pygame
    pygame.display.update()

# Done! Time to quit.
pygame.quit()