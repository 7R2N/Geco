import random

# TODO naprawić wiszące wierzchołki, podgrafy, improve point coordinates generation
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
            connections = []
            while len(connections) < random.randrange(1, 5):
                new_connection = random.randrange(0, size)
                if new_connection != i and new_connection not in connections:
                    connections.append(new_connection)
            x = random.randrange(0,20)
            y = random.randrange(0,20)
            z = random.randrange(0,20)
            nPoint = Point.create(i, connections, [], x, y, z)
            self.map.append(nPoint)

        while len(connections) < random.randrange(1, 5):
            new_connection = random.randrange(0, size)
            if new_connection != i and new_connection not in connections and len(
                    self.map[new_connection].connections) < 4:
                connections.append(new_connection)
                self.map[new_connection].connections.append(i)

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

    def dict(self):
        points = []
        for i in self.map:
            points.append({
                'id': i.id,
                'connections': i.connections,
                'weights': i.weights,
                'x': i.x,
                'y': i.y,
                'z': i.z,
            })
        return {
            'points': points
        }

    def show(self):
        for i in self.map:
            print(i.id, i.connections, i.weights, i.x, i.y, i.z)
