class Position:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

    def set_position(self, x:int, y:int):
        self.x = x
        self.y = y

    def get_position(self):
        return self.x, self.y