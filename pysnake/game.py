import pygame
from snake import Snake
from world import World
from fruit import Fruit
from utils import GameConfig, Point

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.running = True
        self.world = World()
        self.fruit = Fruit()
        self.snakes : list[Snake] = []
        self.screen_update = pygame.USEREVENT
        pygame.time.set_timer(self.screen_update, 150)

    def __del__(self):
        pygame.quit()

    def add_snake(self, snake:Snake):
        self.snakes.append(snake)


    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == self.screen_update:
                for snake in self.snakes:
                    snake.move()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snakes[0].change_direction(Point.UP)
                if event.key == pygame.K_RIGHT:
                    self.snakes[0].change_direction(Point.RIGHT)
                if event.key == pygame.K_DOWN:
                    self.snakes[0].change_direction(Point.DOWN)
                if event.key == pygame.K_LEFT:
                    self.snakes[0].change_direction(Point.LEFT)

    def check_collision(self):
        for snake in self.snakes:
            if snake.position == self.fruit.position:
                self.fruit.spawn()
                snake.score_up()

            if snake.self_collition_check():
                self.running = False
                print("Game Over")
            if not 0 <= snake.position.x <= GameConfig.CELL_NUMBER or  not 0 <= snake.position.y <= GameConfig.CELL_NUMBER:
                self.running = False
                print("Game Over")

    def run(self):
        while self.running:
            self.check_event()
            self.world.draw()
            self.check_collision()
            self.fruit.draw(self.world.screen)
            for snake in self.snakes:
                snake.draw(self.world.screen)
            pygame.display.update()
            self.clock.tick(150)