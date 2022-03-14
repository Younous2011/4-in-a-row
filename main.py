# Import pygame
import pygame
from four_in_a_row.src.conf import Conf

# Init pygame
pygame.init()

# Import after init
from four_in_a_row.src.game_factory import GameFactory

# Create all variables
nb_lignes = 5
nb_colonnes = 8
side = 120

conf = Conf()
game = GameFactory().create(conf, "Hamza", "Younous")

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