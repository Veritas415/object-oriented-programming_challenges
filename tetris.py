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
import math

class Tetronimo:

    def __init__(self, rotation, shape, color):
        self.rotation = rotation
        self.shape = shape
        self.color = color

class Shape:

    def __init__(self, length, width):
        self.length = length
        self.width = width

print(math.floor(1.22))