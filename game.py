# from manual_direction import get_manual_direction as current_direction_function
from typing import Callable, Dict, Optional

from stupid_director import Director as currentDirector

import snake
import playingfield

import os


class Game:
    def __init__(
        self,
        playing_field: Optional[playingfield.PlayingField] = None,
        output: str = "terminal",
        direction_function: object = currentDirector(),
    ) -> None:
        self.game_n = 0
        self.playing_field = playing_field
        self.direction_function = direction_function
        self.output = output
        if not self.playing_field:
            self.playing_field = playingfield.PlayingField(16, 16)

    @staticmethod
    def get_zeroed_points() -> Dict[str, int]:
        return {"apples": 0}

    def play_step(self) -> snake.SnakeState:
        direction = self.direction_function.get_direction(self.snake.playing_field)
        snake_state = self.snake.update(direction_input=direction)
        # os.system("cls" if os.name == "nt" else "clear")
        self.playing_field.print_playing_field(self.output)
        return snake_state

    def reset_game(self) -> None:
        self.step_n = 0
        self.game_n += 1
        self.snake = snake.Snake(self.playing_field)
        self.snake.playing_field.add_snake(self.snake)
        self.snake.playing_field.place_apple()
        self.snake.playing_field.add_apple()
        self.points = self.get_zeroed_points()

    def start_new_game(self, name=None) -> None:
        self.reset_game()
        if name:
            self.name = name
        else:
            self.name = f"game_{self.game_n}"
        self.analysis_file = open(f"output/{self.name}.csv", "w")
        self.analysis_file.write("step_n,points\n")
        self.analysis_file.write("0,0\n")
        snake_state = snake.SnakeState()
        while snake_state.alive:
            snake_state = my_game.play_step()
            self.update_points(snake_state)
            self.step_n += 1
        self.analysis_file.close()
        print(f"Points: {self.calculate_points()}")

    def calculate_points(self) -> int:
        return self.points["apples"]

    def update_points(self, snake_state: snake.SnakeState) -> None:
        if snake_state.eating:
            self.points["apples"] += 1
            if self.analysis_file:
                self.analysis_file.write(f"{self.step_n},{self.calculate_points()}\n")


if __name__ == "__main__":
    my_playing_field = playingfield.PlayingField(2*5, 2*5)
    my_game = Game(
        playing_field=my_playing_field,
        output="opencv"
        # output="none"
        # output="terminal",
    )
    for game_number in range(5):
        my_game.start_new_game()
