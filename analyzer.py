import datetime
import pathlib

import matplotlib.pyplot as plt
from numpy import loadtxt

import playingfield
from Directors.stupid_director import Director as currentDirector
from game import Game


class Analyzer:
    def __init__(self, game: Game) -> None:
        self.game = game
        self.output_path = pathlib.Path(r"output")

    def analyse_game(self, n_games=10):
        current_analysis_path = self.output_path.joinpath(
            datetime.datetime.now().strftime("%Y_%m_%dT%H_%M_%S")
        )
        pathlib.Path(current_analysis_path).mkdir(parents=True, exist_ok=False)
        for game_number in range(n_games):
            print(f"Game: #\t{game_number}")
            self.game.start_new_game(storage_path=current_analysis_path)
        game_data = []
        for p in pathlib.Path(current_analysis_path).joinpath("raw_data").glob("*.csv"):
            data = loadtxt(
                p.absolute(), delimiter=",", unpack=True, dtype=int, skiprows=1
            )
            game_data.append(data)
        for data in game_data:
            plt.plot(data[0], data[1], color="red", alpha=0.3)

        plt.title = "Points as a function of snake steps"
        plt.xlabel("# Snake Steps")
        plt.ylabel("Points")
        # plt.show()
        plt.savefig(current_analysis_path.joinpath(f"PointsPrStep.png"))


if __name__ == "__main__":
    my_playing_field = playingfield.PlayingField(2 * 15, 2 * 10)
    my_game = Game(
        playing_field=my_playing_field,
        # output="opencv"
        output="none",
        # output="terminal",
        direction_function=currentDirector(),
    )
    analyser = Analyzer(my_game)
    analyser.analyse_game()
