class Color:
    def __init__(self, r:int, g:int, b:int, a:int = None):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def get(self) -> tuple:
        if self.a == None:
            return self.r, self.g, self.b
        else:
            return self.r, self.g, self.b, self.a


RED_DARK = Color(211, 47, 47)
RED_LIGHT = Color(255, 100, 92)
RED = Color(244,67,54)

YELLOW_DARK = Color(227, 233, 53)
YELLOW_LIGHT = Color(242, 246, 121)
YELLOW = Color(255, 255, 0)

BROWN_DARK = Color(82, 46, 0)
BROWN_LIGHT = Color(224, 127, 0)
BROWN = Color(143, 81, 0)

BLUE = Color(62, 104, 182)

GREEN_CHROMA_KEY = Color(0, 177, 64)

BLACK = Color(0, 0, 0)

WHITE = Color(255, 255, 255)
WHITE_ALPHA = Color(255, 255, 255, 50)