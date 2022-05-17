#from manual_direction import get_manual_direction as direction_function
from stupid_director import get_direction as direction_function

from snake import Snake, SnakeState
from playfield import Playfield

import os

class Game:
    def __init__(self, playfield=None, output="terminal",direction_function = direction_function):
        self.playfield = playfield
        self.direction_funtion = direction_function
        self.output = output
        if not self.playfield:
            self.playfield = Playfield(16, 16)
        self.snake = Snake(self.playfield)
        self.snake.playfield.add_snake(self.snake)
        self.snake.playfield.place_apple()
        self.snake.playfield.add_apple()
        self.points = self.reset_points()

    def reset_points(self):
        return {"apples": 0}

    def play_step(self):
        direction = self.direction_funtion(self.snake.playfield)
        snake_state = self.snake.update(direction_input=direction)
        os.system('cls' if os.name == 'nt' else 'clear')
        self.playfield.print_playfield(self.output)
        return snake_state

    def reset_game(self):
        pass

    def start_new_game(self):
        self.reset_game()
        snake_state = SnakeState()
        while snake_state.alive:
            snake_state = my_game.play_step()
            self.update_points(snake_state)
        print(f"Points: {self.calculate_points()}")

    def calculate_points(self):
        return self.points["apples"]

    def update_points(self, snake_state):
        if snake_state.eating:
            self.points["apples"] += 1

if __name__ == "__main__":
    my_playfield = Playfield(8, 8)
    my_game = Game(
            playfield=my_playfield,
            #output="opencv"
            output="terminal"
            )
    my_game.start_new_game()
