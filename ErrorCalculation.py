import numpy as np

class ErrorCalculation():
    @staticmethod
    def average(data_array):
        sum = 0
        for i in range(0, len(data_array)):
            sum += data_array[i]
        return sum/len(data_array)

    @staticmethod
    def findNearestIndex(point, path):
        dx = [point.x -ipath.x for ipath in path]
        dy = [point.y -ipath.y for ipath in path]
        d = np.hypot(dx, dy)

        idx = np.argmin(d)

        return idx

        