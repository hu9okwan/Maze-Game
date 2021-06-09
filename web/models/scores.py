import datetime

class Score:

    def __init__(self, player_name, score, date):
        """ Initializes private attributes

        Args:
            name (str): name of the player (cannot be empty)
            score (int): score of the player (cannot be negative)
        
        Raises:
            ValueError: name is empty or not string, score is not integer or negative
        """

        if type(player_name) is not str or not player_name:
            raise ValueError("Invalid name.")
        if type(score) is not int or score < 0:
            raise ValueError("Invalid score.")
        if type(date) is not str:
            raise ValueError("Invalid object")
        
        self._player_name = player_name
        self._score = score
        self._date = date

    @property
    def player_name(self):
        """ Property names (str)"""
        return self._player_name

    @property
    def score(self):
        """ Property scores (int)"""
        return self._score

    @property
    def date(self):
        """ Property datetime (datetime)"""
        return self._date

    @property
    def __dict__(self):
        """Returns a dictionary representation of this object"""
        return {'name': self._player_name, 'score': self._score, 'date': self._date}

    # def __str__(self):
    #     """Returns a formatted string of the name and integer value of score """
    #     return f'Score: {self.player_name} ({self._score})'

    # def __gt__(self, other):
    #     """Returns a boolean. Checks if one score is greater than another."""
    #     if type(other) is not type(self):
    #         raise TypeError("Unspported type")
    #     return self._score > other._score

if __name__ == "__main__":
    pass