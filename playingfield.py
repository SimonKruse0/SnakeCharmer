import random
from typing import List, Optional, Tuple

import cv2
import numpy as np

import snake
from src.enums.game_display import GameDisplay


class PlayingFieldException(Exception):
    pass


def resize_playfield(img: np.ndarray, min_size: int) -> np.ndarray:
    if img.shape[0] < min_size or img.shape[1] < min_size:
        scale_factor = max(min_size / img.shape[0], min_size / img.shape[1])
        img = cv2.resize(
            img,
            (0, 0),
            fx=scale_factor,
            fy=scale_factor,
            interpolation=cv2.INTER_AREA,
        )
    return img


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
            raise PlayingFieldException("No empty space to place apple.")

    def get_empty_fields(self) -> List[Tuple[int, int]]:
        empty_fields = []
        for y in range(self.length_y):
            for x in range(self.length_x):
                if self.playing_area[x, y] == 0:
                    empty_fields.append((x, y))
        return empty_fields

    def print_playing_field(self, output: GameDisplay, **kwargs) -> None:
        if output == GameDisplay.terminal:
            for line in self.playing_area:
                for field in line:
                    print(field, end=" ")
                print("\n")
        elif output == GameDisplay.opencv:
            img = np.zeros((self.length_x, self.length_y, 3))
            for y in range(self.length_y):
                for x in range(self.length_x):
                    if self.playing_area[x, y] == 1:
                        img[x][y] = [255, 0, 0]
                    elif self.playing_area[x, y] == 2:
                        img[x][y] = [0, 255, 0]
            if output_size := kwargs.get("output_size"):
                img = resize_playfield(img, output_size)
            cv2.imshow("snake", img)
            cv2.waitKey(1)
        return
