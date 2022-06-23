import direction
import playingfield


class BaseDirector:
    def get_direction(
        self, playing_field: playingfield.PlayingField
    ) -> direction.Direction:
        ...
