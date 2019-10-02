"""
Challenge: Designing Tetris Using OOP

Let's consider a classic game, Tetris, in terms of OOP. We start off by describing Tetris to find its objects.

Tetris consists of a random sequence of Tetrominos fall down a playing field. The objective of the game is to manipulate these Tetrominos, by moving each one sideways and rotating it by 90 degree units, with the aim of creating a horizontal line of ten blocks without gaps.

In Tetris, really the only object is a Tetromino. It has states of:

    * rotation (in 90 degree units)
    * shape
    * color
    * and behaviors of:
        * falling
        * moving (sideways)
        * rotating
"""
import time

class Shape:

    def __init__(self, borders):
        self.borders = borders

class Tetromino:

    def __init__(self, rotation, shape, color, coordinates, isFalling):
        self.rotation = rotation
        self.shape = shape
        self.color = color
        self.coordinates = coordinates
        self.isFalling = isFalling

    def getRotation(self):
        """Get the Tetromino current 'rotation' value"""
        return self.rotation

    def setRotation(self, value):
        self.rotation = value

    def getShape(self):
        """Get the Tetromino 'shape' value"""
        return self.shape

    def setShape(self, value):
        self.shape = value

    def getColor(self):
        """Get the Tetromino 'color' value"""
        return self.color

    def setColor(self, value):
        self.color = value

    def getCoordinates(self):
        """Get The Tetromino 'coordinates' value"""
        return self.coordinates

    def setCoordinates(self, value):
        self.coordinates = value

    def getIsFalling(self):
        """Get the Tetromino 'isFalling' value"""
        return self.isFalling

    def fall(self):
        """Decrement the y coordinate of a Tetromino's position while it is falling"""
        while self.isFalling:
            time.sleep(.25)
            self.coordinates[1] -- 1

    def land(self):
        """Assign a Tetromino's isFalling value to False"""
        self.isFalling = False