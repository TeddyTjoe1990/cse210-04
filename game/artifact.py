import random
from game.actor import Actor
from game.point import Point

class Artifact(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self, cell_size = 1):
        super().__init__()
        self._message = ""
        self._cell_size = cell_size
        self._score = 0
        self._y_speed = random.randint(1, 3)
        self._list_of_obj = []
        
    def get_message(self):
        """Gets the artifact's score.
        """
        return self._message
    
    def set_message(self, message):
        """Updates the score to the given one.
        """
        self._message = message

    def get_lists(self):
        return self._list_of_obj

    def move_down(self, max_x, max_y):
        x = self._position.get_x() % max_x
        y = self._position.get_y() + self._y_speed % max_y
    
        if y > max_y:
            x = self._position.get_x() % max_x
            y = 0

        self._position = Point(x, y)
        self._position = self._position.scale(self._cell_size)

        return self._position
    
    def set_lists(self, lista):
        self._list_of_obj = lista


    def get_score(self):
        return self._score

    def set_score(self, points):
        self._score = points

    def __str__(self) -> str:
        return super(Artifact, self).__str__() + str(self._score)
        #self._score = "Score: " + self.get_score() NO
        #return f'Score: {self._score}' NO
