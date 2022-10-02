from pygame.math import Vector2

class GameConfig:
    CELL_SIZE = 40
    CELL_NUMBER = 20
    

class Point(Vector2):
    LEFT = Vector2(-1, 0)
    RIGHT = Vector2(1, 0)
    UP = Vector2(0, -1)
    DOWN = Vector2(0, 1)