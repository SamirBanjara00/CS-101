# A data type for turtle graphics using standard draw.

import math
import stddraw
import sys


class Turtle:
    # Constructs a turtle given its coordinates and angle.
    def __init__(self, x, y, theta):
        self.x = x  # x-coordinate of turtle
        self.y = y  # y-coordinate of turtle
        self.theta = theta  # ccw angle (in degrees) of turtle

    # Rotates this turtle by theta in ccw direction.
    def turnLeft(self, theta):
        self.theta += theta

    # Moves this turtle forward by given amount, with the pen down.
    def goForward(self, stepSize):
        xOld = self.x
        yOld = self.y
        self.x += stepSize * math.cos(math.radians(self.theta))
        self.y += stepSize * math.sin(math.radians(self.theta))
        stddraw.line(xOld, yOld, self.x, self.y)

    # Returns a string representation of this turtle.
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.theta) + ')'


# Unit tests the data type.
def _main():
    n = int(sys.argv[1])
    turtle = Turtle(0.5, 0.0, 180.0 / n)
    stepSize = math.sin(math.radians(180.0 / n))
    stddraw.setPenRadius(0.0)
    for i in range(n):
        turtle.goForward(stepSize)
        turtle.turnLeft(360.0 / n)
    stddraw.show()


if __name__ == '__main__':
    _main()
