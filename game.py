# from manual_direction import get_manual_direction as current_direction_function
from typing import Callable, Dict, Optional

from stupid_director import get_direction as current_direction_function

from snake import Snake, SnakeState
from playingfield import PlayingField

import os


class Game:
    def __init__(
        self,
        playing_field: Optional[PlayingField] = None,
        output: str = "terminal",
        direction_function: Callable = current_direction_function,
    ) -> None:
        self.playing_field = playing_field
        self.direction_function = direction_function
        self.output = output
        if not self.playing_field:
            self.playing_field = PlayingField(16, 16)
        self.snake = Snake(self.playing_field)
        self.snake.playing_field.add_snake(self.snake)
        self.snake.playing_field.place_apple()
        self.snake.playing_field.add_apple()
        self.points = self.get_zeroed_points()

    @staticmethod
    def get_zeroed_points() -> Dict[str:int]:
        return {"apples": 0}

    def play_step(self) -> SnakeState:
        direction = self.direction_function(self.snake.playing_field)
        snake_state = self.snake.update(direction_input=direction)
        os.system("cls" if os.name == "nt" else "clear")
        self.playing_field.print_playing_field(self.output)
        return snake_state

    def reset_game(self) -> None:
        pass

    def set_state_to_new_game(self) -> None:
        self.reset_game()
        snake_state = SnakeState()
        while snake_state.alive:
            snake_state = my_game.play_step()
            self.update_points(snake_state)
        print(f"Points: {self.calculate_points()}")

    def calculate_points(self) -> int:
        return self.points["apples"]

    def update_points(self, snake_state: SnakeState) -> None:
        if snake_state.eating:
            self.points["apples"] += 1


if __name__ == "__main__":
    my_playing_field = PlayingField(8, 8)
    my_game = Game(
        playing_field=my_playing_field,
        # output="opencv"
        output="terminal",
    )
    my_game.set_state_to_new_game()
