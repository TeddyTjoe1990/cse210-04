
class Point():
    '''
    A distance from a relative origin(0,0).
    '''
    def __init__(self, x, y):
        '''
        Construct a new Point with x and y values. 
        '''
        self._x = x
        self._y = y

    def add(self, other):
        '''
        Add the point with the other given point, returns a new point. 
        '''
        x = self._x + other.get_x()
        y = self._y + other.get_y()
        
        return Point(x, y)

    def equals(self, other):
        '''
        Wheter or not this Point is equal to the given one. 
        '''
        return self._x == other.get_x() and self._y == other.get_y()

    def get_x(self):
        '''
        Returns the horizontal distance.
        '''
        return self._x

    def get_y(self):
        '''
        Returns the vertical distance. 
        '''
        return self._y

    def scale(self, factor):
        '''
        Scales the point with the provider one and returns a new point.
        '''
        return Point(self._x * factor, self._y * factor)