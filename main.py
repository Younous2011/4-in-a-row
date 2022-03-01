# Import pygame
import pygame

from four_in_a_row.src.position import Position

# Init pygame
pygame.init()

# Import after init
from four_in_a_row.src.game_factory import GameFactory

# Create all variables
nb_lignes = 5
nb_colonnes = 8
side = 120

game = GameFactory().create(side, nb_lignes, nb_colonnes, "Younous", "Soufiane")

running = True
while running:
    x, y = pygame.mouse.get_pos()
    print(
        Position(x, y).get_column(side, 3),
        x, y
    )
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            game.click(x)

        if event.type == pygame.QUIT:
            running = False

    game.update()

    pygame.display.update()

# Done! Time to quit.
pygame.quit()