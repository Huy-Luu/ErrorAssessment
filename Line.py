import math

class Line():
    def __init__(self, pointA, pointB):
        self.pointA = pointA
        self.pointB = pointB
        self.a = (self.pointA.y - self.pointB.y)/(self.pointA.x - self.pointB.x)
        self.b = self.pointA.y - self.a*self.pointA.x

        print(str(self.a) + "," + str(self.b))

    def distanceToPoint(self, point):
        distance  = abs(-1 * self.a * point.x + point.y - self.b) / abs(self.a)
        return distance
