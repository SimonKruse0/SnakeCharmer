from direction import Direction
import getch

from playingfield import PlayingField


def get_manual_direction(playing_field: PlayingField) -> Direction:
    direction = None
    while not direction:
        direction_input = getch.getch()
        if direction_input == "i":
            direction = Direction.UP
        if direction_input == "k":
            direction = Direction.DOWN
        if direction_input == "l":
            direction = Direction.RIGHT
        if direction_input == "j":
            direction = Direction.LEFT
    return direction
