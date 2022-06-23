# from manual_direction import get_manual_direction as current_direction_function

import pathlib
import shutil
from typing import Dict, Optional

import matplotlib.pyplot as plt
from numpy import loadtxt

import playingfield
import snake
from base_director import BaseDirector
from game import Game
from stupid_director import Director as currentDirector


class Analyzer:
    def __init__(
            self,
            game: Game
    ) -> None:
        self.game = game

    def analyse_game(self):
        path = r"./output"
        shutil.rmtree(path, ignore_errors=True)
        pathlib.Path(path).mkdir(parents=True, exist_ok=True)


        for game_number in range(10):
            print(f"Game: #\t{game_number}")
            self.game.start_new_game()

        game_data = []

        for p in pathlib.Path(path).glob("*.csv"):
            # print(f"{p.name}:\n{p.read_text()}\n")
            # data = np.genfromtxt(
            #     p.absolute(),
            #     delimiter=",", dtype=float, names=True
            # )
            data = loadtxt(p.absolute(), delimiter=",", unpack=True, dtype=int, skiprows=1)
            game_data.append(data)
        for data in game_data:
            plt.plot(data[0], data[1], color="red", alpha=0.3)

        plt.title = "Points as a function of snake steps"
        plt.xlabel("# Snake Steps")
        plt.ylabel("Points")
        # plt.show()
        plt.savefig("./output/PointsPrStep.png")


if __name__ == "__main__":

    my_playing_field = playingfield.PlayingField(2 * 10, 2 * 10)
    my_game = Game(
        playing_field=my_playing_field,
        # output="opencv"
        output="none",
        # output="terminal",
        direction_function=currentDirector(),
    )

    analyser = Analyzer(my_game)
    analyser.analyse_game()