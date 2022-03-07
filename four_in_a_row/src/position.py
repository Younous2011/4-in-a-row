class Position:
    def __init__(self, x:int = 0, y:int = 0):
        self.x = x
        self.y = y

    def set_position(self, x:int, y:int):
        self.x = x
        self.y = y

    def get_position(self):
        return self.x, self.y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_top_left_position(self, radius:int):
        top_x = self.x - radius
        top_y = self.y - radius
        return top_x, top_y

    def get_column(self, side:int, translation:int) -> int:
        return self.x // side - translation

    def get_position_token(self, i:int, j:int, l_box:int, L_grill:int):
        x = l_box // 2 + l_box * j
        y = L_grill - (l_box // 2) - l_box * i
        return Position(x, y)
