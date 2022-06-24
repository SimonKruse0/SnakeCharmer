from typing import Iterable, Optional, Tuple

from src.enums import direction
import playingfield


class SnakeState:
    def __init__(self) -> None:
        self.alive = True
        self.eating = False


class OppositeDirectionException(Exception):
    pass


class Snake:
    def __init__(
            self,
            playing_field,
            initial_direction: Optional[direction.Direction] = None,
            shape: Optional[Iterable[Tuple[int, int]]] = None,
    ) -> None:
        self.playing_field = playing_field
        self.direction = initial_direction
        self.state = SnakeState()
        if not self.direction:
            self.direction = direction.Direction.UP
        self.shape = shape
        if not self.shape:
            head_y = int(self.playing_field.length_y / 2)
            head_x = int(self.playing_field.length_x / 4)
            self.shape = []
            for delta_y in range(5, 0, -1):
                if (snake_y := head_y - delta_y) >= 0:
                    self.shape.append((head_x, snake_y))

    @staticmethod
    def stepping_in_direction(
            current_position: Tuple[int, int], stepping_direction: direction.Direction
    ) -> Tuple[int, int]:
        if stepping_direction == direction.Direction.UP:
            return current_position[0] - 1, current_position[1]
        if stepping_direction == direction.Direction.DOWN:
            return current_position[0] + 1, current_position[1]
        if stepping_direction == direction.Direction.LEFT:
            return current_position[0], current_position[1] - 1
        if stepping_direction == direction.Direction.RIGHT:
            return current_position[0], current_position[1] + 1
        raise Exception("Unrecognized initial_direction")

    def propagate(self) -> None:
        if self.state.eating:
            self.state.eating = False
        else:
            self.shape.pop(0)
        head = self.stepping_in_direction(self.shape[-1], self.direction)
        self.shape.append(head)

    def snake_have_self_collided(self) -> bool:
        has_duplicates_in_shape_list = not (
                sorted(list(set(self.shape))) == sorted(self.shape)
        )
        return has_duplicates_in_shape_list

    def get_snake_head(self) -> Tuple[int, int]:
        return self.shape[-1]

    def snake_have_crashed(self) -> bool:
        snake_head = self.get_snake_head()
        if self.playing_field.topology is None:
            if snake_head[0] < 0:
                return True
            if snake_head[0] >= self.playing_field.length_x:
                return True
            if snake_head[1] < 0:
                return True
            if snake_head[1] >= self.playing_field.length_y:
                return True
            return False
        raise Exception(f"Unknown topology encountered {self.playing_field.topology}.")

    def eating_apple(self) -> bool:
        snake_head = self.get_snake_head()
        if snake_head == self.playing_field.apple:
            try:
                self.playing_field.place_apple()
            except playingfield.PlayingFieldException:
                pass
            return True
        return False

    def snake_is_alive(self) -> bool:
        return not (self.snake_have_self_collided() or self.snake_have_crashed())

    def set_direction(self, new_direction: direction.Direction) -> None:
        if not self.direction.is_opposite_direction(new_direction):
            self.direction = new_direction
        raise OppositeDirectionException("Cannot choose opposite initial_direction.")

    def update(
            self, direction_input: Optional[direction.Direction] = None
    ) -> SnakeState:
        if direction_input:
            try:
                self.set_direction(direction_input)
            except OppositeDirectionException:
                pass
        self.propagate()
        self.state.alive = self.snake_is_alive()
        if self.state.alive:
            self.state.eating = self.eating_apple()
            self.playing_field.add_snake(self)
            self.playing_field.add_apple()
        else:
            self.state.eating = False
        return self.get_state()

    def get_state(self) -> SnakeState:
        return self.state
