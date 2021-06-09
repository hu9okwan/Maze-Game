from operator import itemgetter
import json, datetime, os

from .scores import Score

class ScoreManager:
    """
    Representation of a score manager
    """
    FILEPATH = os.path.join("..", "web", "scores.json")

    def __init__(self):
        self._scores = []

    @property
    def scores(self):
        """Property scores (list of scores) """
        return self._scores


    def add_score(self, values):
        """
        Adds an instance of score to be managed
        Args: values(obj)
        Returns: none
        """
        my_dict = dict()
        my_dict["name"] = values.player_name
        my_dict["score"] = values.score
        my_dict["date"] = values.date
        self._scores.append(my_dict)
    
    def get_scores(self):
        """
        returns a list of dictionaries sorted from descending order by score.
        """
        scores_to_return = []
        scores_to_return = sorted(self._scores, key=itemgetter("score"), reverse=True)
        return scores_to_return


    def serialize(self):
        """
        Returns a dictionary of ordered scores
        """
        sorted_score_dict = dict()
        score_list = self.get_scores()
        sorted_score_dict["scores"] = score_list
        return sorted_score_dict


    def to_json(self, json_file = FILEPATH):
        """
        Writes to a json file the contents of objects dictionary
        """
        with open(json_file, 'w') as output:
            json.dump(self.serialize(), output)


    def from_json(self, json_file = FILEPATH):
        """
        Reads a json file to load a object dictionary
        """
        with open(json_file, 'r') as read:
            data = json.load(read)
            view = data.values()
            for list in view: 
                for item in list:
                    new_score = Score(player_name = item["name"], score = item["score"], date = item["date"])
                    self.add_score(new_score)
    


if __name__ == "__main__":
    # FILEPATH = "Scores.json"
    sm = ScoreManager()
    bob = Score("Bob", 1500, datetime.datetime.now().replace(microsecond=0))
    sam = Score("Sam", 1700, datetime.datetime.now().replace(microsecond=0))
    # semibad = Score("bad", 555, '69')
    sm.add_score(bob)
    sm.add_score(sam)
    print(sm.serialize())
    # sm.add_score(semibad)
    # sm.to_json()
    # sm.from_json()
    
    # with open("../scores.json", 'r') as f:
    #     data = json.load(f)
    # print(data)


    # pathname = r"C:\Users\Anson\Documents\BCIT\Object Programming 2515\Group project\Maze_Project\web\scores.json"
    # pathname2 = r"\Maze_Project\web\scores.json"
    # pathname = os.path.join("..", "scores.json")
    # print(pathname)
    # print(os.path.exists(pathname))
    # print(os.path.exists(pathname2))
    # print(pathname)
    # sm.from_json(pathname)
    # print(sm.get_scores())
    #This generates a date and time using datetime with no microseconds
    # now = datetime.datetime.now().replace(microsecond=0)
    