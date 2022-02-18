from .token import Token


class Player:
    def __init__(self, name:str, token:Token):
        self.name = name
        self.token = token