import pygame

pygame.init()
window = pygame.display.set_mode((500, 200))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 100)

from four_in_a_row.src.input import Input

text_input_box = Input(50, 50, 400, font)
text_input_box2 = Input(100, 100, 400, font)
group = pygame.sprite.Group(text_input_box)

run = True
while run:
    clock.tick(60)
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False 
    text_input_box.update((event_list))
    text_input_box2.update((event_list))

    window.fill(0)
    text_input_box.draw(window)
    pygame.display.flip()

pygame.quit()
exit()
