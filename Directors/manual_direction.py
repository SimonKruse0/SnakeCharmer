import getch

from src.enums import direction
import playingfield
from Directors.base_director import BaseDirector


class Director(BaseDirector):
    def __init__(self) -> None:
        pass

    def get_direction(
        self, playing_field: playingfield.PlayingField
    ) -> direction.Direction:
        chosen_direction = None
        while not chosen_direction:
            direction_input = getch.getch()
            if direction_input == "i":
                chosen_direction = direction.Direction.UP
            if direction_input == "k":
                chosen_direction = direction.Direction.DOWN
            if direction_input == "l":
                chosen_direction = direction.Direction.RIGHT
            if direction_input == "j":
                chosen_direction = direction.Direction.LEFT
        return chosen_direction
