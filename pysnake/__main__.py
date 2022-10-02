#!/usr/bin/env python3
from snake import Snake
from game import Game
def main():
    game = Game()
    snake = Snake()
    game.add_snake(snake)
    game.run()

if __name__ == "__main__":
    main()
