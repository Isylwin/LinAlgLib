import math

class DimensionError(Exception):
    pass

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
            self.magnitude = math.sqrt(sum([x**2 for x in self.coordinates]))

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    @property
    def direction(self):
        try:
            return 1/self.magnitude * self
        
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates


    def __add__(self,other):
        try:
            if(not isinstance(other, Vector)):
                raise TypeError

            if(self.dimension != other.dimension):
                raise DimensionError

            temp = [x+y for x,y in zip(self.coordinates, other.coordinates)]
            return Vector(temp)       
        
        except DimensionError:
            raise DimensionError('The dimensions of the vectors are incompatable.')

        except TypeError:
            raise TypeError('Operand is not a Vector object.')


    def __sub__(self,other):
        try:
            if(not isinstance(other, Vector)):
                raise TypeError

            if(self.dimension != other.dimension):
                raise DimensionError

            temp = [x-y for x,y in zip(self.coordinates, other.coordinates)]
            return Vector(temp)

        except DimensionError:
            raise DimensionError('The dimensions of the vectors are incompatable.')

        except TypeError:
            raise TypeError('Operand is not a Vector object.')


    def __mul__(self,other):
        try:
            o_type = type(other)

            if( not (o_type == int or o_type == float or o_type == long) ):
                raise TypeError

            temp = [other*x for x in self.coordinates]
            return Vector(temp)

        except TypeError:
            raise TypeError('Operand is not a Vector object.')


    def __rmul__(self,other):
        return self*other


