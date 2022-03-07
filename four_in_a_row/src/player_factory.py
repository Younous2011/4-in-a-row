from .token_factory import TokenFactory
from .color import Color
from .player import Player

class PlayerFactory:
    
    current_id = 1

    def __init__(self):
        pass

    def create(self, name:str, radius:int, color:Color, color2:Color, p_edge:float = 4 / 5):
        token = TokenFactory().create(PlayerFactory.current_id, radius, color, color2, name[0])
        player = Player(name, token)
        PlayerFactory.current_id += 1
        return player