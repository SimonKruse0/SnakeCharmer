import pathlib
import shutil
import analyzer
import matplotlib.pyplot as plt
from numpy import loadtxt

import playingfield
from game import Game
import src.enums.game_display as display
from Directors.stupid_director import Director as currentDirector


my_playing_field = playingfield.PlayingField(2 * 5, 2 * 10)
my_game = Game(
    playing_field=my_playing_field,
    output=display.GameDisplay.opencv,
    # output="terminal",
    direction_function=currentDirector(),
)



analyser = analyzer.Analyzer(my_game)
analyser.analyse_game()
