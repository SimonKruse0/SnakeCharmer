from direction import Direction
import time
import random

from playingfield import PlayingField


def get_direction(playing_field: PlayingField) -> Direction:
    time.sleep(0.02)
    dirs = [Direction.RIGHT, Direction.LEFT, Direction.UP, Direction.DOWN]
    current_position = playing_field.snake_head
    if current_position[0] == 0:
        dirs.remove(Direction.UP)
    if current_position[1] == 0:
        dirs.remove(Direction.LEFT)
    if current_position[0] == playing_field.length_x - 1:
        dirs.remove(Direction.DOWN)
    if current_position[1] == playing_field.length_y - 1:
        dirs.remove(Direction.RIGHT)

    direction = random.choice(dirs)
    test_step = True
    test_n = 0
    while test_step:
        if direction == Direction.UP:
            pos = (current_position[0] - 1, current_position[1])
        elif direction == Direction.DOWN:
            pos = (current_position[0] + 1, current_position[1])
        elif direction == Direction.LEFT:
            pos = (current_position[0], current_position[1] - 1)
        elif direction == Direction.RIGHT:
            pos = (current_position[0], current_position[1] + 1)
        else:
            raise Exception("Non recognized direction encountered.")
        if playing_field.playing_area[pos[0]][pos[1]] != 1 or test_n > 10:
            test_step = False
        test_n += 1

    return direction
