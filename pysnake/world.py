import pygame

from utils import GameConfig


class World:
    def __init__(self, cell_size=40, cell_number=20):
        self.width = cell_number * cell_size
        self.height = cell_number * cell_size
        self.screen = pygame.display.set_mode((self.width, self.height))

    def draw(self):
        self.screen.fill((110, 190, 50))
        grass_color = (167, 209, 61)
        for row in range(GameConfig.CELL_NUMBER):
            if row % 2 == 0:
                for col in range(GameConfig.CELL_NUMBER):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(
                            col * GameConfig.CELL_SIZE, row * GameConfig.CELL_SIZE, GameConfig.CELL_SIZE, GameConfig.CELL_SIZE)
                        pygame.draw.rect(self.screen, grass_color, grass_rect)
            else:
                for col in range(GameConfig.CELL_NUMBER):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(
                            col * GameConfig.CELL_SIZE, row * GameConfig.CELL_SIZE, GameConfig.CELL_SIZE, GameConfig.CELL_SIZE)
                        pygame.draw.rect(self.screen, grass_color, grass_rect)
