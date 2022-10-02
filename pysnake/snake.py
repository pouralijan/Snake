import random
import pygame
import pathlib
import os
from utils import Point, GameConfig

CWD = pathlib.Path(__file__).cwd()


class Snake:
    class Head():
        def __init__(self):
            self.UP = pygame.image.load(os.path.join(
                CWD, "assets/images/head_up.png")).convert_alpha()
            self.DOWN = pygame.image.load(os.path.join(
                CWD, "assets/images/head_down.png")).convert_alpha()
            self.LEFT = pygame.image.load(os.path.join(
                CWD, "assets/images/head_left.png")).convert_alpha()
            self.RIGHT = pygame.image.load(os.path.join(
                CWD, "assets/images/head_right.png")).convert_alpha()

        def head(self, direction):
            if direction == Point.UP:
                return self.UP
            elif direction == Point.DOWN:
                return self.DOWN
            elif direction == Point.LEFT:
                return self.LEFT
            elif direction == Point.RIGHT:
                return self.RIGHT

    class Body():
        def __init__(self):
            self.HORIZONTAL = pygame.image.load(os.path.join(
                CWD, "assets/images/body_horizontal.png")).convert_alpha()
            self.VERTICAL = pygame.image.load(os.path.join(
                CWD, "assets/images/body_vertical.png")).convert_alpha()
            self.BOTTOMLEFT = pygame.image.load(os.path.join(
                CWD, "assets/images/body_bottomleft.png")).convert_alpha()
            self.BOTTOMRIGHT = pygame.image.load(os.path.join(
                CWD, "assets/images/body_bottomright.png")).convert_alpha()
            self.TOPLEFT = pygame.image.load(os.path.join(
                CWD, "assets/images/body_topleft.png")).convert_alpha()
            self.TOPRIGHT = pygame.image.load(os.path.join(
                CWD, "assets/images/body_topright.png")).convert_alpha()

    class Tail():
        def __init__(self):
            self.UP = pygame.image.load(os.path.join(
                CWD, "assets/images/tail_up.png")).convert_alpha()
            self.DOWN = pygame.image.load(os.path.join(
                CWD, "assets/images/tail_down.png")).convert_alpha()
            self.LEFT = pygame.image.load(os.path.join(
                CWD, "assets/images/tail_left.png")).convert_alpha()
            self.RIGHT = pygame.image.load(os.path.join(
                CWD, "assets/images/tail_right.png")).convert_alpha()

        def tail(self, direction):
            print(direction)
            if direction == Point.UP:
                return self.DOWN
            elif direction == Point.DOWN:
                return self.UP
            elif direction == Point.LEFT:
                return self.RIGHT
            elif direction == Point.RIGHT:
                return self.LEFT

    def __init__(self) -> None:
        self.position = Point(random.randint(
            0, GameConfig.CELL_NUMBER - 1), random.randint(0, GameConfig.CELL_NUMBER - 1))
        self.direction = Point.LEFT
        self.score = 0
        self.new_score = False
        self.head = Snake.Head()
        self.body = Snake.Body()
        self.tail = Snake.Tail()
        self.bodys = [
            self.position - Point.LEFT,
            self.position - Point.LEFT * 2,
            self.position - Point.LEFT * 3,
        ]

    def score_up(self):
        self.score += 1
        self.new_score = True

    def draw(self, surface):
        head = self.head.head(self.direction)
        tail = self.tail.tail(self.bodys[-2] - self.bodys[-1])
        for index, body in enumerate(self.bodys):
            x_pos = body.x * GameConfig.CELL_SIZE
            y_pos = body.y * GameConfig.CELL_SIZE
            body_rect = pygame.Rect(
                x_pos, y_pos, GameConfig.CELL_SIZE, GameConfig.CELL_SIZE)
            if index == 0:
                surface.blit(head, body_rect)
            elif index == len(self.bodys) - 1:
                surface.blit(tail, body_rect)
            else:
                previous_body = self.bodys[index + 1] - body
                next_body = self.bodys[index - 1] - body
                if previous_body.x == next_body.x:
                    surface.blit(self.body.VERTICAL, body_rect)
                elif previous_body.y == next_body.y:
                    surface.blit(self.body.HORIZONTAL, body_rect)
                else:
                    if previous_body.x == -1 and next_body.y == -1 or previous_body.y == -1 and next_body.x == -1:
                        surface.blit(self.body.TOPLEFT, body_rect)
                    elif previous_body.x == -1 and next_body.y == 1 or previous_body.y == 1 and next_body.x == -1:
                        surface.blit(self.body.BOTTOMLEFT, body_rect)
                    elif previous_body.x == 1 and next_body.y == -1 or previous_body.y == -1 and next_body.x == 1:
                        surface.blit(self.body.TOPRIGHT, body_rect)
                    elif previous_body.x == 1 and next_body.y == 1 or previous_body.y == 1 and next_body.x == 1:
                        surface.blit(self.body.BOTTOMRIGHT, body_rect)

    def move(self):
        if self.new_score:
            body_copy = self.bodys[:]
        else:
            body_copy = self.bodys[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.bodys = body_copy[:]
        self.position = self.bodys[0]
        self.new_score = False

    def change_direction(self, direction: Point):
        if self.direction == Point.LEFT and direction == Point.RIGHT:
            return
        if self.direction == Point.RIGHT and direction == Point.LEFT:
            return
        if self.direction == Point.DOWN and direction == Point.UP:
            return
        if self.direction == Point.UP and direction == Point.DOWN:
            return

        self.direction = direction

    def self_collition_check(self):
        return self.bodys[0] in self.bodys[1:]
