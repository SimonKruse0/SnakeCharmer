import random
from typing import List, Optional, Tuple

import cv2
import numpy as np

import snake


class PlayingFieldException(Exception):
    pass


class PlayingField:
    def __init__(
        self, length_x: int, length_y: int, topology: Optional[str] = None
    ) -> None:
        self.length_x = length_x
        self.length_y = length_y
        self.snake_head = None
        self.apple = None
        self.playing_area = np.zeros((length_x, length_y), dtype=np.int16)
        self.topology = topology
        if self.topology is not None:
            raise Exception(f"Encountered unsupported topology {self.topology}.")

    def clear_playing_area(self) -> None:
        self.playing_area = np.zeros((self.length_x, self.length_y), dtype=np.int16)

    def add_snake(self, snake: snake.Snake, value: object = 1) -> None:
        self.clear_playing_area()
        for snake_part in snake.shape:
            self.playing_area.itemset(snake_part, value)
        self.snake_head = snake.shape[-1]

    def add_apple(self) -> None:
        self.playing_area.itemset(self.apple, 2)

    def place_apple(self) -> None:
        empty_fields = self.get_empty_fields()
        if empty_fields:
            self.apple = random.choice(empty_fields)
        else:
            return
            raise PlayingFieldException("No empty space to place apple.")

    def get_empty_fields(self) -> List[Tuple[int, int]]:
        empty_fields = []
        for y in range(self.length_y):
            for x in range(self.length_x):
                if self.playing_area[x, y] == 0:
                    empty_fields.append((x, y))
        return empty_fields

    def print_playing_field(self, output: str = "terminal") -> None:
        if output == "terminal":
            for line in self.playing_area:
                for field in line:
                    print(field, end=" ")
                print("\n")
        elif output == "opencv":
            img = np.zeros((self.length_x, self.length_y, 3))
            for y in range(self.length_y):
                for x in range(self.length_x):
                    if self.playing_area[x, y] == 1:
                        img[x][y] = [255, 0, 0]
                    elif self.playing_area[x, y] == 2:
                        img[x][y] = [0, 255, 0]
            cv2.imshow("snake", img)
            cv2.waitKey(1)
