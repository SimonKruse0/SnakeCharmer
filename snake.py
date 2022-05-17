import numpy as np
import cv2
import random

from direction import Direction

class SnakeState:
    def __init__(self):
        self.alive = True
        self.eating = False

class Snake:
    def __init__(self, playfield, direction=None, shape=None):
        self.playfield = playfield
        self.direction = direction
        self.state = SnakeState()
        if not self.direction:
            self.direction = Direction.UP
        self.shape = shape
        if not self.shape:
            head_y = int(self.playfield.length_y / 2)
            head_x = int(self.playfield.length_x / 4)
            self.shape = []
            for delta_y in range(5, 0, -1):
                if (snake_y := head_y - delta_y) >= 0:
                    self.shape.append((head_x, snake_y))

    def stepping_in_direction(self, current_position, direction):
        if direction == Direction.UP:
            return (current_position[0] - 1, current_position[1])
        if direction == Direction.DOWN:
            return (current_position[0] + 1, current_position[1])
        if direction == Direction.LEFT:
            return (current_position[0], current_position[1] - 1)
        if direction == Direction.RIGHT:
            return (current_position[0], current_position[1] + 1)
        raise Exception("Unrecognized direction")

    def propagate(self, grow=False):
        if self.state.eating:
            self.state.eating = False
        else:
            self.shape.pop(0)
        head = self.stepping_in_direction(self.shape[-1], self.direction)
        self.shape.append(head)

    def snake_have_self_collided(self):
        has_duplicates_in_shape_list = not (sorted(list(set(self.shape))) == sorted(self.shape))
        return has_duplicates_in_shape_list

    def get_snake_head(self):
        return self.shape[-1]

    def snake_have_chrashed(self):
        snake_head = self.get_snake_head()
        if self.playfield.topology is None:
            if snake_head[0] < 0:
                return True
            if snake_head[0] >= self.playfield.length_x:
                return True
            if snake_head[1] < 0:
                return True
            if snake_head[1] >= self.playfield.length_y:
                return True
            return False
        raise Exception(f"Unknown topology encountered {self.playfield.topology}.")
            

    def eating_apple(self):
        snake_head = self.get_snake_head()
        if snake_head == self.playfield.apple:
            self.playfield.place_apple()
            return True
        return False

    def snake_is_alive(self):
        return not (self.snake_have_self_collided() or self.snake_have_chrashed())

    def set_direction(self, new_direction):
        if not self.direction.is_opposite_direction(new_direction):
            self.direction = new_direction
        raise Exception("Cannot choose opposite direction.")
 
    def update(self, direction_input=None, grow=False):
        if direction_input:
            try:
                self.set_direction(direction_input)
            except:
                pass
        self.propagate(grow=grow)
        self.state.alive = self.snake_is_alive()
        if self.state.alive:
            self.state.eating = self.eating_apple()
            self.playfield.add_snake(self)
            self.playfield.add_apple()
        else:
            self.state.eating = False
        return self.get_state()

    def get_state(self):
        return self.state

