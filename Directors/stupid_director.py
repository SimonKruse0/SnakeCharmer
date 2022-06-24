from typing import Optional

import numpy as np

from src.enums import direction
import playingfield
from Directors.base_director import BaseDirector


class Director(BaseDirector):
    def __init__(self) -> None:
        self.first_run = True
        self.toEnd = True
        self.toHome = True
        self.n = True

    def going_home(self, playing_field: playingfield.PlayingField):

        current_position = playing_field.snake_head

        if current_position == (0, playing_field.length_y - 1):
            self.toEnd = False
        if current_position == (0, 0):
            self.n += 1
            self.toHome = False
            return None
        if self.toEnd:
            if current_position[1] == playing_field.length_y - 1:
                return direction.Direction.UP
            return direction.Direction.RIGHT
        if self.toHome:
            return direction.Direction.LEFT

    @staticmethod
    def snaker(playing_field: playingfield.PlayingField) -> direction.Direction:
        current_position = playing_field.snake_head

        if current_position[0] == 0:
            if current_position[1] == 0:
                return direction.Direction.DOWN
            return direction.Direction.LEFT

        if current_position[1] == playing_field.length_y - 1:
            return direction.Direction.UP

        if current_position[0] == 1:
            if current_position[1] % 2 == 0:
                return direction.Direction.DOWN
            return direction.Direction.RIGHT

        if current_position[0] == playing_field.length_x - 1:
            if current_position[1] % 2 == 0:
                return direction.Direction.RIGHT
            return direction.Direction.UP

        if current_position[1] % 2 == 0:
            return direction.Direction.DOWN

        return direction.Direction.UP

    def get_direction(
        self, playing_field: playingfield.PlayingField
    ) -> direction.Direction:

        if (
            np.count_nonzero(playing_field.playing_area)
            / playing_field.playing_area.size
            < 0.6
        ):
            if go_straight := self.go_straight(playing_field):
                return go_straight

        if skip_to_end := self.skip_to_end(playing_field):
            return skip_to_end

        return self.snaker(playing_field)

    @staticmethod
    def go_straight(
            playing_field: playingfield.PlayingField
    ) -> Optional[direction.Direction]:
        apple = playing_field.apple
        current_position = playing_field.snake_head

        for line in playing_field.playing_area[1:]:
            if 1 in line[current_position[1] + 1 : apple[1] + 1]:
                return None

        if current_position[0] == apple[0] or apple[0] == 0:
            if current_position[1] < apple[1]:
                return direction.Direction.RIGHT
        return None

    @staticmethod
    def skip_to_end(
            playing_field: playingfield.PlayingField
    ) -> Optional[direction.Direction]:
        apple = playing_field.apple
        current_position = playing_field.snake_head
        if current_position[0] == 0:
            return None

        for line in playing_field.playing_area[0:]:
            if 1 in line[current_position[1] + 1 :]:
                return None

        for line in playing_field.playing_area[1:]:
            if 1 in line[current_position[1] + 1 :]:
                return None

        if current_position[1] > apple[1]:
            if (
                playing_field.playing_area[current_position[0] - 1][current_position[1]]
                != 1
            ):
                return direction.Direction.UP
        return None
