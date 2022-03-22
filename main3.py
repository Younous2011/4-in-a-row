import pygame

pygame.init()
screen = pygame.display.set_mode((500, 200))

from four_in_a_row.src.text_input import TextInput
from four_in_a_row.src.position import Position
from four_in_a_row.src.color import BLACK, GREY, WHITE
from four_in_a_row.src.button import Button

ti = TextInput(Position(0, 0), 20, BLACK, GREY, (300, 30))
ti2 = TextInput(Position(0, 50), 20, BLACK, GREY, (300, 30))
button = Button(Position(0, 100), "Click here !", 40, WHITE, BLACK, (100, 30))

run = True
while run:
    event_list = pygame.event.get()
    ti.on_event(event_list)
    ti2.on_event(event_list)
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False 

    screen.fill((255, 255, 255))
    ti.blit_in(screen)
    ti2.blit_in(screen)
    pygame.display.update()

pygame.quit()
exit()