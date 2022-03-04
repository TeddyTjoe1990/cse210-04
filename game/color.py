
class Color:
    '''
    Provide information about itself and convert colors with the use of a tuple. 
    '''
    def __init__(self, red, green, blue, alpha = 255):
        '''
        Creates a new color with the provided colors. 
        '''
        self._red = red
        self._green = green
        self._blue = blue
        self._alpha = alpha

    def to_tuple(self):
        '''
        Gets the color as a tuple of 4 colors. 
        '''
        return (self._red, self._green, self._blue, self._alpha)
