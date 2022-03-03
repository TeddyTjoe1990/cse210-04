
from game.color import Color
from game.point import Point

class Actor:
    '''
    The object that moves in the game. 
    This object will track its desing, position on the screen and its velocity in 2d space.
    '''
    def __init__(self) -> None:
        '''
        Construct an new object. 
        '''
        self._text = ""
        self._font_size = 15
        self._color = Color(255, 255, 255)
        self._position = Point(0,0)  # CREATE A POSITION
        self._velocity = Point(0,0)
    
    def get_text(self):
        '''
        Gets the object textual representation.
        '''
        return self._text


    def get_font_size(self):
        '''
        Get the object size.
        '''
        return self._font_size
    
    def get_color(self):
        '''
        Gets the object color.
        '''
        return self._color
    
    def get_position(self):
        '''
        Gets the object position in 2d. 
        '''
        return self._position

    def get_velocity(self):
        '''
        Gets the object's speed and direction. 
        '''
        return self._velocity

    def move_next(self, max_x, max_y):
        '''
        Moves the object to the next position according its speed. 
        '''
        x = (self._position.get_x() + self._velocity.get_x()) % max_x
        y = (self._position.get_y() + self._velocity.get_y()) % max_y

        self._position = Point(x, y)

    def set_text(self, text):
        '''
        Updates the sign to the given value.
        '''
        self._text = text

    def set_font_size(self, font_size):
        '''
        Udpates the size font according to the given size. 
        '''
        self._font_size = font_size

    def set_color(self, color):
        '''
        Updates the color to the given one. 
        '''
        self._color = color
    
    def set_position(self, position):
        '''
        Updates the position to the given one. 
        '''
        self._position = position

    def set_velocity(self, velocity):
        '''
        Updates the velocity to the given one. 
        '''
        self._velocity = velocity
    
    def __str__(self) -> str:
        return self._text