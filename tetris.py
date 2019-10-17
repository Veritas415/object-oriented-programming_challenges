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

Design a set of classes corresponding to the different objects in a game of Tetris.

Use UML diagrams to design the relationships between the different classes.
"""


arrayX = []
arrayY = []

for i in range(9):
  arrayX.append(0)

for n in range(19):
  arrayY.append(arrayX)

#print(arrayX)
for j in range(19):
  print("%s" % arrayY[j])




class Tetromino:

    def __init__(self, rotation, shape, color, coordinates, isFalling):
        self.rotation = rotation
        self.shape = shape
        self.color = color
        self.coordinates = coordinates
        self.isFalling = isFalling

