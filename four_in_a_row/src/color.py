class Color:
    def __init__(self, r:int, g:int, b:int):
        self.r = r
        self.g = g
        self.b = b

    def get(self) -> tuple:
        return self.r, self.g, self.b


RED_DARK = Color(147, 27, 16)
RED_LIGHT = Color(255, 100, 92)
RED = Color(255, 0, 0)

YELLOW_DARK = Color(222, 229, 16)
YELLOW_LIGHT = Color(242, 246, 121)
YELLOW = Color(255, 255, 0)

BROWN_DARK = Color(82, 46, 0)
BROWN_LIGHT = Color(224, 127, 0)
BROWN = Color(143, 81, 0)

BLACK = Color(0, 0, 0)

WHITE = Color(255, 255, 255)