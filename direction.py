from enum import Enum


class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

    def is_opposite_direction(self, direction) -> bool:
        if self == Direction.UP:
            return direction == Direction.DOWN
        if self == Direction.DOWN:
            return direction == Direction.UP
        if self == Direction.RIGHT:
            return direction == Direction.LEFT
        if self == Direction.LEFT:
            return direction == Direction.RIGHT
        raise Exception("Unknown direction encountered.")
