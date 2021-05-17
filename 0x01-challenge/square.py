#!/usr/bin/python3
"""square class that can calculate area and perimeter"""

class Square():
    """square class with attributes width and height"""
    width = 0
    height = 0


    def __init__(self, *args, **kwargs):
        """initializes values"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """Calculates perimeter of square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """special string method for pretty printing"""
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
