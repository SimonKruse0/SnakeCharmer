from direction import Direction
import time
import random


def get_direction(playfield):
    time.sleep(0.02)
    dirs = [
                Direction.RIGHT,
                Direction.LEFT,
                Direction.UP,
                Direction.DOWN
            ]   
    current_position = playfield.snake_head
    if current_position[0] == 0:
        dirs.remove(Direction.UP)
    if current_position[1] == 0:
        dirs.remove(Direction.LEFT)
    if current_position[0] == playfield.length_x - 1:
        dirs.remove(Direction.DOWN)
    if current_position[1] == playfield.length_y - 1:
        dirs.remove(Direction.RIGHT)

    test_step = True
    test_n = 0
    while test_step:
        direction = random.choice(dirs)
        if direction == Direction.UP:
            pos = (current_position[0] - 1, current_position[1])
        if direction == Direction.DOWN:
            pos = (current_position[0] + 1, current_position[1])
        if direction == Direction.LEFT:
            pos = (current_position[0], current_position[1] - 1)
        if direction == Direction.RIGHT:
            pos = (current_position[0], current_position[1] + 1)
        if playfield.playarea[pos[0]][pos[1]] != 1 or test_n > 10:
            test_step = False
        test_n += 1


       
    return direction


