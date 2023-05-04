import random
from win32api import GetSystemMetrics
import matplotlib.pyplot as plt


# TODO naprawić wiszące wierzchołki, podgrafy, różne prędkosci na tej samej sciezce
class Point:
    def __init__(self, id, connections, weights, x, y, z):
        self.id = id
        self.connections = connections
        self.weights = weights
        self.x = x
        self.y = y
        self.z = z

    @staticmethod
    def create(id, connections, weights, x, y, z):
        return Point(id, connections, weights, x, y, z)


class Tree:
    def __init__(self, size):
        self.map = []
        for i in range(size):
            connections = [random.randrange(0, size) for c in range(4)]
            x = random.random()
            y = random.random()
            z = random.random()
            nPoint = Point.create(i, connections, [], x, y, z)
            self.map.append(nPoint)

        for i, p1 in enumerate(self.map):
            weights = []
            for j, connection in enumerate(p1.connections):
                if p1.id == connection:
                    weights.append(0)
                else:
                    p2 = self.map[connection]
                    w = 1 / ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2 + (p2.z - p1.z) ** 2)
                    weights.append(w)
            self.map[i].weights = weights

    def show(self):
        for i in self.map:
            print(i.id, i.connections, i.weights, i.x, i.y, i.z)

    def plot(self):
        plt.rcParams['toolbar'] = 'None'
        screen_width = GetSystemMetrics(0)
        screen_height = GetSystemMetrics(1)
        fig = plt.figure(figsize=(screen_width, screen_height), dpi=250)
        ax = fig.add_subplot(111, projection='3d')
        ax.set_axis_off()
        fig.canvas.set_window_title('fullscreen_toggle')
        plt.get_current_fig_manager().window.showMaximized()
        for point in self.map:
            ax.scatter(point.x, point.y, point.z)
            for i, connection in enumerate(point.connections):
                ax.plot([point.x, self.map[connection].x], [point.y, self.map[connection].y],
                        [point.z, self.map[connection].z], color='black', alpha=0.5)
        plt.tight_layout()
        plt.show()
