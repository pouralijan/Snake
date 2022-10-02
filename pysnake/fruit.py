import random
import os
import pygame
import pathlib
from utils import GameConfig, Point

CWD = pathlib.Path(__file__).cwd()

class Fruit:
    def __init__(self) -> None:
        self.position: Point
        self.spawn()
        apple_path = os.path.join(CWD, "assets/images/apple.png")
        self.apple = pygame.image.load(apple_path).convert_alpha()

    def spawn(self):
        self.position = Point(random.randint(
            0, GameConfig.CELL_NUMBER - 1), random.randint(0, GameConfig.CELL_NUMBER - 1))

    def draw(self, surface):
        fruit_rect = pygame.Rect(self.position.x * GameConfig.CELL_SIZE, self.position.y *
                                 GameConfig.CELL_SIZE, GameConfig.CELL_SIZE, GameConfig.CELL_SIZE)
        surface.blit(self.apple, fruit_rect)
