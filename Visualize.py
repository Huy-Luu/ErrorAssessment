import matplotlib.pyplot as plt

class Visualize:
    @staticmethod
    def scattered(points, wpoints):
        cx, cy = zip(*[(float(i.x),float(i.y)) for i in points])
        wx, wy = zip(*[(float(i.x),float(i.y)) for i in wpoints])
        plt.plot(cx, cy, ".b")
        plt.plot(wx, wy)
        plt.show()