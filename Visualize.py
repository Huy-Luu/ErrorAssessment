import matplotlib.pyplot as plt

class Visualize:
    @staticmethod
    def scattered(points):#, wpoints):
        cx, cy = zip(*[(float(i.x),float(i.y)) for i in points])
        #wx, wy = zip(*[(float(i.x),float(i.y)) for i in wpoints])
        plt.plot(cx, cy, ".b")
        #plt.show()

    @staticmethod
    def line(waypoints):
        wx, wy = zip(*[(float(i.x),float(i.y)) for i in waypoints])
        plt.plot(wx,wy)

    @staticmethod
    def plot():
        plt.show()