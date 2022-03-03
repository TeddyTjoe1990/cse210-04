
import pyray
from game.point import Point

class KeyboardService:
    '''
    Detects player key press and give a point that represent a direction. 
    '''
    def __init__(self, cell_size = 1):
        '''
        Constructs a new object service using the specified cell size. 
        '''
        self._cell_size = cell_size

    def get_direction(self):
        '''
        Gets direction according on the key that is press. 
        '''
        dx = 0
        dy = 0

        if pyray.is_key_down(pyray.KEY_LEFT):
            dx = -1
        if pyray.is_key_down(pyray.KEY_RIGHT):
            dx = 1

        direction = Point(dx, dy)
        direction = direction.scale(self._cell_size)
        return direction