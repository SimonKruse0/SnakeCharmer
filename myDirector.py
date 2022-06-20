import direction
import time
import random

import playingfield


class Director:
    def __init__(self):
        self.firstrun = True

    def get_direction(
        self, playing_field: playingfield.PlayingField
    ) -> direction.Direction:

        dirs = [
            direction.Direction.RIGHT,
            direction.Direction.LEFT,
            direction.Direction.UP,
            direction.Direction.DOWN,
        ]

        current_position = playing_field.snake_head

        chosen_direction = dirs[0]

        if self.firstrun:
            self.firstrun = False
            return direction.Direction.UP

        if current_position[1] == playing_field.length_x - 1:
            return direction.Direction.UP


        if current_position[0] == playing_field.length_y - 1:
            return direction.Direction.RIGHT

        if current_position[1] == 0:
            return direction.Direction.DOWN



        return direction.Direction.LEFT

    # def get_direction(playing_field: playingfield.PlayingField) -> direction.Direction:
    #     time.sleep(0.02)
    #     dirs = [direction.Direction.RIGHT, direction.Direction.LEFT, direction.Direction.UP, direction.Direction.DOWN]
    #     current_position = playing_field.snake_head
    #     if current_position[0] == 0:
    #         dirs.remove(direction.Direction.UP)
    #     if current_position[1] == 0:
    #         dirs.remove(direction.Direction.LEFT)
    #     if current_position[0] == playing_field.length_x - 1:
    #         dirs.remove(direction.Direction.DOWN)
    #     if current_position[1] == playing_field.length_y - 1:
    #         dirs.remove(direction.Direction.RIGHT)
    #
    #     chosen_direction = random.choice(dirs)
    #     test_step = True
    #     test_n = 0
    #     while test_step:
    #         if chosen_direction == direction.Direction.UP:
    #             pos = (current_position[0] - 1, current_position[1])
    #         elif chosen_direction == direction.Direction.DOWN:
    #             pos = (current_position[0] + 1, current_position[1])
    #         elif chosen_direction == direction.Direction.LEFT:
    #             pos = (current_position[0], current_position[1] - 1)
    #         elif chosen_direction == direction.Direction.RIGHT:
    #             pos = (current_position[0], current_position[1] + 1)
    #         else:
    #             raise Exception("Non recognized initial_direction encountered.")
    #         if playing_field.playing_area[pos[0]][pos[1]] != 1 or test_n > 10:
    #             test_step = False
    #         test_n += 1
    #
    #     return chosen_direction
