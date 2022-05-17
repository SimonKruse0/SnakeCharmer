from direction import Direction
import getch

def get_manual_direction(playfield):
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


